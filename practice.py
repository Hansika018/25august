import pandas as pd
data = {
    'Age':[27,28,29,'None',30,31,32,'None',33,34],
    'Height':[162,164,165,'None',167,170,'None',172,1740,175],
    'Wt':[54,56,'None',65,67,68,'None',69,70,72],
    'marks':[78,79,80,'None',82,84,85,'None',87,88],
    'city':['mtr','raya','jait','sonai','khura','goverdhan','agra','aligarh','hathras','barsana']
}
df=pd.DataFrame(data)
print(df);