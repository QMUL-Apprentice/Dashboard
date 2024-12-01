import pandas as pd
import plotly.graph_objects as go


file_path = './data-set/sick-absences/sick-absences-rate-by-sex.csv'  
data = pd.read_csv(file_path, skiprows=3)  


data.columns = data.columns.str.replace('\n', ' ').str.strip()
data = data.dropna(axis=1, how='all')  
data = data.dropna(axis=0, how='all')  
data = data.replace(',,', None)  
data.dropna(inplace=True)  


data['Year'] = data['Year'].astype(str).str.extract('(\d+)').astype(int)


men_col = [col for col in data.columns if 'men' in col.lower()][0]
women_col = [col for col in data.columns if 'women' in col.lower()][0]


fig = go.Figure()


fig.add_trace(go.Scatter(
    x=data['Year'],
    y=data[men_col],
    mode='lines+markers',
    name='Men',
    line=dict(color='blue')
))


fig.add_trace(go.Scatter(
    x=data['Year'],
    y=data[women_col],
    mode='lines+markers',
    name='Women',
    line=dict(color='orange')
))

fig.update_layout(
    title='Sickness Absence Rate by Year',
    xaxis_title='Year',
    yaxis_title='Sickness Absence Rate (%)',
    template='plotly_dark', 
    showlegend=True,
    legend=dict(
        x=0,
        y=1,
        traceorder='normal',
        bgcolor='rgba(0,0,0,0)',
        bordercolor='rgba(255,255,255,0.5)'
    )
)

# Show the combined plot
fig.show()
