# Script to scrape 13f filings from the SEC website and save it to Excel.

import pandas as pd
import requests
from bs4 import BeautifulSoup
import re

def xml_to_xlsx(xml, CIK, year, quarter):

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

    filename = f"{year} Q{quarter} {CIK}.xlsx"
    df.to_excel(filename, index=False)
    print(f"Saved to {filename}")

def download_13f(CIK_list, year, quarter):
    for CIK in CIK_list:
        url = f"https://www.sec.gov/cgi-bin/browse-edgar?CIK={CIK}&owner=exclude&action=getcompany&type=13F-HR"

        headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
        'Accept-Encoding': 'gzip, deflate, br',
        'HOST': 'www.sec.gov',
        }

        # access web page showing all recent 13f filings of the given fund
        response = requests.get(url, headers=headers)
        html = BeautifulSoup(response.text, "html.parser")
        
        # access web page of the most recent 13f filing
        last_report_url = ('https://www.sec.gov' + html.findAll('a', id="documentsbutton")[0]['href'])
        response = requests.get(last_report_url, headers=headers)
        html = BeautifulSoup(response.text, "html.parser")

        # access web page of the xml containing the 13f data
        tags = html.findAll('a', attrs={'href': re.compile('xml')})
        for tag in tags:
            if tag.text.lower() == 'form13finfotable.xml':
                xml_url = tag.get('href')
        xml = requests.get('https://www.sec.gov' + xml_url, headers=headers)
        xml_parsed = BeautifulSoup(xml.content, "lxml")
        xml_to_xlsx(xml_parsed, CIK, year, quarter)

CIK_list = ['1656456', '1649339']
year     = 2021
quarter  = 4

download_13f(CIK_list, str(year), str(quarter))