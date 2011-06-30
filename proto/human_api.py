#!/usr/bin/env python

"""
Create part of the API by hand. I will use to help create the machine-based
wrapper generator shortly.

Uses Python Api Module
'git submodule add git://github.com/codeforamerica/Python-API-Module.git api'
"""

from urllib import quote
from urllib import urlencode

from api import API, urlopen

class BroadbandMap(API):

    def __init__(self):
        super(Wrapper, self).__init__()
        self.base_url = "http://www.broadbandmap.gov/developer/api"
        self.output_format = 'json'
        self.required_params = {'format': 'json'}

    def call_api(self, *args, **kwargs):
        """Exposed method to connect and query the EPA's API."""
        try:
            output_format = kwargs.pop('output_format')
        except KeyError:
            output_format = self.output_format
        url_string = "/".join([x.strip() for x in args])
        url_options = urlencode(kwargs)
        if url_options:
            url_string = self.base_url + url_string + "?format=json&" + url_options
        else: url_string = self.base_url + url_string + "?format=json"
        print url_string
        #json_data = urlopen(url_string).read()
        #data = self._format_data(output_format, xml_data)
        #return data

class Almanac(BroadbandMap):
    
    def __init__(self):
        super(BroadbandMap, self).__init__()
        self.base_url = 'http://www.broadbandmap.gov/broadbandmap/almanac/'
    
    def ranking_by_geography_id_within_state(self, dataVersion, stateId, 
            censusMetricType, rankingMetric, geographyType, geographyId, **kwarg):
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
        self.call_api(dataVersion, 'rankby', 'state', stateId, censusMetricType, rankingMetric,
                geographyType, 'id', geographyId, **kwarg)

foo = Almanac()
foo.ranking_by_geography_id_within_state('fall2010', '01', 'population',
'wirelineproviderequals0', 'county', '01101', order='asc', format='json')
foo.ranking_by_geography_id_within_state('fall2010', '01', 'population',
'wirelineproviderequals0', 'county', '01101')
