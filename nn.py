from pyexcel_ods import get_data
k=get_data("/home/anant/Desktop/Untitled 1.ods")
import json
k=json.dumps(k)
c=0
print k
for i in k:
	if i=='['
	c+=1
	if c==2:
		
