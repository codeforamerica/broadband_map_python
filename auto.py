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
        output = []
        for docurl, doccontents in self.docdata.iteritems():
        #for docurl, doccontents in data.exampledocdata_dict.iteritems():
            doctext, apicall, samplecall = doccontents[0:3]
            print docurl
            paramdoclist = doccontents[4:]
            paramsdocs = doccontents[3:]
            staticparams, formatted_userparams = self._extractexampleparams(apicall, samplecall)
            methodname = self._createmethodname(docurl)
            staticparams, formatted_exampleuserparams = self._extractexampleparams(apicall, samplecall)
            defparams, callparams = self._formatparams(staticparams)
            defstr, callstr = self._createfxn(methodname,
                    defparams,
                    callparams)
            output.append(defstr)
            output.append(self._createdocstring(doctext, apicall, samplecall,
                paramdoclist, paramsdocs, methodname, docurl))
            output.append(callstr)
        with open('methodtext.py', 'w') as f:
            f.write(''.join(output))
        #return ''.join(output)

    def _formatparams(self, params):
        """
        Takes list of strings extracted from the api call documentation, figure
        out which ones are static and which are variables, and format accordingly
        for generating a python function.
        """
        defparams = []
        callparams = []
        for param in params:
        # The broadband map delineates user-inputted vars with { } brackets
        # http://www.broadbandmap.gov/broadbandmap/almanac/{dataVersion}/rankby/state/{stateId}/{censusMetric}/{rankingMetric}/{geographyType}/id/{geographyId}?properties={properties}&format={format}&callback={functionName}&order={sortOrder}&properties={properties}
            if '{' in param: #non-static 
                callparams.append(param[1:-1]) #variables
                defparams.append(param[1:-1])
            else:
                callparams.append("'%s'" % param) #static text
        callparams = ", ".join(callparams[:-1])
        defparams = ", ".join(defparams[:-1])
        return (defparams, callparams)

    def _createfxn(self, fxnname, fxnparams,  apiparams):
        """
        Creates an api wrapper fxn given the name, user-input params, and required
        static text.
        """
        defstr = "\n    def " + fxnname + "(self, " + fxnparams + ", **optargs):"
        callstr = "        self.call_api(" + apiparams + ", **optargs) \n" 
        #return defstr + "\n" + callstr
        return (defstr, callstr)

    def _extractexampleparams(self, apicall, samplecall): #API-specific
        """
        This extracts the user-input parameters, as opposed to the static
        params, for this API method based on the documentation provided by
        the Broadbandmap API.
        """
        samplecall = samplecall.replace('http://www.broadbandmap.gov/broadbandmap/',
                '').split('/')
        sampleparams = samplecall[:-1] + samplecall[-1].split('?')
        staticparams = apicall.replace('http://www.broadbandmap.gov/broadbandmap/',
                '').split('/')
        staticparams = staticparams[:-1] + staticparams[-1].split('?')
        exampleuserparams = [x for x in sampleparams if x not in staticparams]
        #return "', '".join(userparams[:-1])
        return (staticparams, "', '".join(exampleuserparams[:-1]))
        # sampleparams: [u'geography', u'congdistrict', u'id', u'0111101', u'format=json'] 
        # staticparams: [u'geography', u'{geographyType}', u'id', u'{geographyId}', u'format={format}&callback={functionName}']
        # userparams: [u'congdistrict', u'0111101', u'format=json']

    def _formatparamdocs(self, paramdoclist):
        result = []
        for param in paramdoclist:
            result.append("@param %s" % param)
        return "\n        ".join(result)

    def _createmethodname(self, api_url): #API-specific
        api_url = api_url.replace('http://www.broadbandmap.gov/developer/api/', '')
        api_url = api_url.replace('-', '_')
        return api_url

    def _createdocstring(self, doctext, apicall, samplecall, paramdoclist,
            paramsdocs, methodname, docurl):
        docwrapper = textwrap.TextWrapper(initial_indent='        ', subsequent_indent='        ')
        doctext = docwrapper.fill(doctext)    
        staticparams, formatted_exampleuserparams = self._extractexampleparams(apicall, samplecall)
        doclist = ['\n', '        """', 
                '\n', doctext, 
                '\n', 
                '\n        ', 'Parameter list:', 
                '\n', docwrapper.fill('**Note that the API\'s format param is hardcoded to be json in this wrapper. Specify other optional parameters by passing named arguments to the wrapper fxn, e.g. someAPICall(callback="Someoption") **'), 
                '\n',
                '\n        ', self._formatparamdocs(paramdoclist), 
                '\n',
                '\n        ', 'Call construction:', 
                '\n        ', apicall, 
                '\n        ', 'Sample call:', 
                '\n        ', samplecall, 
                '\n',
                '\n        ', '>>> ', methodname, "('", formatted_exampleuserparams, "')", 
                '\n',
                '\n        ', '@see ', docurl, 
                '\n',
                '        """', '\n']
        #defstr = "    def " + fxnname + "(self, " + ", ".join(fxnparams) + ", **optargs):"
        return ''.join(doclist)

    #print _createdocstring(data.docdata)

test = Autowrap()
#apicall, samplecall = data.exampledocdata[1:3]
#staticparams, userparams = test._extractexampleparams(apicall, samplecall)
#print staticparams, userparams
print test.main()
