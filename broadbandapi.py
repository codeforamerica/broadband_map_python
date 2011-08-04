#!/usr/bin/env python

"""
The National Broadband Map is a tool to search, analyze and map broadband availability across the United States.
Created and maintained by the NTIA, in collaboration with the FCC, and in partnership with 50 states, five territories and the District of Columbia. 
"""

from api import API


class BroadbandAPI(API):
"""
Python wrapper for the US National BroadbandMap API.
See www.broadbandmap.gov/developer for more information. 
"""
    def __init__(self):
        pass

    def geography_lookup_api_by_geography_id(self, geographyType, geographyId, **optargs):
        """
        This API allows you to find a geography of a specified
        geography type by the geography id.

        Parameter list:
        **Note that the API's format param is hardcoded to be json in
        this wrapper. Specify other optional parameters by passing
        named arguments to the wrapper fxn, e.g.
        someAPICall(callback="Someoption") **

        @param geographyId: specify the geography id to search for demographics.
        @param format (optional): Valid formats are xml, json, jsonp with default being xml.
        @param callback (optional): jsonp callback function name.

        Call construction:
        http://www.broadbandmap.gov/broadbandmap/geography/{geographyType}/id/{geographyId}?format={format}&callback={functionName}
        Sample call:
        http://www.broadbandmap.gov/broadbandmap/geography/congdistrict/id/0111101?format=json

        >>> geography_lookup_api_by_geography_id('congdistrict', '0111101')

        @see http://www.broadbandmap.gov/developer/api/geography-lookup-api-by-geography-id
        """
        self.call_api('geography', geographyType, 'id', geographyId, **optargs) 

    def speed_test_api_minimum_and_maximum_quartile_speeds_by_geography_type(self, geographyType, **optargs):
        """
        This API returns the minimum and maximum quartile speeds by
        geography type within the nation.

        Parameter list:
        **Note that the API's format param is hardcoded to be json in
        this wrapper. Specify other optional parameters by passing
        named arguments to the wrapper fxn, e.g.
        someAPICall(callback="Someoption") **

        @param speedTestType (optional) - specify the speed test type among any,ookla,mlab with default being any
        @param format (optional) - valid formats are xml, json, jsonp with default being xml
        @param callback (optional) - jsonp callback function name

        Call construction:
        http://www.broadbandmap.gov/broadbandmap/speedtest/{geographyType}/quartile?testtype={speedTestType}&format={format}&callback={functionName}
        Sample call:
        http://www.broadbandmap.gov/broadbandmap/speedtest/state/quartile?format=json

        >>> speed_test_api_minimum_and_maximum_quartile_speeds_by_geography_type('state')

        @see http://www.broadbandmap.gov/developer/api/speed-test-api-minimum-and-maximum-quartile-speeds-by-geography-type
        """
        self.call_api('speedtest', geographyType, 'quartile', **optargs) 

    def almanac_api_ranking_by_geography_type_within_a_state(self, dataVersion, stateId, censusMetric, rankingMetric, geographyType, **optargs):
        """
        This API is designed to find the rankings by any geography
        type within the state with a specific census metric
        (population or household) and ranking metric (any of the
        metrics from provider, demographic, technology or speed). Only
        the top ten and bottom ten rankings would be returned through
        the API if the result set is greater than 500; otherwise full
        ranking list be returned.

        Parameter list:
        **Note that the API's format param is hardcoded to be json in
        this wrapper. Specify other optional parameters by passing
        named arguments to the wrapper fxn, e.g.
        someAPICall(callback="Someoption") **

        @param stateId - specify the state fips code within which the ranking should be done
        @param censusMetricType - specify the census metric by which the data has to be aggregated. It can be either 'population' or 'household'
        @param rankingMetric - specify one of the various metrics from demographics, technologies, speeds or providers by which the ranking will be done
        @param geographyType - specify either one of the following geography type: state, censusplace, msa, usf, county, statesenate, statehouse, congdistrict
        @param sortOrder - specify 'asc' for ascending order(default) and 'desc' for descending order
        @param properties - specify the properties comma delimited to be included in the result
        @param format (optional) - valid formats are xml, json, jsonp with default being xml
        @param callback (optional) - jsonp callback function name

        Call construction:
        http://www.broadbandmap.gov/broadbandmap/almanac/{dataVersion}/rankby/state/{stateId}/{censusMetric}/{rankingMetric}/{geographyType}?properties={properties}&format={format}&callback={functionName}&order={sortOrder}&properties={properties}
        Sample call:
        http://www.broadbandmap.gov/broadbandmap/almanac/fall2010/rankby/state/01/population/wirelineproviderequals0/county?format=json&order=asc

        >>> almanac_api_ranking_by_geography_type_within_a_state('fall2010', '01', 'population', 'wirelineproviderequals0', 'county')

        @see http://www.broadbandmap.gov/developer/api/almanac-api-ranking-by-geography-type-within-a-state
        """
        self.call_api('almanac', dataVersion, 'rankby', 'state', stateId, censusMetric, rankingMetric, geographyType, **optargs) 

    def speed_test_api_by_geography_type_and_geography_name(self, geographyType, geographyNames, **optargs):
        """
        This API returns the speed test results for a particular
        geography type (e.g., state, congressional district) and
        geography name (e.g., Virginia).

        Parameter list:
        **Note that the API's format param is hardcoded to be json in
        this wrapper. Specify other optional parameters by passing
        named arguments to the wrapper fxn, e.g.
        someAPICall(callback="Someoption") **

        @param geographyNames - specify the geography names to search for separated by commas and a maximum of 10 are allowed
        @param speedTestType (optional) - specify the speed test type among any,ookla,mlab with default being any
        @param format (optional) - valid formats are xml, json, jsonp with default being xml
        @param callback (optional) - jsonp callback function name

        Call construction:
        http://www.broadbandmap.gov/broadbandmap/speedtest/{geographyType}/names/{geographyNames}?testtype={speedTestType}&format={format}&callback={functionName}
        Sample call:
        http://www.broadbandmap.gov/broadbandmap/speedtest/state/names/alabama,arizona?format=json

        >>> speed_test_api_by_geography_type_and_geography_name('state', 'alabama,arizona')

        @see http://www.broadbandmap.gov/developer/api/speed-test-api-by-geography-type-and-geography-name
        """
        self.call_api('speedtest', geographyType, 'names', geographyNames, **optargs) 

    def almanac_api_ranking_by_geography_type_within_the_nation(self, dataVersion, censusMetric, rankingMetric, geographyType, **optargs):
        """
        This API is designed to find the rankings by any geography
        type within the nation with a specific census metric
        (population or household) and ranking metric (any of the
        metrics from provider, demographic, technology or speed).
        Support for full list of rankings by nation is not allowed for
        geography types (e.g., county, census place, usf) so only the
        top ten and bottom ten rankings would be returned through the
        API.

        Parameter list:
        **Note that the API's format param is hardcoded to be json in
        this wrapper. Specify other optional parameters by passing
        named arguments to the wrapper fxn, e.g.
        someAPICall(callback="Someoption") **

        @param censusMetricType - specify the census metric by which the data has to be aggregated. It can be either 'population' or 'household'
        @param rankingMetric - specify one of the various metrics from demographics, technologies, speeds or providers by which the ranking will be done
        @param geographyType - specify either one of the following geography type: state, censusplace, msa, usf, county, statesenate, statehouse, congdistrict, tribalnation
        @param sortOrder - specify 'asc' for ascending order(default) and 'desc' for descending order
        @param properties - specify the properties comma delimited to be included in the result
        @param format (optional) - valid formats are xml, json, jsonp with default being xml
        @param callback (optional) - jsonp callback function name

        Call construction:
        http://www.broadbandmap.gov/broadbandmap/almanac/{dataVersion}/rankby/nation/{censusMetric}/{rankingMetric}/{geographyType}?properties={properties}&format={format}&callback={functionName}&order={sortOrder}&properties={properties}
        Sample call:
        http://www.broadbandmap.gov/broadbandmap/almanac/fall2010/rankby/nation/population/wirelineproviderequals0/county?format=json&order=asc

        >>> almanac_api_ranking_by_geography_type_within_the_nation('fall2010', 'population', 'wirelineproviderequals0', 'county')

        @see http://www.broadbandmap.gov/developer/api/almanac-api-ranking-by-geography-type-within-the-nation
        """
        self.call_api('almanac', dataVersion, 'rankby', 'nation', censusMetric, rankingMetric, geographyType, **optargs) 

    def wireline_broadband_api(self, dataVersion, **optargs):
        """
        This API returns all the wireline providers within a US census
        block given a passed latitude and longitude.

        Parameter list:
        **Note that the API's format param is hardcoded to be json in
        this wrapper. Specify other optional parameters by passing
        named arguments to the wrapper fxn, e.g.
        someAPICall(callback="Someoption") **

        @param latitude - latitude of a point. Example: 41.486857
        @param longitude - longitude of a point. Example: -71.294392
        @param maxResults - specify the maximum results to be returned - defaulted to 100
        @param format (optional) - valid formats are xml, json, jsonp with default being xml
        @param callback (optional) - jsonp callback function name

        Call construction:
        http://www.broadbandmap.gov/broadbandmap/broadband/{dataVersion}/wireline?latitude={latitude}&longitude=-{longitude}&maxresults={maxResults}&format={format}&callback={functionName}
        Sample call:
        http://www.broadbandmap.gov/broadbandmap/broadband/fall2010/wireline?latitude=42.456&longitude=-74.987&format=json

        >>> wireline_broadband_api('fall2010')

        @see http://www.broadbandmap.gov/developer/api/wireline-broadband-api
        """
        self.call_api('broadband', dataVersion, 'wireline', **optargs) 

    def geography_lookup_api_by_name_of_specific_geography_type_within_a_state(self, stateFips, geographyType, geographyName, **optargs):
        """
        This API returns geographies by name of a specific geography
        type within a state.

        Parameter list:
        **Note that the API's format param is hardcoded to be json in
        this wrapper. Specify other optional parameters by passing
        named arguments to the wrapper fxn, e.g.
        someAPICall(callback="Someoption") **

        @param geographyType : specify either one of the following geography type: county, censusplace, msa, usf,  statesenate, statehouse, congdistrict, tribalnation
        @param geographyName: specify the geography name with atleast 3 leading characters.
        @param maxResults: specify the maximum results to be returned. defaulted to 100.
        @param all: if true returns the complete set of results.
        @param format (optional): Valid formats are xml, json, jsonp with default being xml.
        @param callback (optional): jsonp callback function name.

        Call construction:
        http://www.broadbandmap.gov/broadbandmap/geography/state/{stateFips}/{geographyType}/name/{geographyName}?maxresults={maxResults}&all={all}&format={format}&callback={functionName}
        Sample call:
        http://www.broadbandmap.gov/broadbandmap/geography/state/17/county/name/mar?format=json

        >>> geography_lookup_api_by_name_of_specific_geography_type_within_a_state('17', 'county', 'mar')

        @see http://www.broadbandmap.gov/developer/api/geography-lookup-api-by-name-of-specific-geography-type-within-a-state
        """
        self.call_api('geography', 'state', stateFips, geographyType, 'name', geographyName, **optargs) 

    def almanac_api_ranking_by_geography_id_within_the_nation(self, dataVersion, censusMetric, rankingMetric, geographyType, geographyId, **optargs):
        """
        This API is designed to find the rankings by any geography ID
        within the nation with a specific census metric (population or
        household) and ranking metric (any of the metrics from
        provider, demographic, technology or speed). The results are
        the top ten and bottom ten rankings within the nation for the
        particular geography type and my area rankings include +/- 5
        rankings from the my area rank.

        Parameter list:
        **Note that the API's format param is hardcoded to be json in
        this wrapper. Specify other optional parameters by passing
        named arguments to the wrapper fxn, e.g.
        someAPICall(callback="Someoption") **

        @param censusMetricType - specify the census metric by which the data has to be aggregated. It can be either 'population' or 'household'
        @param rankingMetric - specify one of the various metrics from demographics, technologies, speeds or providers by which the ranking will be done
        @param geographyType - specify either one of the following geography type: state, censusplace, msa, usf, county, statesenate, statehouse, congdistrict, tribalnation
        @param geographyId - specify the my area geography ID to be ranked
        @param sortOrder - specify 'asc' for ascending order (default) and 'desc' for descending order
        @param Properties - specify the properties comma delimited to be included in the results

        Call construction:
        http://www.broadbandmap.gov/broadbandmap/almanac/{dataVersion}/rankby/nation/{censusMetric}/{rankingMetric}/{geographyType}/id/{geographyId}?properties={properties}&format={format}&callback={functionName}&order={sortOrder}&properties={properties}
        Sample call:
        http://www.broadbandmap.gov/broadbandmap/almanac/fall2010/rankby/nation/population/wirelineproviderequals0/county/id/51117?format=json&order=asc

        >>> almanac_api_ranking_by_geography_id_within_the_nation('fall2010', 'population', 'wirelineproviderequals0', 'county', '51117')

        @see http://www.broadbandmap.gov/developer/api/almanac-api-ranking-by-geography-id-within-the-nation
        """
        self.call_api('almanac', dataVersion, 'rankby', 'nation', censusMetric, rankingMetric, geographyType, 'id', geographyId, **optargs) 

    def broadband_summary_api_nation(self, dataVersion, censusMetricType, **optargs):
        """
        This API returns broadband summary data for the entire United
        States. It is designed to retrieve broadband summary data and
        census metrics (population or households) combined as search
        criteria. The data includes wireline and wireless providers,
        different technologies and broadband speeds reported in the
        particular area being searched for on a scale of 0 to 1.

        Parameter list:
        **Note that the API's format param is hardcoded to be json in
        this wrapper. Specify other optional parameters by passing
        named arguments to the wrapper fxn, e.g.
        someAPICall(callback="Someoption") **

        @param censusMetricType - specify the census metric by which the data has to be aggregated. It can be either 'population' or 'household'
        @param format (optional) - valid formats are xml, json, jsonp with default being xml
        @param callback (optional) - jsonp callback function name

        Call construction:
        http://www.broadbandmap.gov/broadbandmap/analyze/{dataVersion}/summary/{censusMetricType}/nation?format={format}&callback={callback}
        Sample call:
        http://www.broadbandmap.gov/broadbandmap/analyze/fall2010/summary/population/nation?format=json

        >>> broadband_summary_api_nation('fall2010', 'population')

        @see http://www.broadbandmap.gov/developer/api/broadband-summary-api-nation
        """
        self.call_api('analyze', dataVersion, 'summary', censusMetricType, 'nation', **optargs) 

    def broadband_provider_api_all_providers(self, , **optargs):
        """
        The Broadband Provider API searches for all providers with a
        specified name.

        Parameter list:
        **Note that the API's format param is hardcoded to be json in
        this wrapper. Specify other optional parameters by passing
        named arguments to the wrapper fxn, e.g.
        someAPICall(callback="Someoption") **

        @param callback (optional): jsonp callback function name.

        Call construction:
        http://www.broadbandmap.gov/broadbandmap/provider?format={format}&callback={functionName}
        Sample call:
        http://www.broadbandmap.gov/broadbandmap/provider?format=json

        >>> broadband_provider_api_all_providers('')

        @see http://www.broadbandmap.gov/developer/api/broadband-provider-api-all-providers
        """
        self.call_api('provider', **optargs) 

    def community_anchor_institutions_api_by_geography_type_and_geography_id(self, dataVersion, geographyType, geographyIds, **optargs):
        """
        This API allows the user to retrieve the broadband
        availability among the Community Anchor Institutions by
        geography type and ID.

        Parameter list:
        **Note that the API's format param is hardcoded to be json in
        this wrapper. Specify other optional parameters by passing
        named arguments to the wrapper fxn, e.g.
        someAPICall(callback="Someoption") **

        @param geographyType - specify either one of the following geography type: state, county, censusplace, msa, usf, statesenate, statehouse, congdistrict, tribalnation
        @param geographyIds - specify the geography IDs to search for separated by commas and a maximum of 10 are allowed
        @param format (optional) - valid formats are xml, json, jsonp with default being xml
        @param callback (optional) - jsonp callback function name

        Call construction:
        http://www.broadbandmap.gov/broadbandmap/cai/{dataVersion}/{geographyType}/ids/{geographyIds}?format={format}&callback={functionName}
        Sample call:
        http://www.broadbandmap.gov/broadbandmap/cai/fall2010/state/ids/01,02?format=json

        >>> community_anchor_institutions_api_by_geography_type_and_geography_id('fall2010', 'state', '01,02')

        @see http://www.broadbandmap.gov/developer/api/community-anchor-institutions-api-by-geography-type-and-geography-id
        """
        self.call_api('cai', dataVersion, geographyType, 'ids', geographyIds, **optargs) 

    def btop_funding_api_nation(self, , **optargs):
        """
        This API returns BTOP funding for the entire United States.

        Parameter list:
        **Note that the API's format param is hardcoded to be json in
        this wrapper. Specify other optional parameters by passing
        named arguments to the wrapper fxn, e.g.
        someAPICall(callback="Someoption") **

        @param callback (optional) - jsonp callback function name

        Call construction:
        http://www.broadbandmap.gov/broadbandmap/btop/nation?format={format}&callback={functionName}
        Sample call:
        http://www.broadbandmap.gov/broadbandmap/btop/nation?format=json

        >>> btop_funding_api_nation('')

        @see http://www.broadbandmap.gov/developer/api/btop-funding-api-nation
        """
        self.call_api('btop', 'nation', **optargs) 

    def wireless_broadband_api(self, dataVersion, **optargs):
        """
        This API returns all the wireless providers within a US census
        block given a passed latitude and longitude.

        Parameter list:
        **Note that the API's format param is hardcoded to be json in
        this wrapper. Specify other optional parameters by passing
        named arguments to the wrapper fxn, e.g.
        someAPICall(callback="Someoption") **

        @param latitude - latitude of a point. Example: 41.486857
        @param longitude - longitude of a point. Example: -71.294392
        @param maxResults - specify the maximum results to be returned - defaulted to 100
        @param format (optional) - valid formats are xml, json, jsonp with default being xml
        @param callback (optional) - jsonp callback function name

        Call construction:
        http://www.broadbandmap.gov/broadbandmap/broadband/{dataVersion}/wireless?latitude={latitude}&longitude=-{longitude}&maxresults={maxResults}&format={format}&callback={functionName}
        Sample call:
        http://www.broadbandmap.gov/broadbandmap/broadband/fall2010/wireless?latitude=42.456&longitude=-74.987&format=json

        >>> wireless_broadband_api('fall2010')

        @see http://www.broadbandmap.gov/developer/api/wireless-broadband-api
        """
        self.call_api('broadband', dataVersion, 'wireless', **optargs) 

    def bip_funding_api_by_state_name(self, stateNames, **optargs):
        """
        This API allows the user to find the BIP funding allocated to
        states by specifying the state names.

        Parameter list:
        **Note that the API's format param is hardcoded to be json in
        this wrapper. Specify other optional parameters by passing
        named arguments to the wrapper fxn, e.g.
        someAPICall(callback="Someoption") **

        @param format (optional): Valid formats are xml, json, jsonp with default being xml.
        @param callback (optional): jsonp callback function name.

        Call construction:
        http://www.broadbandmap.gov/broadbandmap/bip/states/{stateNames}?format={format}&callback={functionName}
        Sample call:
        http://www.broadbandmap.gov/broadbandmap/bip/states/alaska,alabama?format=json

        >>> bip_funding_api_by_state_name('alaska,alabama')

        @see http://www.broadbandmap.gov/developer/api/bip-funding-api-by-state-name
        """
        self.call_api('bip', 'states', stateNames, **optargs) 

    def community_anchor_institutions_api_nation(self, dataVersion, **optargs):
        """
        This API allows the user to retrieve the broadband
        availability among the Community Anchor Institutions for the
        entire United States.

        Parameter list:
        **Note that the API's format param is hardcoded to be json in
        this wrapper. Specify other optional parameters by passing
        named arguments to the wrapper fxn, e.g.
        someAPICall(callback="Someoption") **

        @param format (optional) - Valid formats are xml, json, jsonp with default being xml
        @param callback (optional) - jsonp callback function name

        Call construction:
        http://www.broadbandmap.gov/broadbandmap/cai/{dataVersion}/nation?format={format}&callback={functionName}
        Sample call:
        http://www.broadbandmap.gov/broadbandmap/cai/fall2010/nation?format=json

        >>> community_anchor_institutions_api_nation('fall2010')

        @see http://www.broadbandmap.gov/developer/api/community-anchor-institutions-api-nation
        """
        self.call_api('cai', dataVersion, 'nation', **optargs) 

    def community_anchor_institutions_closest_by_latitude_and_longitude(self, , **optargs):
        """
        This API returns the closest community anchor institutions by
        latitude and longitude

        Parameter list:
        **Note that the API's format param is hardcoded to be json in
        this wrapper. Specify other optional parameters by passing
        named arguments to the wrapper fxn, e.g.
        someAPICall(callback="Someoption") **

        @param longitude - longitude of a point. Example: -71.294392
        @param Maxresults (optional) - maximum number of results (default 25, maximum 100)
        @param format (optional) - valid formats are xml, json, jsonp with default being xml
        @param callback (optional) - jsonp callback function name

        Call construction:
        http://www.broadbandmap.gov/broadbandmap/cai/closest?latitude={latitude}&longitude={longitude}&maxresults={maxResults}&format={format}&callback={functionName}
        Sample call:
        http://www.broadbandmap.gov/broadbandmap/cai/closest?latitude=41.486857&longitude=-71.294392&maxresults=2&format=json

        >>> community_anchor_institutions_closest_by_latitude_and_longitude('')

        @see http://www.broadbandmap.gov/developer/api/community-anchor-institutions-closest-by-latitude-and-longitude
        """
        self.call_api('cai', 'closest', **optargs) 

    def almanac_api_parameters(self, , **optargs):
        """
        The Almanac API is designed to get all almanac parameters used
        by the Almanac API for ranking.

        Parameter list:
        **Note that the API's format param is hardcoded to be json in
        this wrapper. Specify other optional parameters by passing
        named arguments to the wrapper fxn, e.g.
        someAPICall(callback="Someoption") **

        @param callback (optional): jsonp callback function name.

        Call construction:
        http://www.broadbandmap.gov/broadbandmap/almanac/parameters?format={format}&callback={functionName}
        Sample call:
        http://www.broadbandmap.gov/broadbandmap/almanac/parameters?format=json

        >>> almanac_api_parameters('')

        @see http://www.broadbandmap.gov/developer/api/almanac-api-parameters
        """
        self.call_api('almanac', 'parameters', **optargs) 

    def speed_test_api_by_geography_type_and_geography_id(self, geographyType, geographyIds, **optargs):
        """
        This API returns the speed test results for a particular
        geography type (e.g., state, congressional district) and
        geography ID.

        Parameter list:
        **Note that the API's format param is hardcoded to be json in
        this wrapper. Specify other optional parameters by passing
        named arguments to the wrapper fxn, e.g.
        someAPICall(callback="Someoption") **

        @param geographyIds - specify the geography IDs to search for separated by commas and a maximum of 10 are allowed
        @param speedTestType (optional) - specify the speed test type among any,ookla,mlab with default being any
        @param format (optional) - valid formats are xml, json, jsonp with default being xml
        @param callback (optional) - jsonp callback function name

        Call construction:
        http://www.broadbandmap.gov/broadbandmap/speedtest/{geographyType}/ids/{geographyIds}?testtype={speedTestType}&format={format}&callback={functionName}
        Sample call:
        http://www.broadbandmap.gov/broadbandmap/speedtest/state/ids/01,02?format=json

        >>> speed_test_api_by_geography_type_and_geography_id('state', '01,02')

        @see http://www.broadbandmap.gov/developer/api/speed-test-api-by-geography-type-and-geography-id
        """
        self.call_api('speedtest', geographyType, 'ids', geographyIds, **optargs) 

    def geography_lookup_api_by_geography_type_within_a_state(self, stateFips, geographyType, **optargs):
        """
        This API returns all geographies of specific geography type
        within a state.

        Parameter list:
        **Note that the API's format param is hardcoded to be json in
        this wrapper. Specify other optional parameters by passing
        named arguments to the wrapper fxn, e.g.
        someAPICall(callback="Someoption") **

        @param geographyType - specify either one of the following geography type: county, censusplace, msa, usf,  statesenate, statehouse, congdistrict, tribalnation
        @param maxResults - specify the maximum results to be returned - defaulted to 100
        @param all - if true returns the complete set of results
        @param format (optional) - valid formats are xml, json, jsonp with default being xml
        @param callback (optional) - jsonp callback function name

        Call construction:
        http://www.broadbandmap.gov/broadbandmap/geography/state/{stateFips}/{geographyType}?maxresults={maxResults}&all={all}&format={format}&callback={functionName}
        Sample call:
        http://www.broadbandmap.gov/broadbandmap/geography/state/01/msa?format=json

        >>> geography_lookup_api_by_geography_type_within_a_state('01', 'msa')

        @see http://www.broadbandmap.gov/developer/api/geography-lookup-api-by-geography-type-within-a-state
        """
        self.call_api('geography', 'state', stateFips, geographyType, **optargs) 

    def btop_funding_api_by_state_id(self, stateIds, **optargs):
        """
        This API returns BTOP funding information by state ID.

        Parameter list:
        **Note that the API's format param is hardcoded to be json in
        this wrapper. Specify other optional parameters by passing
        named arguments to the wrapper fxn, e.g.
        someAPICall(callback="Someoption") **

        @param format (optional) - valid formats are xml, json, jsonp with default being xml
        @param callback (optional) - jsonp callback function name

        Call construction:
        http://www.broadbandmap.gov/broadbandmap/btop/stateids/{stateIds}?format={format}&callback={functionName}
        Sample call:
        http://www.broadbandmap.gov/broadbandmap/btop/stateids/01,02?format=json

        >>> btop_funding_api_by_state_id('01,02')

        @see http://www.broadbandmap.gov/developer/api/btop-funding-api-by-state-id
        """
        self.call_api('btop', 'stateids', stateIds, **optargs) 

    def census_api_by_coordinates(self, geographyType, **optargs):
        """
        This API returns the US Census Block geography ID information
        given a passed Latitude and Longitude.

        Parameter list:
        **Note that the API's format param is hardcoded to be json in
        this wrapper. Specify other optional parameters by passing
        named arguments to the wrapper fxn, e.g.
        someAPICall(callback="Someoption") **

        @param latitude - latitude of a point. Example: 41.486857
        @param longitude - longitude of a point. Example: -71.294392
        @param format (optional) - valid formats are xml, json, jsonp with default being xml
        @param callback (optional) - jsonp callback function name

        Call construction:
        http://www.broadbandmap.gov/broadbandmap/census/{geographyType}?latitude={latitude}&longitude={longitude}&format={format}&callback={functionName}
        Sample call:
        http://www.broadbandmap.gov/broadbandmap/census/block?latitude=42.456&longitude=-74.987&format=json

        >>> census_api_by_coordinates('block')

        @see http://www.broadbandmap.gov/developer/api/census-api-by-coordinates
        """
        self.call_api('census', geographyType, **optargs) 

    def census_api_by_fips_code(self, geographyType, geographyId, **optargs):
        """
        This API finds the geography of a specified geography type by
        geography id within the entire United States.

        Parameter list:
        **Note that the API's format param is hardcoded to be json in
        this wrapper. Specify other optional parameters by passing
        named arguments to the wrapper fxn, e.g.
        someAPICall(callback="Someoption") **

        @param fipsCode - FIPS code (unique identifier)
        @param format (optional) - valid formats are xml, json, jsonp with default being xml
        @param callback (optional) - jsonp callback function name

        Call construction:
        http://www.broadbandmap.gov/broadbandmap/census/{geographyType}/fips/{geographyId}?format={format}&callback={functionName}
        Sample call:
        http://www.broadbandmap.gov/broadbandmap/census/state/fips/36?format=json

        >>> census_api_by_fips_code('state', '36')

        @see http://www.broadbandmap.gov/developer/api/census-api-by-fips-code
        """
        self.call_api('census', geographyType, 'fips', geographyId, **optargs) 

    def geography_lookup_api_by_geography_type_and_geography_name(self, geographyType, geographyName, **optargs):
        """
        This API returns geographies by name of a specific geography
        type.

        Parameter list:
        **Note that the API's format param is hardcoded to be json in
        this wrapper. Specify other optional parameters by passing
        named arguments to the wrapper fxn, e.g.
        someAPICall(callback="Someoption") **

        @param geographyName - specify the geography name with at least 3 leading characters
        @param maxResults - specify the maximum results to be returned - defaulted to 100
        @param all - if true returns the complete set of results
        @param format (optional) - valid formats are xml, json, jsonp with default being xml
        @param callback (optional) - jsonp callback function name

        Call construction:
        http://www.broadbandmap.gov/broadbandmap/geography/{geographyType}/name/{geographyName}?maxresults={maxResults}&all={all}&{format={format}&callback={functionName}
        Sample call:
        http://www.broadbandmap.gov/broadbandmap/geography/censusplace/name/sei?format=json

        >>> geography_lookup_api_by_geography_type_and_geography_name('censusplace', 'sei')

        @see http://www.broadbandmap.gov/developer/api/geography-lookup-api-by-geography-type-and-geography-name
        """
        self.call_api('geography', geographyType, 'name', geographyName, **optargs) 

    def geography_lookup_api_by_geography_type(self, geographyType, **optargs):
        """
        This API allows users to find all geographies of a specified
        geography type.

        Parameter list:
        **Note that the API's format param is hardcoded to be json in
        this wrapper. Specify other optional parameters by passing
        named arguments to the wrapper fxn, e.g.
        someAPICall(callback="Someoption") **

        @param maxResults: specify the maximum results to be returned. defaulted to 100
        @param all: if true returns the complete set of results
        @param format (optional): Valid formats are xml, json, jsonp with default being xml
        @param callback (optional): jsonp callback function name.

        Call construction:
        http://www.broadbandmap.gov/broadbandmap/geography/{geographyType}?maxresults={maxResults}&all={all}&format={format}&callback={functionName}
        Sample call:
        http://www.broadbandmap.gov/broadbandmap/geography/congdistrict?format=json&maxresults=1000

        >>> geography_lookup_api_by_geography_type('congdistrict')

        @see http://www.broadbandmap.gov/developer/api/geography-lookup-api-by-geography-type
        """
        self.call_api('geography', geographyType, **optargs) 

    def demographics_api_by_geography_type_and_geography_name(self, dataVersion, geographyType, geographyNames, **optargs):
        """
        This API allows the user to search for the demographic
        information for a particular geography type and geography
        name.

        Parameter list:
        **Note that the API's format param is hardcoded to be json in
        this wrapper. Specify other optional parameters by passing
        named arguments to the wrapper fxn, e.g.
        someAPICall(callback="Someoption") **

        @param geographyType - specify either one of the following geography type: state, county, censusplace, msa, usf, statesenate, statehouse, congdistrict, tribalnation
        @param geographyNames - specify the geography names to search for separated by commas and a maximum of 10 are allowed
        @param format (optional) - valid formats are xml, json, jsonp with default being xml
        @param callback (optional) - jsonp callback function name

        Call construction:
        http://www.broadbandmap.gov/broadbandmap/demographic/{dataVersion}/{geographyType}/names/{geographyNames}?format={format}&callback={functionName}
        Sample call:
        http://www.broadbandmap.gov/broadbandmap/demographic/fall2010/county/names/jersey,jefferson?format=json

        >>> demographics_api_by_geography_type_and_geography_name('fall2010', 'county', 'jersey,jefferson')

        @see http://www.broadbandmap.gov/developer/api/demographics-api-by-geography-type-and-geography-name
        """
        self.call_api('demographic', dataVersion, geographyType, 'names', geographyNames, **optargs) 

    def demographics_api_nation(self, dataVersion, **optargs):
        """
        This API allows the user to search for the demographic
        information for the whole nation.

        Parameter list:
        **Note that the API's format param is hardcoded to be json in
        this wrapper. Specify other optional parameters by passing
        named arguments to the wrapper fxn, e.g.
        someAPICall(callback="Someoption") **

        @param format (optional) - Valid formats are xml, json, jsonp with default being xml
        @param callback (optional) - jsonp callback function name

        Call construction:
        http://www.broadbandmap.gov/broadbandmap/demographic/{dataVersion}/nation?format={format}&callback={functionName}
        Sample call:
        http://www.broadbandmap.gov/broadbandmap/demographic/fall2010/nation?format=json

        >>> demographics_api_nation('fall2010')

        @see http://www.broadbandmap.gov/developer/api/demographics-api-nation
        """
        self.call_api('demographic', dataVersion, 'nation', **optargs) 

    def btop_funding_api_by_state_name(self, stateNames, **optargs):
        """
        This API returns BTOP funding information by state name.

        Parameter list:
        **Note that the API's format param is hardcoded to be json in
        this wrapper. Specify other optional parameters by passing
        named arguments to the wrapper fxn, e.g.
        someAPICall(callback="Someoption") **

        @param format (optional) - valid formats are xml, json, jsonp with default being xml
        @param callback (optional) - jsonp callback function name

        Call construction:
        http://www.broadbandmap.gov/broadbandmap/btop/states/{stateNames}?format={format}
        Sample call:
        http://www.broadbandmap.gov/broadbandmap/btop/states/alaska,alabama?format=json

        >>> btop_funding_api_by_state_name('alaska,alabama')

        @see http://www.broadbandmap.gov/developer/api/btop-funding-api-by-state-name
        """
        self.call_api('btop', 'states', stateNames, **optargs) 

    def community_anchor_institutions_api_by_geography_type_and_geography_name(self, dataVersion, geographyType, geographyNames, **optargs):
        """
        This API allows the user to retrieve the broadband
        availability among the Community Anchor Institutions by
        geography name and type.

        Parameter list:
        **Note that the API's format param is hardcoded to be json in
        this wrapper. Specify other optional parameters by passing
        named arguments to the wrapper fxn, e.g.
        someAPICall(callback="Someoption") **

        @param geographyType - specify either one of the following geography type: state, county, censusplace, msa, usf, statesenate, statehouse, congdistrict, tribalnation
        @param geographyNames - specify the geography names to search for separated by commas and a maximum of 10 are allowed
        @param format (optional) - valid formats are xml, json, jsonp with default being xml
        @param callback (optional) - jsonp callback function name

        Call construction:
        http://www.broadbandmap.gov/broadbandmap/cai/{dataVersion}/{geographyType}/names/{geographyNames}?format={format}&callback={functionName}
        Sample call:
        http://www.broadbandmap.gov/broadbandmap/cai/fall2010/state/names/alabama,arizona?format=json

        >>> community_anchor_institutions_api_by_geography_type_and_geography_name('fall2010', 'state', 'alabama,arizona')

        @see http://www.broadbandmap.gov/developer/api/community-anchor-institutions-api-by-geography-type-and-geography-name
        """
        self.call_api('cai', dataVersion, geographyType, 'names', geographyNames, **optargs) 

    def broadband_provider_api_by_provider_name(self, providerName, **optargs):
        """
        The Broadband Provider API searches for all providers with a
        specified name.

        Parameter list:
        **Note that the API's format param is hardcoded to be json in
        this wrapper. Specify other optional parameters by passing
        named arguments to the wrapper fxn, e.g.
        someAPICall(callback="Someoption") **

        @param all: if true returns the complete set of results.
        @param maxResults: specify the maximum results to be returned. defaulted to 20.
        @param format (optional): Valid formats are xml, json, jsonp with default being xml.
        @param callback (optional): jsonp callback function name.

        Call construction:
        http://www.broadbandmap.gov/broadbandmap/provider/name/{providerName}?maxresults={maxResults}&all={all}&format={format}&callback={functionName}
        Sample call:
        http://www.broadbandmap.gov/broadbandmap/provider/name/alb?format=json

        >>> broadband_provider_api_by_provider_name('alb')

        @see http://www.broadbandmap.gov/developer/api/broadband-provider-api-by-provider-name
        """
        self.call_api('provider', 'name', providerName, **optargs) 

    def almanac_api_ranking_by_geography_id_within_a_state(self, dataVersion, stateId, censusMetric, rankingMetric, geographyType, geographyId, **optargs):
        """
        This API is designed to find the rankings by geography within
        the state for a specific metric (population or household) and
        rank (any of the metrics from provider, demographic,
        technology or speed). The results are the top ten and bottom
        ten records within the state for the particular geography type
        and my area rankings. Additionally we include +/- 5 rankings
        from the 'my' area rank.

        Parameter list:
        **Note that the API's format param is hardcoded to be json in
        this wrapper. Specify other optional parameters by passing
        named arguments to the wrapper fxn, e.g.
        someAPICall(callback="Someoption") **

        @param stateId - specify the state fips code within which the ranking should be done
        @param censusMetricType - specify the census metric by which the data has to be aggregated. It can be either population or household
        @param rankingMetric - specify one of the various metrics from demographics, technologies, speeds or providers by which the ranking will be done
        @param geographyType - specify one of the following geography type: censusplace, msa, usf, county, statesenate, statehouse, congdistrict
        @param geographyId - specify the my area geography ID to be ranked
        @param sortOrder - specify 'asc' for ascending order (default) and 'desc' for descending order
        @param properties - specify the properties comma delimited to be included in the result
        @param format (optional) - valid formats are xml, json, jsonp with default being xml
        @param callback (optional) - jsonp callback function name

        Call construction:
        http://www.broadbandmap.gov/broadbandmap/almanac/{dataVersion}/rankby/state/{stateId}/{censusMetric}/{rankingMetric}/{geographyType}/id/{geographyId}?properties={properties}&format={format}&callback={functionName}&order={sortOrder}&properties={properties}
        Sample call:
        http://www.broadbandmap.gov/broadbandmap/almanac/fall2010/rankby/state/01/population/wirelineproviderequals0/county/id/01101?format=json&order=asc

        >>> almanac_api_ranking_by_geography_id_within_a_state('fall2010', '01', 'population', 'wirelineproviderequals0', 'county', '01101')

        @see http://www.broadbandmap.gov/developer/api/almanac-api-ranking-by-geography-id-within-a-state
        """
        self.call_api('almanac', dataVersion, 'rankby', 'state', stateId, censusMetric, rankingMetric, geographyType, 'id', geographyId, **optargs) 

    def bip_funding_api_by_state_id(self, stateIds, **optargs):
        """
        This API allows the user to find the BIP funding allocated to
        states by specifying the state fips code.

        Parameter list:
        **Note that the API's format param is hardcoded to be json in
        this wrapper. Specify other optional parameters by passing
        named arguments to the wrapper fxn, e.g.
        someAPICall(callback="Someoption") **

        @param format (optional): Valid formats are xml, json, jsonp with default being xml.
        @param callback (optional): jsonp callback function name.

        Call construction:
        http://www.broadbandmap.gov/broadbandmap/bip/stateids/{stateIds}?format={format}&callback={functionName}
        Sample call:
        http://www.broadbandmap.gov/broadbandmap/bip/stateids/01,02?format=json

        >>> bip_funding_api_by_state_id('01,02')

        @see http://www.broadbandmap.gov/developer/api/bip-funding-api-by-state-id
        """
        self.call_api('bip', 'stateids', stateIds, **optargs) 

    def bip_funding_api_nation(self, , **optargs):
        """
        This API allows the user to retrieve the BIP funding
        allocation for the whole nation.

        Parameter list:
        **Note that the API's format param is hardcoded to be json in
        this wrapper. Specify other optional parameters by passing
        named arguments to the wrapper fxn, e.g.
        someAPICall(callback="Someoption") **

        @param format (optional): Valid formats are xml, json, jsonp with default being xml.
        @param callback (optional): jsonp callback function name.

        Call construction:
        http://www.broadbandmap.gov/broadbandmap/bip/nation?format={format}&callback={functionName}
        Sample call:
        http://www.broadbandmap.gov/broadbandmap/bip/nation?format=json

        >>> bip_funding_api_nation('')

        @see http://www.broadbandmap.gov/developer/api/bip-funding-api-nation
        """
        self.call_api('bip', 'nation', **optargs) 

    def speed_test_api_nation(self, , **optargs):
        """
        This API returns all the speed test results for the entire
        United States.

        Parameter list:
        **Note that the API's format param is hardcoded to be json in
        this wrapper. Specify other optional parameters by passing
        named arguments to the wrapper fxn, e.g.
        someAPICall(callback="Someoption") **

        @param format (optional): Valid formats are xml, json, jsonp with default being xml.
        @param callback (optional): jsonp callback function name.

        Call construction:
        http://www.broadbandmap.gov/broadbandmap/speedtest/nation?testtype={speedTestType}&format={format}&callback={functionName}
        Sample call:
        http://www.broadbandmap.gov/broadbandmap/speedtest/nation?format=json

        >>> speed_test_api_nation('')

        @see http://www.broadbandmap.gov/developer/api/speed-test-api-nation
        """
        self.call_api('speedtest', 'nation', **optargs) 

    def demographics_api_by_geography_type_and_geography_id(self, dataVersion, geographyType, geographyIds, **optargs):
        """
        This API allows the user to search for the demographic
        information for a particular geography type and geography ID

        Parameter list:
        **Note that the API's format param is hardcoded to be json in
        this wrapper. Specify other optional parameters by passing
        named arguments to the wrapper fxn, e.g.
        someAPICall(callback="Someoption") **

        @param geographyType - specify either one of the following geography type: state, county, censusplace, msa, usf, statesenate, statehouse, congdistrict, tribalnation
        @param geographyIds - specify the geography IDs to search for separated by commas and a maximum of 10 are allowed
        @param format (optional) - valid formats are xml, json, jsonp with default being xml
        @param callback (optional) - jsonp callback function name

        Call construction:
        http://www.broadbandmap.gov/broadbandmap/demographic/{dataVersion}/{geographyType}/ids/{geographyIds}?format={format}&callback={functionName}
        Sample call:
        http://www.broadbandmap.gov/broadbandmap/demographic/fall2010/county/ids/17081,17083?format=json

        >>> demographics_api_by_geography_type_and_geography_id('fall2010', 'county', '17081,17083')

        @see http://www.broadbandmap.gov/developer/api/demographics-api-by-geography-type-and-geography-id
        """
        self.call_api('demographic', dataVersion, geographyType, 'ids', geographyIds, **optargs) 

    def broadband_summary_api_by_geography_type_and_geography_id(self, dataVersion, censusMetricType, geographyType, geographyIds, **optargs):
        """
        This API returns broadband summary data by geography IDs for a
        specific geography type. It is designed to retrieve broadband
        summary data by geography and census metrics (population or
        households) combined as search criteria. The data includes
        wireline and wireless providers, different technologies and
        broadband speeds reported in the particular area being
        searched for on a scale of 0 to 1.

        Parameter list:
        **Note that the API's format param is hardcoded to be json in
        this wrapper. Specify other optional parameters by passing
        named arguments to the wrapper fxn, e.g.
        someAPICall(callback="Someoption") **

        @param censusMetricType - specify the census metric by which the data has to be aggregated. It can be either population or household
        @param geographyType - specify either one of the following geography type: state, censusplace, msa, county, statesenate, statehouse, congdistrict, usf, tribalnation
        @param geographyIds - specify the geography IDs to search for separated by commas and a maximum of 10 are allowed
        @param format (optional) - valid formats are xml, json, jsonp with default being xml
        @param callback (optional) - jsonp callback function name

        Call construction:
        http://www.broadbandmap.gov/broadbandmap/analyze/{dataVersion}/summary/{censusMetricType}/{geographyType}/ids/{geographyIds}?format={format}&callback={callback}
        Sample call:
        http://www.broadbandmap.gov/broadbandmap/analyze/fall2010/summary/population/state/ids/10?format=json 

        >>> broadband_summary_api_by_geography_type_and_geography_id('fall2010', 'population', 'state', '10')

        @see http://www.broadbandmap.gov/developer/api/broadband-summary-api-by-geography-type-and-geography-id
        """
        self.call_api('analyze', dataVersion, 'summary', censusMetricType, geographyType, 'ids', geographyIds, **optargs) 

    def census_api_by_geography_name(self, geographyType, geographyName, **optargs):
        """
        This API finds all the geographies specified by a geography
        name (e.g., Washington) of a specific geography type (e.g.,
        congressional district) within the entire United States.

        Parameter list:
        **Note that the API's format param is hardcoded to be json in
        this wrapper. Specify other optional parameters by passing
        named arguments to the wrapper fxn, e.g.
        someAPICall(callback="Someoption") **

        @param geographyName - specify the geography name with at least 3 leading characters
        @param maxResults - specify the maximum results to be returned - defaults to 100
        @param all - if true returns the complete set of results.
        @param format (optional) - valid formats are xml, json, jsonp with default being xml

        Call construction:
        http://www.broadbandmap.gov/broadbandmap/census/{geographyType}/{geographyName}?maxresults={maxResults}&all={all}&format={format}&callback={functionName}
        Sample call:
        http://www.broadbandmap.gov/broadbandmap/census/county/fai?format=json

        >>> census_api_by_geography_name('county', 'fai')

        @see http://www.broadbandmap.gov/developer/api/census-api-by-geography-name
        """
        self.call_api('census', geographyType, geographyName, **optargs) 

    def demographics_api_by_coordinates(self, dataVersion, **optargs):
        """
        find the demographics data from the coordinates.

        Parameter list:
        **Note that the API's format param is hardcoded to be json in
        this wrapper. Specify other optional parameters by passing
        named arguments to the wrapper fxn, e.g.
        someAPICall(callback="Someoption") **

        @param latitude: latitude of a point.
        @param longitude: longitude of a point.
        @param format (optional): Valid formats are xml, json, jsonp with default being xml.
        @param callback (optional): jsonp callback function name.

        Call construction:
        http://www.broadbandmap.gov/broadbandmap/demographic/{dataVersion}/coordinates?format={format}&callback={functionName}
        Sample call:
        http://www.broadbandmap.gov/broadbandmap/demographic/fall2010/coordinates?latitude=42.456&longitude=-74.987&format=json

        >>> demographics_api_by_coordinates('fall2010')

        @see http://www.broadbandmap.gov/developer/api/demographics-api-by-coordinates
        """
        self.call_api('demographic', dataVersion, 'coordinates', **optargs) 
