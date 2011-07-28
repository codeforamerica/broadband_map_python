#!/usr/bin/env python

"""Python class that will generate an API wrapper class, complete with
documentation, from data (e.g. scraped from a website)"""

import textwrap
from api import API, urlopen

class AutoWrap(object):
    def _formatparams(params): 
        """
        Takes list of strings extracted from the api call documentation, figure
        out which ones are static and which are variables, and format accordingly
        for generating a python function, aka
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

    def _createfxn(fxnname, fxnparams,  apiparams):
        """
        Creates an api wrapper fxn given the name, user-input params, and required
        static text.
        """
        defstr = "    def " + fxnname + "(self, " + ", ".join(fxnparams) + ", **optargs):"
        callstr = "       self.call_api(" + _formatparams(apiparams) + ", **optargs)" 
        return defstr + "\n" + callstr 

    def _extractexampleparams(apicall, samplecall):
        """
        This extracts the user-input parameters based on the documentation provided by
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
        return "', '".join(exampleparams[:-1])

    def _formatparamdocs(paramdoclist):
        result = []
        for param in paramdoclist:
            result.append("@param %s" % param)
        return "\n    ".join(result)

    def _create_method_name(api_url):
        api_url = api_url.replace('http://www.broadbandmap.gov/developer/api/', '')
        api_url = api_url.replace('-', '_')
        return api_url

    def _createdocstring(docdata):
        docwrapper = textwrap.TextWrapper(initial_indent='    ', subsequent_indent='    ')
        for docurl, doccontents in docdata.iteritems():
            doctext, apicall, samplecall = doccontents[0:3]
            paramdoclist = doccontents[4:]
            doctext = docwrapper.fill(doctext)    
            params = doccontents[3:]
            methodname = _create_method_name(docurl)
            doclist = ['    """', 
                    '\n', doctext, '\n', 
                    '\n    ', 'Parameter list:', 
                    '\n    ', '(note that Format param is hardcoded to be json in this wrapper. Specify other optional parameters by passing named arguments to the wrapper fxn, e.g.', 
                    '\n    ', 'someAPICall(callback="Someoption")) ', '\n',
                    '\n    ', _formatparamdocs(paramdoclist), '\n',
                    '\n    ', 'Call construction:', 
                    '\n    ', apicall, 
                    '\n    ', 'Sample call:', 
                    '\n    ', samplecall, '\n',
                    '\n    ', '>>> ', methodname, "('", 
                    _extractexampleparams(apicall, samplecall), "')", '\n',
                    '\n    ', '@see ', docurl, '\n',
                    '    """']
            #defstr = "    def " + fxnname + "(self, " + ", ".join(fxnparams) + ", **optargs):"
            return ''.join(doclist)
