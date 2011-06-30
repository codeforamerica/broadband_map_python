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
    soup = bs(urlopen(url).read(), ['fast', 'lxml'])
    desc = soup.find(text=re.compile('^Description')).findNext('p').string
    #lstrip to remove \n at beginning
    apicall = soup.find(text='API call')
    if apicall == None:
        apicall = soup.find(text='API Call')
    apicall = apicall.findPrevious('p').contents[2].lstrip()
    samplecall = soup.find(text='Sample call')
    if samplecall == None:
        samplecall = soup.find(text='Sample Call')
    samplecall = samplecall.findNext('a').string
    return [desc, apicall, samplecall]

def find_links():
    """
    for that EPA dataset.
    """
    # We'll use BeautifulSoup + lxml for parsing.
    url = "http://www.broadbandmap.gov/developer"
    soup = bs(urlopen(url).read(), ['fast', 'lxml'])
    hrefs = soup.findAll('a', href=True)
    #for i in range(len(hrefs)):
        #url = hrefs[i]['href']
        #if "http://www.broadbandmap.gov/developer/api" in url:
            #api_urls.append(url)
    api_urls = [ tag['href'] for tag in hrefs 
            if 'http://www.broadbandmap.gov/developer/api' in ['href']]
    for url in api_urls:
        doc = find_docs(url)
        docs[url] = doc
        print url
    #with open('scraperdocs.txt', 'w') as f:
        #f.write(str(docs))

def find_params(url):
    """
    generate docs for each class by hand, probably.:
    dir(module)
    .__doc__
    Example: http://some_url.com/
    >>> api.somecall(foo)
    """
    soup = bs(urlopen(url).read(), ['fast', 'lxml'])
    param = soup.find(text='Parameters')
    params = param.findNext('ul').findAll(text=True)
    #s.replace("     "," ")
    print params

#find_links()
#find_docs('http://www.broadbandmap.gov/developer/api/wireless-broadband-api')
find_params('http://www.broadbandmap.gov/developer/api/wireless-broadband-api')


#def find_definition_urls(set_of_links):
    #"""Find the available definition URLs for the columns in a table."""
    #definition_dict = {}
    #for link in set_of_links:
        #if link.startswith('http://'):
            #table_dict = {}
            #soup = bs(urlopen(link).read(), ['fast', 'lxml'])
            #unordered_list = soup.find('div', {'id': 'main'}).findAll('ul')[-1]
            #for li in unordered_list.findAll('li'):
                #a = li.findChild('a')
                #table_dict.update({a.string: a.attrs['href']})
            #link_name = re.sub('.*p_table_name=(\w+)&p_topic.*', r'\1',
                               #link).upper()
            #definition_dict.update({link_name: table_dict})
    #return definition_dict

#def create_agency(agency):
    #"""Create an agency text file of definitions."""
    #links = find_table_links(agency)
    #definition_dict = find_definition_urls(links)
    #with open(agency + '.txt', 'w') as f:
        #f.write(str(definition_dict))

#def loop_through_agency(agency):
    #with open(agency + '.txt') as f:
        #data = eval(f.read())
    #for table in data:
        #for column in data[table]:
            #value_link = data[table][column]
            #data[table][column] = grab_definition(value_link)
    #data = json.dumps(data)
    #with open(agency + '_values.json', 'w') as f:
        #f.write(str(data))


#def grab_definition(url):
    #if url.startswith('//'):
        #url = 'http:' + url
    #soup = bs(urlopen(url).read(), ['fast', 'lxml'])
    #try:
        #bold = soup.findAll('b')[1]
        #value = bold.next.next.strip('\n\n')
    #except IndexError:
        #print url
    #except TypeError:
        #print url
    #else:
        #return value
    #return url


#def main():
    #agency = 'radinfo'
    #create_agency(agency)
    #loop_through_agency(agency)

#if __name__ == '__main__':
    #main()
