#Improve by specifiying the Province/State with duplicate countries such as "Australia"
#Theory: if statement so if the Province/State column is not empty/NaN then it will add the Province/State in () next to it
#Improve by accepting other names for coutry e.x. America, USA, United States, United States of America = US

import pandas as pd
import plotly
import plotly.express as px
import plotly.graph_objs as go


df = pd.read_csv('https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv') # changed link from my copy to orginal data set
df = pd.DataFrame(df)


df =df.drop(columns=['Province/State', 'Lat','Long'])
df=df.rename(columns={'Country/Region':'Time'})
df = df.set_index('Time').transpose()
list_of_countries = list(df.columns)

fig = go.Figure()
for col in df.columns:
    fig.add_trace(go.Scatter(x=df.index, y=df[col],  mode='lines', name = col))
fig.update_layout(title = "Number of Confirmed Cases in Each Country")
fig.show()