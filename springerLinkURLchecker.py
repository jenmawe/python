# Sampling the records, there are 2 different errors. One is a redirect to
# Metapress.com. The other is a Page not found, which from tests results in an error on the page.
# Sample used a small set with links to specific errors for testing

# Imports the libraries and beautifulSoup to scrap webpage
import csv
import urllib
import requests
import re
from bs4 import BeautifulSoup
import urllib3

#This helps with those pages that redirect to avoid the error message
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}

#Opens and prepares the file to be read and originally 4 csv files to write results to
#On the second pass, this writes to only 2 files: for urls that work and those that don't
#In addition to a file for any that don't fall in the known categories
csvFile0 = open('springerLink_pass1.csv', encoding='utf-8', mode='r')
csvFile = csvFile0.readlines()[18000:21000]
readCSV = csv.reader(csvFile, delimiter=',')

csvFile1 = open('siteError_pass2.csv', 'a', newline='')
writer1 = csv.writer(csvFile1, delimiter=',')

csvFile2 = open('siteOK_pass2.csv', 'a', newline='')
writer2 = csv.writer(csvFile2, delimiter=',')


#runs through the csv file with the list of urls
#Tests the status first and then triages based on 200 or not
for row in readCSV:
    url = row[2]
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    page = requests.get(url, timeout=40, verify=False, headers=headers)
    statusCode = page.status_code
    if statusCode == 200:
        buy = []
        print('ok')
        html = page.text
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.title.string
        actionsPDF = soup.find_all('div',{'class':"content-type-list__action"})
        links = soup.find_all('a')
        metaphrase = 'metapress'
        metap = metaphrase in title.lower()
        for b in links:
            if 'checkout' in b.attrs['href']:
                buy.append(b)
            else:
                continue
        if metap == True:
            print('This resource redirects to main Metapress site: ', row[0])
            writer1.writerow(row)
        elif len(buy) > 0:
            print('This resource must be bought: ', row[0])
            writer1.writerow(row)
        elif len(actionsPDF) > 2:
            print('Content OK - more than 2 downloads')
            writer2.writerow(row)
        else:
            print('Manually check url: ', row[0])
            writer1.writerow(row)
    else:
        print('Sorry. This page isn\'t working: ', row[0])
        print(row)
        writer1.writerow(row)
        continue

#Closes all files
csvFile0.close()
csvFile1.close()
csvFile2.close()
