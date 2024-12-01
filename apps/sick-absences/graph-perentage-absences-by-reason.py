import pandas as pd
import plotly.express as px


file_path = './data-set/sick-absences/percentage-of-occureences-of-sick-absences-by-reason.csv'

data = pd.read_csv(file_path, skiprows=5)
data = data.dropna(axis=1, how='all') 
data = data.drop(columns=[col for col in data.columns if 'Unnamed' in col])  
data.columns = ['Reason given for sickness', '2022', '2021', '2020', '2019', '2018', '2017', '2016', '2015', '2014', '2013', '2012', '2011', '2010', '2009']
data = data[~data['Reason given for sickness'].str.contains("Total|note", na=False)]


data = data.replace('[w]', None)
data.iloc[:, 1:] = data.iloc[:, 1:].apply(pd.to_numeric, errors='coerce')
data.set_index('Reason given for sickness', inplace=True)
data = data.T
data_long = data.reset_index().melt(id_vars=['index'], var_name='Reason', value_name='Percentage')
data_long.rename(columns={'index': 'Year'}, inplace=True)
data_long['Year'] = pd.to_numeric(data_long['Year'], errors='coerce')


data_long = data_long.sort_values('Year')


print(data_long.head())


fig = px.line(data_long, x='Year', y='Percentage', color='Reason',
              title='Sickness Absence by Reason (2009 - 2022)',
              labels={'Year': 'Year', 'Percentage': 'Percentage of Occurrences'})


fig.update_layout(
    xaxis_title='Year',
    yaxis_title='Percentage of Occurrences',
    legend_title='Reason for Sickness',
    hovermode='x unified',  
    template='plotly_dark' 
)


fig.show()


