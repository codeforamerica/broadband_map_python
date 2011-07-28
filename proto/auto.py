#!/usr/bin/env python

"""Python class that will generate an API wrapper class, complete with
documentation, from data (e.g. scraped from a website)"""

import textwrap

def formatparams(params): 
    """
    Takes list of strings extracted from the api call documentation, figure
    out which ones are static and which are variables, and format accordingly
    for generating a python function
    """
    formattedparams = []
    for param in params:
        if '{' in param:
            formattedparams.append(param[1:-1]) #variables
        else:
            formattedparams.append("'%s'" % param) #static text
    return ", ".join(formattedparams)

def createfxn(fxnname, fxnparams,  apiparams):
    defstr = "    def " + fxnname + "(self, " + ", ".join(fxnparams) + ", **optargs):"
    callstr = "       self.call_api(" + formatparams(apiparams) + ", **optargs)" 
    print defstr + "\n" + callstr 

def extractexampleparams(apicall, samplecall):
    """
    This extracts the actual parameters based on the documentation provided by
    the Broadbandmap API.
    """
    #compare "apicall" example to "samplecall" example in the docs to figure out
    #which ones params are static and which are vars for user input
    samplecall = samplecall.replace('http://www.broadbandmap.gov/broadbandmap/',
            '').split('/')
    exampleparams = samplecall[:-1] + samplecall[-1].split('?')
    staticparams = apicall.replace('http://www.broadbandmap.gov/broadbandmap/',
            '').split('/')
    staticparams = staticparams[:-1] + staticparams[-1].split('?')
    exampleparams = [v for v in exampleparams if v not in staticparams]
    #print "APICALL", exampleparams, 
    #print '\n', staticparams,'\n'
    return "', '".join(exampleparams[:-1])

extractexampleparams('http://www.broadbandmap.gov/broadbandmap/almanac/{dataVersion}/rankby/state/{stateId}/{censusMetric}/{rankingMetric}/{geographyType}/id/{geographyId}?properties={properties}&format={format}&callback={functionName}&order={sortOrder}&properties={properties',
'http://www.broadbandmap.gov/broadbandmap/almanac/fall2010/rankby/state/01/population/wirelineproviderequals0/county/id/01101?format=json&order=asc')


def formatparamdocs(paramdoclist):
    result = []
    for param in paramdoclist:
        result.append("@param %s" % param)
    return "\n    ".join(result)


# hmm, so. two ways of getting the sample python call:
# 1. extract from the documentation 2. extract from the call construction example

#item: list, 1. documentation text 2. API call format 3. Sample API call 4..n. Parameters and parameter descriptions

def create_method_name(api_url):
    api_url = api_url.replace('http://www.broadbandmap.gov/developer/api/', '')
    api_url = api_url.replace('-', '_')
    return api_url

def createdocstring(docdata):
    docwrapper = textwrap.TextWrapper(initial_indent='    ', subsequent_indent='    ')
    for docurl, doccontents in docdata.iteritems():
        doctext, apicall, samplecall = doccontents[0:3]
        paramdoclist = doccontents[4:]
        doctext = docwrapper.fill(doctext)    
        params = doccontents[3:]
        methodname = create_method_name(docurl)
        doclist = ['    """', 
                '\n', doctext, '\n', 
                '\n    ', 'Parameter list:', 
                '\n    ', '(note that Format param is hardcoded to be json in this wrapper. Specify other optional parameters by passing named arguments to the wrapper fxn, e.g.', 
                '\n    ', 'someAPICall(callback="Someoption")) ', '\n',
                '\n    ', formatparamdocs(paramdoclist), '\n',
                '\n    ', 'Call construction:', 
                '\n    ', apicall, 
                '\n    ', 'Sample call:', 
                '\n    ', samplecall, '\n',
                '\n    ', '>>> ', methodname, "('", 
                extractexampleparams(apicall, samplecall), "')", '\n',
                '\n    ', '@see ', docurl, '\n',
                '    """']
        #defstr = "    def " + fxnname + "(self, " + ", ".join(fxnparams) + ", **optargs):"
        return ''.join(doclist)

