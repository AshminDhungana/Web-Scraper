"""Scrape data from Links and store in Excel File"""


import re
from bs4 import BeautifulSoup
from urllib.request import urlopen


def CreateSoup(site: str):
    html = urlopen(site)
    soup =BeautifulSoup(html,'lxml')
    return soup

def main():
    site = input("Enter the URL of site to extract data: ").strip()
    soup = CreateSoup(site)



if __name__ == "__main__":
    main()