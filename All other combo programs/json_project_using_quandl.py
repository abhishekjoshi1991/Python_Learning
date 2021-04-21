# JSON project:

'''
accessing data from quandl website and print yearwise average of closed price for
any company's json data. Use Indian Equities Adjusted End of Day Prices.

here we will create one blank dictionary, then inside that dict we will
start appending year as keys, for each key we will create blank list as value, inside
that values we will fill closed price data.

e.g
a=dict()
l1=[2010,2010,2010,2011,2011] ,year can be fetched from data[0]
for data in l1:
    if data not in a:
        a[data]=list()

a = {2010: [], 2011: []}, such structure we required.

'''

import json, requests, datetime

url=input('enter the json url for which data is required: ')
r = requests.get(url)
print(r) #to print response code
loaded_data = r.text
master_data = json.loads(loaded_data)
dict_of_years = dict()

'''
now this json has structure inside ['dataset']['data'] as,

'Date', 'Open Price', 'High Price', 'Low Price', 'Last Traded Price', 'Close Price', 'Total Traded Quantity', 'Turnover (in Lakhs)'
'2010-12-31', 389.91, 391.95, 386.75, 390.15, 391.02, 6449104.72, 25143.4 .....etc

in list format, from this we need only data i.e index 0 and close price at index 5.
'''

for data in master_data['dataset']['data']:
    year = datetime.datetime.strptime(data[0], "%Y-%m-%d").year
    if year not in dict_of_years: #if year key not present in dict
        dict_of_years[year] = list() #create blank list ahead of year in dict like {2000:[]}
        dict_of_years[year].append(data[5])
    else: #if key present in dict, means list structure already there, just append
        dict_of_years[year].append(data[5])

print(dict_of_years)

for year, price in sorted(dict_of_years.items(), key= lambda x:x[0]):
    print(year, sum(price)/len(price))




