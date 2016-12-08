'''
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2011_us_ag_exports.csv')

for col in df.columns:
    df[col] = df[col].astype(str)
  '''  
    #replace using csv reader
    
import csv
with open ('2011_us_ag_exports.csv', 'r+') as csvfile:
	fieldnames = ['code','state','category','total exports','beef','pork','poultry','dairy,fruits fresh','fruits proc','total fruits','veggies fresh','veggies proc','total veggies','corn','wheat','cotton']
	#reader
	reader = csv.DictReader(csvfile)
	#with open ('2011_us_ag_exports.csv', 'w') as csvfile:
	writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
	writer.writeheader()
	for row in reader:
		writer.writerow({'code': row['code']})
		print row['code']
		

