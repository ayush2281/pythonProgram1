import json
file=open("example_2.json","r")
x=file.read()
finaldata=json.loads(x)
# print(finaldata)

for a in finaldata:
    print(a['q1'])