#! /usr/bin/env python

 #'bip_funding_api_by_state_id'
 #'bip_funding_api_by_state_name'

#So, create classes. 
#Need to map from doc URL to sample call URL.
#docURL --
#apicallURL --
#For each docURL, generate classandfxnName, 
#1. then process to create dict, { 'almanac':('by state', 'by state name')}
#2. Generate code (classes and methods)
#3. Generate documentation. 

#Probably easier, though, and faster, to just insert the classes by hand. Yea. So create class GeneralAPI(), autogenerate fxns (with correct API.Almanac.bySTate('tx') format, not the temporary API.almanacAPI_byState('tx') format). Yea. Because would have to reformat ScrapedDocsDict to be nested, which could be ugly. Instead just have simple for each loop.


#====Data.py contents...===
#doclinks = [

#Structure:
#key: documentation URL
#item: list, 1. documentation text 2. API call format 3. Sample API call 4..n. Parameters and parameter descriptions
#docdata = {'

    #def ranking_by_geography_id_within_state(self, dataVersion, stateId, 
            #censusMetricType, rankingMetric, geographyType, geographyId, **kwarg):
expect = "'broadbandmap', 'almanac', dataVersion, 'rankby', 'state', stateId, censusMetricType, rankingMetric, geographyType, 'id', geographyId"
#print expect
name = "ranking_by_geography_id_within_state"
params = ['dataVersion', 'stateId', 'censusMetric', 'rankingMetric', 'geographyType', 'geographyId']
name = "ranking_by_geography_id_within_state"
urlparams = ['broadbandmap', 'almanac', '{dataVersion}', 'rankby', 'state', '{stateId}', '{censusMetric}', '{rankingMetric}', '{geographyType}', 'id', '{geographyId}']


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

    #with open('api.py', 'w') as f:
        #f.write(str(docs))

createfxn(name, params, urlparams)

'''
current output:
def ranking_by_geography_id_within_state(self, dataVersion,
stateId, censusMetric, rankingMetric, geographyType, geographyId, **optargs):
           self.call_api('broadbandmap', 'almanac', dataVersion, 'rankby',
                   'state', stateId, censusMetric, rankingMetric, geographyType,
                   'id', geographyId, **optargs):
'''
