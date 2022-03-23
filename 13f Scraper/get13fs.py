# Script to download data from 13f filings from the SEC website. 
# I coded this in 2018; it looks like the sec.gov URL is forbidden now unfortunately. The txt to xlsx parser still works.

import urllib
import requests
import xlwings as xw

def download_urls(year, quarter):
    # Get next quarter b/c SEC categorizes 13fs based the quarter when it was actually filed
    if quarter == 4:
        sec_year = str(int(year) + 1)
        sec_quarter = 1
    else:
        sec_year = year
        sec_quarter = str(int(quarter) + 1)

    url = "https://www.sec.gov/Archives/edgar/full-index/%s/QTR%s/master.idx" % (sec_year, sec_quarter)
    
    print('Downloading URLs from %s' % url)

    sourceData = urllib.request.urlopen(url).read()
    splitSource = sourceData.decode().split('\n') 

    filepath = '%s Q%s URLs.txt' % (year, quarter)
    saveFile = open(filepath, 'a')

    for eachLine in splitSource:
        splitLine = eachLine.split('|')
        if '|' in eachLine:
            saveFile.write(eachLine+'\n')

def download_13f(CIK_list, year, quarter):
    for CIK in CIK_list:
        filepath = '%s Q%s URLs.txt' % (year, quarter)
        file = open(filepath, 'r')
        
        urlEnd = ""
        for line in file.readlines():
            splitLine = line.split('|')
            if (splitLine[0] == CIK) and (splitLine[2] == '13F-HR'):
                urlEnd = splitLine[4]
        if urlEnd == "": print('CIK %s not found in file %s' % (CIK, filepath))
        
        fullURL = "https://www.sec.gov/Archives/"+urlEnd

        sourceData = urllib.request.urlopen(fullURL).read()
        splitSource = sourceData.decode().split('\n')

        saveFilepath = '13f Text Files/%s Q%s %s.txt' % (year, quarter, CIK)
        saveFile = open(saveFilepath, 'a')
        print(saveFilepath+' created')

        for eachLine in splitSource:
            saveFile.write(eachLine+'\n')

def txt_to_xlsx(CIK_list, year, quarter):
    nameTag = "nameOfIssuer>"
    cusipTag = "cusip>"
    sharesTag = "sshPrnamt>"
    sharesTypeTag = "sshPrnamtType>"
    valueTag = "value>"
    putCallTag = "putCall>"

    row = 1 # first row is headers
    manager_col = 1
    CIK_col = 2
    date_col = 3
    security_name_col = 4
    cusip_col = 5
    shares_col = 6
    shares_type_col = 7
    put_call_col = 8
    value_col = 9

    wb = xw.Book('Manager List.xlsx')
    sht = wb.sheets['13f Data']

    for CIK in CIK_list:
        filepath = '13f Text Files/%s Q%s %s.txt' % (year, quarter, CIK)
        file = open(filepath, 'r')

        manager_name = ""
        for line in file.readlines():
            if not manager_name and '<name>' in line:
                    manager_name = parseLine(line)
            if nameTag in line:
                row += 1 # make new row for new security
                sht.range(row, security_name_col).value = parseLine(line).replace('amp;','') 
                sht.range(row, manager_col).value = manager_name
                sht.range(row, CIK_col).value = CIK
                sht.range(row, date_col).value = year+' Q'+quarter
            if cusipTag in line:
                sht.range(row, cusip_col).value = parseLine(line) 
            if sharesTag in line:
                sht.range(row, shares_col).value = parseLine(line)
            if sharesTypeTag in line:
                sht.range(row, shares_type_col).value = parseLine(line) 
            if putCallTag in line:
                sht.range(row, put_call_col).value = parseLine(line) 
            if valueTag in line:
                sht.range(row, value_col).value = parseLine(line) 
        print(manager_name+' complete')
        file.close()

def parseLine(line):
    return line[line.find('>')+1:line.find('</')]

# Be sure to enter inputs as text, not numbers
CIK_list = ['1353316','1384982']
year     = '2018'
quarter  = '1'

#Create a text file containing URLs to all 13fs for a given quarter
download_urls(year, quarter)

#Download 13fs using the URL file and save the 13f text files to a folder
download_13f(CIK_list, year, quarter)

#Transfer 13f data from text files to existing xlsx file 
txt_to_xlsx(CIK_list, year, quarter)