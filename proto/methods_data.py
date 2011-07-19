#! /usr/bin/env python
test = [
'ranking_by_geography_id_within_state', 
['dataVersion', 'stateId', 'censusMetricType', 'rankingMetric', 'geographyType', 'geographyId'], 
'http://www.broadbandmap.gov/broadbandmap/almanac/{dataVersion}/rankby/state/{stateId}/{censusMetric}/{rankingMetric}/{geographyType}/id/{geographyId}?properties={properties}&format={format}&callback={functionName}&order={sortOrder}&properties={properties}',
        """
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
]

print 'expected output data (dictionary)', test

string = 'http://www.broadbandmap.gov/broadbandmap/almanac/{dataVersion}/rankby/state/{stateId}/{censusMetric}/{rankingMetric}/{geographyType}/id/{geographyId}?properties={properties}&format={format}&callback={functionName}&order={sortOrder}&properties={properties}'

def get_params(url):
    urlc = url.replace('http://www.broadbandmap.gov/', '')
    #split on ? at most once and take 1st piece
    urlc = urlc.split('?',1)[0]
    urllist = urlc.split('/')
    params = []
    for x in urllist:
        if '{' in x:
            params.append(x[1:-1]) 
    print 'params', params
    print 'urllist', urllist
" format: param, 'rankby', 'state', "
print 'get params from a URL from the scraped docs'
get_params(string)

def create_fxn(params_dict, url_dict):
    # this function is a template for the methods which use call_api to return data
    
    def fxn(params, **keywords):
        pass
        #return self.call_api(dataVersion, 'rankby', 'state', stateId, censusMetricType, rankingMetric,
    pass

