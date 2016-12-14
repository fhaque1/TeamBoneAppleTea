import csv
reader = csv.DictReader(open('2011_us_ag_exports.csv'))

for row in reader:
    with open('test', 'w') as file_:
        file_.write(str(row))
    SystemExit(0)
