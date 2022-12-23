import pandas as pd
import csv
import os
import re

# Convert csv to a dataframe.

df = pd.read_csv('interview_scent.csv')

# Get a series of booleans that has True when scent_prediction is not None. Count this.

cnt = 0
for i in df.scent_prediction != 'None':
    if i == True:
        cnt = cnt + 1

# Find all the unique scents. This also includes scents with multiple notes.
#Adding all this to a set so duplicates are removed and counting the set length.

scents = df.scent_prediction.unique()
scents = scents[1:]
for i in enumerate(scents):
    scents[i[0]] = i[1].split(',')
d = set()
for i in scents:
    for j in i:
        o = j.strip()
        d.add(o)

# Creating a dictionary with scents as keys. Created a list with all scents presen and mapped them to the dictionary with values as count.

dict = {}
temp = list(df.scent_prediction)
res = list(filter('None'.__ne__, temp))
for i in enumerate(res):
    res[i[0]] = i[1].split(',')
temp = []
for i in res:
    for j in i:
        o = j.strip()
        temp.append(o)
for i in temp:
    if i in dict.keys():
        dict[i] = dict[i] + 1
    else:
        dict[i] = 1

# Created a csv with the generated dictionary.

fields = ['scent_value', 'count']
filename = os.getcwd() + '\\scent_distrib.csv'
with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    for i in dict.keys():
        row = [i, dict[i]]
        csvwriter.writerow(row)

# Used a regex pattern to find out weight in string formed by concatenating title, short_description and long_description.
# \d*\.?\d+ is used to find any integer or float value, \s* signifies the prescence of zero or more whitespaces and this
#is followed by a set of weight units to be searched for.

title = list(df.title)
sh = list(df.short_description)
lo = list(df.long_description)
l = []
for i in range(len(title)):
    l.append([title[i], sh[i], lo[i]])
quan = []
for i in l:
    st = ' '.join(str(v) for v in i)
    pattern = re.compile(r'\d*\.?\d+\s*(?:ounce|fl oz|oz|ounces|Oz)\b',
                         re.I)
    res = pattern.findall(st)
    if len(res) == 0:
        quan.append('None')
    else:
        quan.append(res[0])
df['quantity_prediction'] = quan
df.to_csv('new.csv', index=False, header=True)

# providing required output

print ('Find the total number of rows in the csv file, ignoring the rows where `prediction`is "None": '
       , cnt)
print ('Find the distinct values in the `scent_prediction` column of csv.: '
       , d)
print ('Find the count of each distinct value appearing in the `scent_prediction` column of csv.: '
       , dict)
print ('Create a new csv file with columns scent_value,count and write the values from the above question to the new file.: Created.')
print ('Create regex:', df)
print ('new.csv created with quantity_prediction column populated')
