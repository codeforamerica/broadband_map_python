Python wrapper for National Broadband Map API
http://broadbandmap.gov/developer

31 Jun 2011: 
`proto` directory contains my prototyping work on going from scraped data to 
correctly formatted documentation, and perhaps eventually to functions or 
classes. 
Files in .txt are data gleaned from running scraper.py
And using bs4 (beautiful soup alpha) folder copied to dist-packages (on 
ubuntu 10.10, path is `/usr/lib/python2.6/dist-packages`)

some unknown date:
todo:
insert parameters into docstrings (high)
fix the indentation of long function example (low priority) -- meh skip (
needed in both autodoc and automethod)

28 Jul 2010:
Todo: deal with the optargs. Sample api calls look like this: SampleCall
http://www.broadbandmap.gov/broadbandmap/almanac/fall2010/rankby/state/01/population/wirelineproviderequals0/county/id/01101?format=json&order=asc
Then I need to output:
>>> ranking_by_geography_id_within_state('fall2010', '01', 'population',
...    'wirelineproviderequals0', 'county', '01101')
This will be further refined by hand to provide:
>>> api.almanac.ranking_by_geography_id_within_state('fall2010', '01', 'population',
...    'wirelineproviderequals0', 'county', '01101', order='asc')
I can work with this data: APICall 
http://www.broadbandmap.gov/broadbandmap/almanac/{dataVersion}/rankby/state/{stateId}/{censusMetric}/{rankingMetric}/{geographyType}/id/{geographyId}?properties={properties}&format={format}&callback={functionName}&order={sortOrder}&properties={properties}
So. Planned steps:
APICall.replace(http...broadbandmap), then iteratively replace with '' anything not in {}, so we get final list of test params.

Done for the night. Perhaps autogenerate "order='asc'" params for documentation as well, or perhaps do by hand.
Still need to do:
for methods_auto.py, autowrap long argument lines

8/4/11:
fix method names (sort into API classes) -- requires revamping data dictionary into a nested list (dictionaries are unordered)
write autotest.py and generate testing

document and cont. integration

fix manually errors like:
    def btop_funding_api_nation(self, , **optargs):

ignore non-wrapped documentation lines (drop the issue).
