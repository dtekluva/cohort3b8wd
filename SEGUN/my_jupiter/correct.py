import pandas as pd
cases="https://data.humdata.org/hxlproxy/api/data-preview.csv?url=https%3A%2F%2Fraw.githubusercontent.com%2FCSSEGISandData%2FCOVID-19%2Fmaster%2Fcsse_covid_19_data%2Fcsse_covid_19_time_series%2Ftime_series_covid19_confirmed_global.csv&filename=time_series_covid19_confirmed_global.csv"
death="https://data.humdata.org/hxlproxy/api/data-preview.csv?url=https%3A%2F%2Fraw.githubusercontent.com%2FCSSEGISandData%2FCOVID-19%2Fmaster%2Fcsse_covid_19_data%2Fcsse_covid_19_time_series%2Ftime_series_covid19_deaths_global.csv&filename=time_series_covid19_deaths_global.csv"
recoveries="https://data.humdata.org/hxlproxy/api/data-preview.csv?url=https%3A%2F%2Fraw.githubusercontent.com%2FCSSEGISandData%2FCOVID-19%2Fmaster%2Fcsse_covid_19_data%2Fcsse_covid_19_time_series%2Ftime_series_covid19_recovered_global.csv&filename=time_series_covid19_recovered_global.csv"

data_cases=pd.read_csv(cases)
data_death=pd.read_csv(death)
data_recoveries=pd.read_csv(recoveries)
print(data_cases)
data_cases.drop(['Province/State', 'Lat', 'Long'], axis = 1, inplace=True)
print(data_cases)
melted_data_cases = data_cases.melt(id_vars=['Country/Region'], value_name='cases', var_name='dates') 
#melting 
print(melted_data_cases)
melted_data_cases[melted_data_cases["Country/Region"] == "Afghanistan"]
data_death.drop(['Province/State', 'Lat', 'Long'], axis = 1, inplace=True) #melting the data_death
melted_data_death = data_death.melt(id_vars=['Country/Region'], value_name='deaths', var_name='dates')
melted_data_cases["deaths"]=melted_data_death.deaths