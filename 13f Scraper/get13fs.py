# Script to scrape 13f filings from the SEC EDGAR website and save it to Excel.

import pandas as pd
import requests
from bs4 import BeautifulSoup
import re

def xml_to_xlsx(xml, filename):

    issuers = xml.body.findAll('nameofissuer')
    cusips = xml.body.findAll('cusip')
    values = xml.body.findAll('value')    
    sshprnamts = xml.body.findAll('sshprnamt')

    columns = [
        "Name of Issuer",
        "CUSIP",
        "Value (x$1000)",
        "Shares"
    ]
    df = pd.DataFrame(columns=columns)

    for issuer, cusip, value, sshprnamt in zip(issuers, cusips, values, sshprnamts):
        row = {
            "Name of Issuer": issuer.text,
            "CUSIP": cusip.text,
            "Value (x$1000)": value.text,
            "Shares": sshprnamt.text,
        }
        df = pd.concat([df, pd.DataFrame([row])], ignore_index=True)

    df.to_excel(filename, index=False)
    print(f"Saved to {filename}")

def download_13f(CIK_list, date):
    for CIK in CIK_list:
        url = f"https://data.sec.gov/rss?cik={CIK}"

        headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.46'
        }

        # access the rss feed showing all recent 13f filings of the given fund
        try:
            response = requests.get(url, headers=headers)
        except Exception as e:
            print(f'Error fetching the URL: {url}')
            print(e)
        rss = BeautifulSoup(response.content, "lxml")
        
        # get fund name
        name = rss.findAll('confirmed-name')[0].text

        # access the web page for the filing for the chosen reference date
        reports = rss.findAll('content-type', attrs={'type': 'text/xml'})
        for report in reports:
            if report.find('report-date').text == date:
                last_report_url = report.find('filing-href').text
        response = requests.get(last_report_url, headers=headers)
        html = BeautifulSoup(response.text, "html.parser")

        # access the xml containing the 13f data
        tags = html.findAll('a', attrs={'href': re.compile('xml')})
        for tag in tags:
            if tag.text.lower() == 'form13finfotable.xml':
                xml_url = tag.get('href')
        xml = requests.get('https://www.sec.gov' + xml_url, headers=headers)
        xml_parsed = BeautifulSoup(xml.content, "lxml")
        filename = f"{date} {name}.xlsx"
        xml_to_xlsx(xml_parsed, filename)

CIK_list = ['1656456', '1649339']  # CIK (Central Index Key) is an identifier used by the SEC. Choose the CIKs of the funds you'd like to download 13f filings for.
date = '2021-12-31'  # enter date in format YYYY-MM-DD

download_13f(CIK_list, date)