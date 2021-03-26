import pandas as pd
import gc
import re

# totalEngJson = pd.read_json('TOTAL.json')
# Can't read file as a json and must be parsed as a text
# Columns to create must include:
# series_id, name, units, f, start, end, last_updated, data
# Data is a list object with list objects containing 2 values
# Year/Date, unit amount
# Two types of json objects: Annual and monthly
# This is for the same recorded energy name
# Create a new csv of both total dataframes

# Two dataframes
# series_id, name, units, f, start, end, last_updated, date, amount
# {"series_id":"([\w\.]+)","name":"([\w \,]+)","units":"([\w \,]+)","f":"(\w+)","start":".+","data":(?:(\[("\d+",[\d\.]+)\])(?:,|))}
totAnnual = pd.DataFrame(columns =['series_id', 'name', 'units',
                                   'f',
                                   'date', 'amount'])
totMonthly = pd.DataFrame(columns =['series_id', 'name', 'units',
                                   'f',
                                   'date', 'amount'])
energyRegex = r'{"series_id":"([\w\.\-]+)","name":"([\w \,\:\(\)-]+)","units":"([\w \,]+)","f":"(\w+)","description":".+","iso3166":"([\w\-]+)","geography":".+","'
dataRegex = r'(?:\["([\w\d]+)",((?:[\d\.]+)|(?:\w+))\](?:,|))'
with open('../data/raw/SEDS.json','r') as file:
	line = file.readline()
	while line:
		match = re.findall(energyRegex,line)
		data =  re.findall(dataRegex,line)
		try:
			if match[0][3] == 'A':
				for d in data:
					totAnnual.loc[len(totAnnual.index)] = ([match[0][0],
						match[0][1],match[0][2],match[0][3],d[0],d[1]])
			else:
				for d in data:
					totMonthly.loc[len(totMonthly.index)] =([match[0][0],
						match[0][1],match[0][2],match[0][3],d[0],d[1]])
		except:
			None
		line = file.readline()

totMonthly.to_csv('../data/processed/SEDSM.csv',index = False)
totAnnual.to_csv('../data/processed/SEDSA.csv',index = False)
del totAnnual
del totMonthly
gc.collect()