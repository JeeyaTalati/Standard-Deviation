import csv
import math
import statistics
with open("Class3.csv",newline="") as f:
    reader=csv.reader(f)
    fileData=list(reader)
data=fileData[0]
value=len(data)
sum=0

for x in data:
    sum=sum+int(x)
mean=sum/value
print(mean)
dif=0
total=0
for y in data:
    dif=int(y)-mean
    dif=dif**2
    total=total+dif
    dif=0
deviation=math.sqrt(total/value)
print(deviation)


