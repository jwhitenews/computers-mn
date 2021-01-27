
import pandas as pd

URL = "file:///C:/Users/n680592x/OneDrive/Desktop/taxes2020/hdc.html"



tables = pd.read_html(URL)

#print ("There are : ",len(tables)," tables")
#print(tables[0])

data = pd.DataFrame(tables[0])

data = data['Chrgs'].sum()


print(data)