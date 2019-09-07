## Python scripts
This repository has python scripts used for work. 

* createAlepSysNum.py  
This python script expects an ARC report from Aleph with headers for bib doc number, item statistic code, item statistic description, no of items, title, collection, barcode, item status description, item status code, holding doc no. It creates two text files one with the bib sys numbers and one for the holdings sys numbers. This was the first I created and it is tailored only for a specific output.

*  getSysNumbers.py
This python script expects a csv of numbers that need to be formated for Aleph. The script asks if they are holdings or bib system numbers, asks for the name of the csv and the text file. It also removes the extra line from the text file which was a problem in the script above. 

*  springerLinkURLchecker.py
This python script is specific for a csv file of springer urls. I wasn't able to get it working except by going through a number of lines at a time because the site would bump me off.
