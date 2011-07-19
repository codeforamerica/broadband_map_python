#! /usr/bin/env python

import textwrap

#====Data.py contents...===
#doclinks = [

#Structure:
#key: documentation URL
#docdata = {'

    #def ranking_by_geography_id_within_state(self, dataVersion, stateId, 
            #censusMetricType, rankingMetric, geographyType, geographyId, **kwarg):
#expect = "'broadbandmap', 'almanac', dataVersion, 'rankby', 'state', stateId, censusMetricType, rankingMetric, geographyType, 'id', geographyId"
#name = "ranking_by_geography_id_within_state"
#params = ['dataVersion', 'stateId', 'censusMetric', 'rankingMetric', 'geographyType', 'geographyId']
#name = "ranking_by_geography_id_within_state"
#urlparams = ['broadbandmap', 'almanac', '{dataVersion}', 'rankby', 'state', '{stateId}', '{censusMetric}', '{rankingMetric}', '{geographyType}', 'id', '{geographyId}']
docdata = {'http://www.broadbandmap.gov/developer/api/geography-lookup-api-by-geography-id': [u'This API is designed to find the rankings by any geography type within the state with a specific census metric (population or household) and ranking metric (any of the metrics from provider, demographic, technology or speed). Only the top ten and bottom ten rankings would be returned through the API if the result set is greater than 500; otherwise full ranking list be returned.', u'http://www.broadbandmap.gov/broadbandmap/almanac/{dataVersion}/rankby/state/{stateId}/{censusMetric}/{rankingMetric}/{geographyType}?properties={properties}&format={format}&callback={functionName}&order={sortOrder}&properties={properties}', u'http://www.broadbandmap.gov/broadbandmap/almanac/fall2010/rankby/state/01/population/wirelineproviderequals0/county?format=json&order=asc', u'dataVersion - specify the data version for search(no defaults). Examples: fall2010', u'stateId - specify the state fips code within which the ranking should be done', u"censusMetricType - specify the census metric by which the data has to be aggregated. It can be either 'population' or 'household'", u'rankingMetric - specify one of the various metrics from demographics, technologies, speeds or providers by which the ranking will be done', u'geographyType - specify either one of the following geography type: state, censusplace, msa, usf, county, statesenate, statehouse, congdistrict', u"sortOrder - specify 'asc' for ascending order(default) and 'desc' for descending order", u'properties - specify the properties comma delimited to be included in the result', u'format (optional) - valid formats are xml, json, jsonp with default being xml', u'callback (optional) - jsonp callback function name']}

expected = """
        This API is designed to find the rankings by geography within the
        state for a specific metric (population or household) and rank (any of
        the metrics from provider, demographic, technology or speed). The
        results are the top ten and bottom ten records within the state for the
        particular geography type and my area rankings. Additionally we include
        +/- 5 rankings from the 'my' area rank.

        Call construction:
        http://www.broadbandmap.gov/broadbandmap/almanac/{dataVersion}/rankby/state/{stateId}/{censusMetric}/{rankingMetric}/{geographyType}/id/{geographyId}?properties={properties}&format={format}&callback={functionName}&order={sortOrder}&properties={properties}
        Sample call:
        http://www.broadbandmap.gov/broadbandmap/almanac/fall2010/rankby/state/01/population/wirelineproviderequals0/county/id/01101?format=json&order=asc

        >>> ranking_by_geography_id_within_state('fall2010', '01', 'population',
        ...    'wirelineproviderequals0', 'county', '01101')

        @see
        http://www.broadbandmap.gov/developer/api/almanac-api-ranking-by-geography-id-within-a-state
        """
#print 'EXPECTED', expected       

def extractexampleparams(apicall, samplecall):
    samplecall = samplecall.replace('http://www.broadbandmap.gov/broadbandmap/',
            '').split('/')
    exampleparams = samplecall[:-1] + samplecall[-1].split('?')
    staticparams = apicall.replace('http://www.broadbandmap.gov/broadbandmap/',
            '').split('/')
    staticparams = staticparams[:-1] + staticparams[-1].split('?')
    exampleparams = [v for v in exampleparams if v not in staticparams]
    print "APICALL", exampleparams, 
    #print '\n', staticparams,'\n'
    return "', '".join(exampleparams[:-1])

extractexampleparams('http://www.broadbandmap.gov/broadbandmap/almanac/{dataVersion}/rankby/state/{stateId}/{censusMetric}/{rankingMetric}/{geographyType}/id/{geographyId}?properties={properties}&format={format}&callback={functionName}&order={sortOrder}&properties={properties',
'http://www.broadbandmap.gov/broadbandmap/almanac/fall2010/rankby/state/01/population/wirelineproviderequals0/county/id/01101?format=json&order=asc')

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
        doctext = docwrapper.fill(doctext)    
        params = doccontents[3:]
        methodname = create_method_name(docurl)
        doclist = ['    """', 
                '\n', doctext, '\n', 
                '\n     ', 'Call construction:', 
                '\n     ', apicall, 
                '\n     ', 'Sample call:', 
                '\n     ', samplecall, '\n',
                '\n     ', '>>> ', methodname, "('", 
                extractexampleparams(apicall, samplecall), "')", '\n'
                '\n     ', '@see ', docurl]
        #defstr = "    def " + fxnname + "(self, " + ", ".join(fxnparams) + ", **optargs):"
        return ''.join(doclist)

print createdocstring(docdata)


def fixdocstring(func):

    func.__doc__ = func.__doc__.replace('<arg_a>', 'a: a very common argument')
    #(This is just an example, other string formatting methods can be used as well.)
    return func

    list_params

@fixdocstring
def test(a):
    '''
    Arguments:
    <arg_a>
    '''
    pass
