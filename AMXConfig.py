import pandas, json

# Load CSV into data frame
df = pandas.read_csv('ncmd_units_export.csv')

# Remove unnecessary data from the set and then sort the 
# set by name and IP (descending order for 'NAME' and ascending order for 'IP')
dfPared = df[['NAME','TYPE','MAC','IP']]
dfSort = dfPared.sort_values(['TYPE','IP'], ascending=(0,1))

# Export pared and sorted data to JSON format
dfJSON = dfSort.to_json(orient='records', indent=4)

print(dfJSON)