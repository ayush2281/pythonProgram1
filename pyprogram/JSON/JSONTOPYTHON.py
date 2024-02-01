# Python JSON
# if you have a json string, you can  parse it by using the json.loads()method.

import json
d='{"cname":"Python","fees":12000,"duration":"45Days"}' #json format
x=json.loads(d)
print(type(x))
print(x)
for a in x:
    print(a,x[a])