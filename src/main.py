import pandas as pd
import json
import math

source_val = 'KPI Dashboard'

df = pd.read_excel('./Financial_report.xlsx',sheet_name=source_val)

source_object = {
    'source': source_val,
    'categories': []
}

under_category = False
cur_category = None
category_set = set()
for i in range(df.shape[0]): #categories will always be in column B ('Unnamed: 1')
    check_counter=0
    for j in range(2,df.iloc[i].shape[0]):
        check_counter+=1
        if type(df.iloc[i,j])!=pd._libs.tslibs.timestamps.Timestamp:
            if (type(df.iloc[i,1])==str) and under_category: #and (not math.isnan(df.iloc[i,1]))
                source_object['categories'][-1]['fields'].append(df.iloc[i,1])
            break
    if check_counter==df.iloc[i].shape[0]-2:
        under_category = True
        cur_category = df.iloc[i,1]

        if cur_category not in category_set:
            category_set.add(cur_category)
            dates = df.iloc[i,2:]
            dates = sorted(dates)
            # TODO check date row format?
            source_object['categories'].append(
                {
                    'name': df.iloc[i,1],
                    'fields': [],
                    'subsets': ["all"],
                    'start_date': dates[0].strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3]+"+00:00",
                    'end_date': dates[-1].strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3]+"+00:00"
                }
            )
        if type(df.iloc[i,0])==str:
            subset = df.iloc[i,0]
            for i in range(len(source_object['categories'])):
                if source_object['categories'][i]['name']==cur_category:
                    source_object['categories'][i]['subsets'].append(subset)
                    break


with open("my_soln.json","w") as f:
    json.dump(source_object,f,indent=4)











# json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}], indent=4)

        # TODO check date row format?
        # if dates[0]!=df.iloc[i,2] or dates[-1]==df.iloc[i,-1]:
        #     raise RuntimeError("Row {} (of Dates) either doesn't start with Min date or end with Max date or both".format(i))