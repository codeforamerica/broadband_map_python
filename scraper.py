#!/usr/bin/env python

"""
Scraper, BroadBand Maps API.
"""

import re
import json
from urllib2 import urlopen
import urllib
import urlparse

from bs4 import BeautifulSoup as bs

api_urls = []
docs = {}

def find_docs(url):
    """
    Finds the description, structure of the api call, and a sample api call
    from a given BroadbandMap API documentation url.
    """
    soup = bs(urlopen(url).read(), ['fast', 'lxml'])
    desc = soup.find(text=re.compile('^Description')).findNext('p').string
    apicall = soup.find(text='API call')
    if apicall == None:
        apicall = soup.find(text='API Call')
    #lstrip to remove \n at beginning
    apicall = apicall.findPrevious('p').contents[2].lstrip()
    samplecall = soup.find(text='Sample call')
    if samplecall == None:
        samplecall = soup.find(text='Sample Call')
    samplecall = samplecall.findNext('a').string
    return [desc, apicall, samplecall]

def find_links():
    """
    Creates list of links to all API('s) methods for BroadbandMap family of
    APIs.
    """
    # We'll use BeautifulSoup + lxml for parsing.
    url = "http://www.broadbandmap.gov/developer"
    soup = bs(urlopen(url).read(), ['fast', 'lxml'])
    hrefs = soup.findAll('a', href=True)
    api_urls = [ tag['href'] for tag in hrefs 
            if 'http://www.broadbandmap.gov/developer/api' in tag['href']]
    return api_urls

def parse_api():
    api_urls = find_links()
    for url in api_urls:
        print url
        doc = find_docs(url)
        params = find_params(url)
        docs[url] = doc.append(params)
    with open('scraperdocs.txt', 'w') as f:
        f.write(str(docs))

def find_params(url):
    """
    Finds the bulleted list of parameters on given BroadbandMap url.
    Then cleans the list, i.e. takes something like:
        [u'\n', u'dataVersion - specify the data version for      search(no
        defaults). Examples: fall2010', u'\n',]
    and takes out the newlines and weird extra spaces and outputs:
        [u'dataVersion - specify the data version for search(no defaults).
        Examples: fall2010']
    """
    soup = bs(urlopen(url).read(), ['fast', 'lxml'])
    param = soup.find(text='Parameters')
    params = param.findNext('ul').findAll(text=True)
    cleanparams = filter(lambda x: '\n' not in x, params)
    cleanparams = map(lambda x: x.replace("      "," "), cleanparams)
    return cleanparams

def find_paramnames(params):
    """
    Takes a list which contains elements like:
        [u'maxResults - specify the maximum results to be 
        returned - defaulted to 100']
    and outputs:
        [u'maxResults']
    """
    names = []
    for line in params:
        names.append(line.split(' - ', 1)[0])
    return names


#find_links()
#find_docs('http://www.broadbandmap.gov/developer/api/wireless-broadband-api')
params = find_params('http://www.broadbandmap.gov/developer/api/wireless-broadband-api')
find_paramnames(params)
#parse_api()

#if __name__ == '__main__':
    #main()
