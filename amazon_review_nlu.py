import xlrd
import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
import watson_developer_cloud.natural_language_understanding.features.v1 as \
    features
	
workbook=xlrd.open_workbook("test_data.xls")
worksheet=workbook.sheet_by_index(0)
total_rows=worksheet.nrows
table=list()
output=list()
print(total_rows)
for x in range(total_rows):
		table.append(worksheet.cell(x,6).value)
		
##for i in range(123,len(table)):

natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2017-02-27',
    username="d145642f-5637-4fb5-938a-5f3290ddf947",
    password='TTZO6Fv0oKQz')
response = ""
s=""
count=0
print("Watson review  products ..hahaha\n")
for i in range(0,len(table)-3):   
	 response = natural_language_understanding.analyze(text=table[i],features=[features.Sentiment()])
	 s=json.dumps(response)
	 data=json.loads(s)
	 print(table[i])
	 print('\n')
	 print(data)
	 if(data['sentiment']['document']['score'])>0.50:
             count=count+1
         print(i,count)
         print('\n')
	 
print(count)
