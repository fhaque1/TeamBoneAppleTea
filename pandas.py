import csv
reader = csv.DictReader(open('2011_us_ag_exports.csv'))

result = {}
for row in reader:
    for column, value in row.iteritems():
        result.setdefault(column, []).append(value)
print result
