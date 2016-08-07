from pyexcel_ods import get_data
data=get_data("/home/anant/Desktop/foss/pyth.ods")
import json
k=json.dumps(data)
sum=int(k[13])+int(k[16])
print sum

