#Test for the duplicate country solution
#theory: make if inside of the if statement below checking for duplicates in list_of_countries list, if true it will do the fig but instead use the column with specific row
#e.x. if input "Australia" then the user will be prompt to type in a region such as "Australian Capital Territory" so it will show only one line there (avoid the "ValueError: Wrong number of items passed 8, placement implies 1")


import pandas as pd
import plotly
import plotly.express as px


df = pd.read_csv('https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv') # change link from my copy to orginal
df = pd.DataFrame(df)

df =df.drop(columns=['Lat','Long'])   #Country/Region row is still here
df=df.rename(columns={'Country/Region':'Time'})
df = df.set_index('Time').transpose()
list_of_countries = list(df.columns)
name = input("Enter a country! ")     #Problem with countries that are separated into multiple rows based on region e.x. Canada has multiple rows in resp.
name = name.capitalize()
if name == "Us":
  name = "US"

if name in list_of_countries:
  fig = px.line(df, x=df.index, y= name, title="Number of Confirmed Cases in " + name,)
  fig.update_xaxes(title="Time")
  fig.update_yaxes(title="Number of Confirmed Cases")
  fig.show()
else:
	print("No data :( Please input a different country.")
