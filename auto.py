#!/usr/bin/env python

"""Python class that will generate an API wrapper class, complete with
documentation, from data (e.g. scraped from a website)"""

import textwrap
from api import API, urlopen
import data

class Autowrap(object):
    def __init__(self):
        self.docdata = data.docdata #In format: # key: documentation URL # item: list[1. documentation text 2. API call format 3. Sample API call 4..n.  Parameters and parameter descriptions]
        #self.doclinks = data.doclinks #In format: [docURL1, docURL2]  (list of links to documentation for each API method) 

    def main(self):
        for docurl, doccontents in self.docdata.iteritems():
            doctext, apicall, samplecall = doccontents[0:3]
            paramdoclist = doccontents[4:]
            params = doccontents[3:]


   def _formatparams(self, params):
        """
        Takes list of strings extracted from the api call documentation, figure
        out which ones are static and which are variables, and format accordingly
        for generating a python function.
        """
        formattedparams = []
        for param in params:
        # The broadband map delineates user-inputted vars with { } brackets
        # http://www.broadbandmap.gov/broadbandmap/almanac/{dataVersion}/rankby/state/{stateId}/{censusMetric}/{rankingMetric}/{geographyType}/id/{geographyId}?properties={properties}&format={format}&callback={functionName}&order={sortOrder}&properties={properties}
            if '{' in param: #non-static 
                formattedparams.append(param[1:-1]) #variables
            else:
                formattedparams.append("'%s'" % param) #static text
        return ", ".join(formattedparams)

    def _createfxn(self, fxnname, fxnparams,  apiparams):
        """
        Creates an api wrapper fxn given the name, user-input params, and required
        static text.
        """
        defstr = "    def " + fxnname + "(self, " + ", ".join(fxnparams) + ", **optargs):"
        callstr = "       self.call_api(" + self._formatparams(apiparams) + ", **optargs)" 
        #return defstr + "\n" + callstr
        return (defstr, callstr)

    def _extractexampleparams(self, apicall, samplecall): #API-specific
        """
        This extracts the user-input parameters, as opposed to the static
        params, for this API method based on the documentation provided by
        the Broadbandmap API.
        """
        #compare "apicall" example to "samplecall" example in the docs to figure out
        #which ones params are static and which are vars for user input
        samplecall = samplecall.replace('http://www.broadbandmap.gov/broadbandmap/',
                '').split('/')
        allparams = samplecall[:-1] + samplecall[-1].split('?')
        staticparams = apicall.replace('http://www.broadbandmap.gov/broadbandmap/',
                '').split('/')
        staticparams = staticparams[:-1] + staticparams[-1].split('?')
        userparams = [x for x in allparams if x not in staticparams]
        return (

    def _formatparamdocs(self, paramdoclist):
        result = []
        for param in paramdoclist:
            result.append("@param %s" % param)
        return "\n    ".join(result)

    def _createmethodname(self, api_url): #API-specific
        api_url = api_url.replace('http://www.broadbandmap.gov/developer/api/', '')
        api_url = api_url.replace('-', '_')
        return api_url

    def _createdocstrings(self, docdata):
        docwrapper = textwrap.TextWrapper(initial_indent='    ', subsequent_indent='    ')
            doctext = docwrapper.fill(doctext)    
            methodname = self._createmethodname(docurl)
            doclist = ['    """', 
                    '\n', doctext, 
                    '\n', 
                    '\n    ', 'Parameter list:', 
                    '\n    ', '(note that Format param is hardcoded to be json in this wrapper. Specify other optional parameters by passing named arguments to the wrapper fxn, e.g.', 
                    '\n    ', 'someAPICall(callback="Someoption")) ', 
                    '\n',
                    '\n    ', self._formatparamdocs(paramdoclist), 
                    '\n',
                    '\n    ', 'Call construction:', 
                    '\n    ', apicall, 
                    '\n    ', 'Sample call:', 
                    '\n    ', samplecall, 
                    '\n',
                    '\n    ', '>>> ', methodname, "('", 
                    self._extractexampleparams(apicall, samplecall), "')", 
                    '\n',
                    '\n    ', '@see ', docurl, 
                    '\n',
                    '    """']
            #defstr = "    def " + fxnname + "(self, " + ", ".join(fxnparams) + ", **optargs):"
            return ''.join(doclist)

    #print _createdocstring(data.docdata)
