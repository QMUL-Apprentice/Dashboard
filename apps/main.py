import dash
from dash import dcc, html
import plotly.graph_objs as go
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from clean_health_data import load_and_clean_data


def clean_pm25_data(data):
    df = pd.read_csv(data)
    df['PM2.5 Particulate (ug/m3)'] = pd.to_numeric(df['PM2.5 Particulate (ug/m3)'], errors='coerce')
    df_cleaned = df.dropna(subset=['PM2.5 Particulate (ug/m3)'])
    df_cleaned = df_cleaned.reset_index(drop=True)
    return df_cleaned






def load_and_clean_sickness_reason_data(file_path):
    data = pd.read_csv(file_path, skiprows=5)
    data = data.dropna(axis=1, how='all')
    data = data.drop(columns=[col for col in data.columns if 'Unnamed' in col])
    data.columns = ['Reason given for sickness', '2022', '2021', '2020', '2019', '2018', '2017', '2016', '2015', '2014', '2013', '2012', '2011', '2010', '2009']
    data = data[~data['Reason given for sickness'].str.contains("Total|note", na=False)]
    data = data[~data['Reason given for sickness'].isin(['Eye/ear/nose/mouth/dental problems', 'Prefers not to give details'])]
    data = data.replace('[w]', None)
    data.iloc[:, 1:] = data.iloc[:, 1:].apply(pd.to_numeric, errors='coerce')
    data.set_index('Reason given for sickness', inplace=True)
    data = data.T
    data_long = data.reset_index().melt(id_vars=['index'], var_name='Reason', value_name='Percentage')
    data_long.rename(columns={'index': 'Year'}, inplace=True)
    data_long['Year'] = pd.to_numeric(data_long['Year'], errors='coerce')
    data_long = data_long.sort_values('Year')
    return data_long


file_path = './data-set/sick-absences/percentage-of-occureences-of-sick-absences-by-reason.csv'
data_long = load_and_clean_sickness_reason_data(file_path)





men_file_path = './data-set/sick-absences/Number-of-days-lost-through-sick-absences.csv'
women_file_path = './data-set/sick-absences/Women-number-of-days-lost-through-sick-absences.csv'
def load_and_clean_sick_data():
   
    men_data = pd.read_csv(men_file_path, skiprows=3)
    women_data = pd.read_csv(women_file_path)

    men_data = men_data.dropna(axis=1, how='all').dropna(axis=0, how='all')
    women_data = women_data.dropna(axis=1, how='all').dropna(axis=0, how='all')

    
    new_data_men = men_data.loc[men_data['Geographic area (Men)'] == 'London']
    new_data_women = women_data.loc[women_data['Geographic area (Women)'] == 'London']

 
    row_data_men = new_data_men.iloc[0, 1:]
    row_data_women = new_data_women.iloc[0, 1:]

 
    row_data_men.index = row_data_men.index.str.extract(r'(\d{4})')[0]
    row_data_women.index = row_data_women.index.str.extract(r'(\d{4})')[0]

    
    common_years = sorted(set(row_data_men.index).intersection(set(row_data_women.index)))
    row_data_men = row_data_men.loc[common_years].astype(float)
    row_data_women = row_data_women.loc[common_years].astype(float)

    return row_data_men, row_data_women, common_years


row_data_men, row_data_women, common_years = load_and_clean_sick_data()
file_path = './data-set/phof-indicators-data-london/monthlyrespiratorydeathsinlondon20012015.csv'
health_data = load_and_clean_data(file_path)

app = dash.Dash(__name__)





pieChartCategories = ['Motor road transport',  'Other']
barChartCategories = ['10<', '10-18', '18-25', '25-40', '40-60', '60+']

values1 = [190, 103]
values2 = [32, 42, 20, 18, 22, 45]

x_scatter = np.random.rand(100) * 10 
y_scatter = 2 * x_scatter + np.random.randn(100) * 2 


m, c = np.polyfit(x_scatter, y_scatter, 1)  
y_regression = m * x_scatter + c 





air_cleaned_data = clean_pm25_data('./data-set/air-quality-london.xlsx - Monthly averages.csv')
air_cleaned_data['Month'] = pd.to_datetime(air_cleaned_data['Month'], format='%b-%Y')
air_cleaned_data['Year'] = air_cleaned_data['Month'].dt.year


air_cleaned_data = air_cleaned_data[air_cleaned_data['Year'] != 2019]

numeric_data = air_cleaned_data.select_dtypes(include=['number'])

yearly_data = numeric_data.groupby('Year').sum()

x = yearly_data.index  
y1 = yearly_data['PM2.5 Particulate (ug/m3)']  

x_ticks = x[::2]  


fig1 = go.Figure(go.Scatter(x=x, y=y1, mode='lines'))


fig1.update_layout(
    title='Particulate Matter (PM2.5) (London)',
    template='plotly_dark',
    plot_bgcolor='rgba(0, 0, 0, 0)',  
    paper_bgcolor='rgba(0, 0, 0, 0)',
    font=dict(color='white'),
    xaxis=dict(
        title='Year', 
        showgrid=False, 
        zeroline=True, 
        showline=True, 
        linewidth=1, 
        linecolor='white',
        tickmode='array',  
        tickvals=x_ticks, 
        tickangle=45, 
    ),
    yaxis=dict(
        title='PM 2.5 (µg/m³)', 
        showgrid=False, 
        zeroline=True, 
        showline=True, 
        linewidth=1, 
        linecolor='white',
        range=[y1.min() - 10, y1.max() + 300]  
    ),
    title_x=0.5
)
fig2 = go.Figure(go.Scatter(
    x=health_data['Year Of Occurrence'],
    y=health_data['Total'],
    mode='lines+markers',
    name='Respiratory Disease Cases'
))

y_max = health_data['Total'].max() * 1.1  

fig2.update_layout(
    title='Respiratory Disease Cases in (London)',
    template='plotly_dark',
    plot_bgcolor='rgba(0, 0, 0, 0)',
    paper_bgcolor='rgba(0, 0, 0, 0)',
    font=dict(color='white'),
    xaxis=dict(title='Year', showgrid=False, zeroline=True, showline=True, linewidth=1, linecolor='white'),
    yaxis=dict(
        title='Number of Cases',
        range=[0, y_max], 
        showgrid=False,
        zeroline=True,
        showline=True,
        linewidth=1,
        linecolor='white'
    ),
    title_x=0.5
)


fig3 = go.Figure()
fig3.add_trace(go.Scatter(x=common_years, y=row_data_men, mode='lines', name='Men'))


fig3.add_trace(go.Scatter(x=common_years, y=row_data_women, mode='lines', name='Women'))


fig3.update_layout(
    title='Work Absenteeism By Sex (London)',
    template='plotly_dark',
    plot_bgcolor='rgba(0, 0, 0, 0)',
    paper_bgcolor='rgba(0, 0, 0, 0)',
    font=dict(color='white'),
    xaxis=dict(title='Year', showgrid=False, zeroline=True, showline=True, linewidth=1, linecolor='white'),
    yaxis=dict(title='Number of absences', showgrid=False, zeroline=True, showline=True, linewidth=1, linecolor='white'),
    title_x=0.5
)





fig4 = go.Figure()


for reason in data_long['Reason'].unique():
  
    filtered_data = data_long[data_long['Reason'] == reason]
    
    fig4.add_trace(go.Scatter(x=filtered_data['Year'], y=filtered_data['Percentage'],
                             mode='lines', name=reason, line=dict(width=2))) 


fig4.update_layout(
    title='Absenteeism by Reason (2009 - 2022)',
    template='plotly_dark',
    plot_bgcolor='rgba(0, 0, 0, 0)',
    paper_bgcolor='rgba(0, 0, 0, 0)',
    font=dict(color='white'),
    xaxis=dict(title='Year', showgrid=False, zeroline=True, showline=True, linewidth=1, linecolor='white'),
    yaxis=dict(title='Percentage of Occurrences', showgrid=False, zeroline=True, showline=True, linewidth=1, linecolor='white'),
    title_x=0.7,
    title_y=0.9,

    width=550,  
    height=400, 
    margin=dict(l=80, r=200, t=80, b=70),  # Increase margins around the plot
   
    legend=dict(x=1, y=1, traceorder='normal', orientation='v', font=dict(size=10), bgcolor='rgba(0, 0, 0, 0)'),
)


fig5 = go.Figure(go.Pie(labels=pieChartCategories, values=values1, name='Pie Chart 1'))
fig5.update_layout(
    title='Air Pollution Source',
    template='plotly_dark',
    plot_bgcolor='rgba(0, 0, 0, 0)',
    paper_bgcolor='rgba(0, 0, 0, 0)',
    font=dict(color='white'),
    title_x=0.5
)

fig6 = go.Figure(go.Bar(x=barChartCategories, y=values2, name='Bar Graph 2'))
fig6.update_layout(
    title='Respiratory Diseases Cases By Age',
    template='plotly_dark',
    plot_bgcolor='rgba(0, 0, 0, 0)',
    paper_bgcolor='rgba(0, 0, 0, 0)',
    font=dict(color='white'),
    title_x=0.5
)

xinv = np.linspace(0, 10, 100)
xcal = np.linspace(0, 10, 100)
yinv = np.exp(-xcal)



def reciprocal(x, A, B):
    return A / (x + B)

# Generate the x values for the number of e-bikes (range 0 to 10, you can adjust as needed)
xinv = np.linspace(1, 10, 100)  # Avoid division by zero by starting at x=1
A = 100  # Set a value for A (vertical stretch)
B = 1    # Set a value for B (horizontal shift)

# Calculate y values based on the reciprocal function
yinv = reciprocal(xinv, A, B)

# Create the figure for the plot
fig_inv = go.Figure(go.Scatter(x=xinv, y=yinv, mode='lines', name='Reciprocal Decay'))

# Update layout for aesthetics and titles
fig_inv.update_layout(
    title='Scenario: Number of e-bikes/e-scooters increase',
    template='plotly_dark',
    plot_bgcolor='rgba(0, 0, 0, 0)',
    paper_bgcolor='rgba(0, 0, 0, 0)', 
    font=dict(color='white'),
    xaxis=dict(title='Number of e-Bikes', showgrid=False, zeroline=True, showline=True, linewidth=1, linecolor='white'),
    yaxis=dict(title='AQI', showgrid=False, zeroline=True, showline=True, linewidth=1, linecolor='white'),
    title_x=0.5
)


fig_inv2 = go.Figure(go.Scatter(x=xinv, y=yinv, mode='lines', name='Inverse Exponential'))
fig_inv2.update_layout(
    title='Scenario: Number of e-bikes/<br>e-scooters increase',
    template='plotly_dark',
    plot_bgcolor='rgba(0, 0, 0, 0)',
    paper_bgcolor='rgba(0, 0, 0, 0)',
    font=dict(color='white'),
    xaxis=dict(title='Number of e-Bikes', showgrid=False, zeroline=True, showline=True, linewidth=1, linecolor='white'),
    yaxis=dict(title='Work absenteeism logarithmic', showgrid=False, zeroline=True, showline=True, linewidth=1, linecolor='white'),
    title_x=0.5, 
    margin=dict(l=80, r=80, t=120, b=70)
)




gauge_fig2 = go.Figure(go.Indicator(
    mode="gauge+number+delta",
    value=0.7,
    title={"text": "correlation coefficient AQI vs Health Cases"},
    gauge={
        "axis": {"range": [0, 1]},
        "bar": {"color": "green"},
        "steps": [
            {"range": [0, 0.3], "color": "red"},
            {"range": [0.3, 0.6], "color": "yellow"},
            {"range": [0.6, 1], "color": "green"}
        ],
    },
    number={"font": {"size": 40}},
))
gauge_fig2.update_layout(
    template="plotly_dark",
    plot_bgcolor='rgba(0, 0, 0, 0)',
    paper_bgcolor='rgba(0, 0, 0, 0)',
    font=dict(color='white'),
    title_x=0.5
)

np.random.seed(42)
london_lat = 51.5074  
london_lon = -0.1278 


num_hotspots = 20
latitudes = london_lat + np.random.uniform(-0.05, 0.05, num_hotspots)
longitudes = london_lon + np.random.uniform(-0.05, 0.05, num_hotspots)


air_quality_values = np.random.uniform(0, 100, num_hotspots)


figlond = go.Figure(go.Scattermapbox(
    lat=latitudes,
    lon=longitudes,
    mode='markers',
    marker=dict(
        size=12,
        color=air_quality_values,
        colorscale='Viridis',  
        showscale=True, 
        colorbar=dict(title="Air Quality Index (AQI)"),
    ),
    text=[f"Air Quality: {value:.2f}" for value in air_quality_values],  
))

figlond.update_layout(
    title="London Air Quality Hotspots",
    mapbox=dict(
        style="carto-positron", 
        center=dict(lat=london_lat, lon=london_lon),
        zoom=10,
    ),
    template="plotly_dark",
    plot_bgcolor='rgba(0, 0, 0, 0)', 
    paper_bgcolor='rgba(0, 0, 0, 0)',  
    font=dict(color='white'),
    title_x=0.5
)





fig7 = go.Figure()
fig7.add_trace(go.Scatter(x=x_scatter, y=y_scatter, mode='markers', name='Data Points'))


fig7.add_trace(go.Scatter(x=x_scatter, y=y_regression, mode='lines', name='Regression Line', line=dict(color='red')))

fig7.update_layout(
    title='AQI vs Respiratory Health Cases',
    template='plotly_dark',
    plot_bgcolor='rgba(0, 0, 0, 0)',  
    paper_bgcolor='rgba(0, 0, 0, 0)',  
    font=dict(color='white'),
    xaxis=dict(title='AQI Levels', showgrid=False, zeroline=True, showline=True, linewidth=1, linecolor='white'),
    yaxis=dict(title='Work Abstenesim', showgrid=False, zeroline=True, showline=True, linewidth=1, linecolor='white'),
    title_x=0.5  # Center the title
)


# Load the data
df = pd.read_csv('aqi_health_data.csv')  # replace 'your_data.csv' with your actual file path

# Prepare data for regression
X = df[['AQI']]  # Predictor: Average AQI
y = df['NumHC']  # Target: Number of health cases

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a linear regression model and fit the data
model = LinearRegression()
model.fit(X_train, y_train)

# Predict the health cases based on AQI
y_pred = model.predict(X_test)

# Scatter plot data (actual values)
x_scatter = X_test.squeeze()  # AQI levels
y_scatter = y_test  # Actual health cases

# Regression line data (predicted values)
y_regression = y_pred  # Predicted health cases from the regression model

# Create a figure with scatter and regression line
fig7 = go.Figure()

# Add scatter plot
fig7.add_trace(go.Scatter(x=x_scatter, y=y_scatter, mode='markers', name='Data Points'))

# Add regression line
fig7.add_trace(go.Scatter(x=x_scatter, y=y_regression, mode='lines', name='Regression Line', line=dict(color='red')))

# Update layout with styling
fig7.update_layout(
    title='AQI vs Health Cases',
    template='plotly_dark',
    plot_bgcolor='rgba(0, 0, 0, 0)',
    paper_bgcolor='rgba(0, 0, 0, 0)',
    font=dict(color='white'),
    xaxis=dict(title='AQI Levels', showgrid=False, zeroline=True, showline=True, linewidth=1, linecolor='white'),
    yaxis=dict(title='Health Cases', showgrid=False, zeroline=True, showline=True, linewidth=1, linecolor='white'),
    title_x=0.5
)


correlation_coefficient = np.corrcoef(df['AQI'], df['NumHC'])[0, 1]

# Create the gauge figure
gauge_fig = go.Figure(go.Indicator(
    mode="gauge+number+delta",
    value=correlation_coefficient,  # Set the value to the correlation coefficient
    title={"text": "Correlation Coefficient: AQI vs Health Cases"},
    gauge={
        "axis": {"range": [0, 1]},  # Set the range for the gauge from 0 to 1
        "bar": {"color": "green"},  # Color of the bar
        "steps": [
            {"range": [0, 0.3], "color": "red"},  # Low correlation (red)
            {"range": [0.3, 0.6], "color": "yellow"},  # Moderate correlation (yellow)
            {"range": [0.6, 1], "color": "green"}  # High correlation (green)
        ],
    },
    number={"font": {"size": 40}},  # Set the font size of the number
))
gauge_fig.update_layout(
    template="plotly_dark",
    plot_bgcolor='rgba(0, 0, 0, 0)',
    paper_bgcolor='rgba(0, 0, 0, 0)',
    font=dict(color='white'),
    title_x=0.5
)



fig8 = go.Figure()
fig8.add_trace(go.Scatter(x=x_scatter, y=y_scatter, mode='markers', name='Data Points'))
fig8.add_trace(go.Scatter(x=x_scatter, y=y_regression, mode='lines', name='Regression Line', line=dict(color='red')))

fig8.update_layout(
    title='AQI vs Respiratory Cases',
    template='plotly_dark',
    plot_bgcolor='rgba(0, 0, 0, 0)',  
    paper_bgcolor='rgba(0, 0, 0, 0)', 
    font=dict(color='white'),
    xaxis=dict(title='AQI Levels', showgrid=False, zeroline=True, showline=True, linewidth=1, linecolor='white'),
    yaxis=dict(title='Health Cases', showgrid=False, zeroline=True, showline=True, linewidth=1, linecolor='white'),
    margin=dict(l=50, r=100, t=80, b=70),
    title_x=0.1,
    width=430, 
    height=400,
)
app.layout = html.Div(style={'backgroundColor': '#000000', 'padding': '20px'}, children=[
    html.H1('London Air Quality Findings: ', style={'color': 'white', 'textAlign': 'center'}),

 
    html.Div(style={'display': 'flex', 'flexWrap': 'wrap', 'justifyContent': 'space-between'}, children=[
        html.Div(children=[
            dcc.Graph(figure=fig1, style={'width': '100%', 'height': '400px'}),
            html.P("Figure 1: The change in PM2.5 levels in london from 2008 to 2015. In 10 years there has only been an insignificant reduction of 60 ug/m³", 
                   style={'color': 'white', 'textAlign': 'center'})
        ], style={'width': '32%'}),

        html.Div(children=[
            dcc.Graph(figure=fig2, style={'width': '100%', 'height': '400px'}),
            html.P("Figure 2: Change in respiratory diesease cases in london from 2001 to 2015. In 14 years, the number of yearly cases have only been reduced by 1700", 
                   style={'color': 'white', 'textAlign': 'center'})
        ], style={'width': '32%'}),

        html.Div(children=[
            dcc.Graph(figure=fig6, style={'width': '100%', 'height': '400px'}),
            html.P("Figure 3: Respiratory disease cases by age. As the chart depicts, most disease cases are diagnosed in teenagers and the elderly, who are more susceptible.", 
                   style={'color': 'white', 'textAlign': 'center'})
        ], style={'width': '32%'})
    ]),

    # Second row of graphs
    html.Div(style={'display': 'flex', 'flexWrap': 'wrap', 'justifyContent': 'space-between'}, children=[
        html.Div(children=[
            dcc.Graph(figure=fig3, style={'width': '100%', 'height': '400px'}),
            html.P("Figure 4: The number of work absences for male and female from 1995 to 2022. The graph shows that the number of absences are at an all time high in 2022 for women and steadily increasing for men.", 
                   style={'color': 'white', 'textAlign': 'center'})
        ], style={'width': '32%'}),

        html.Div(children=[
            dcc.Graph(figure=fig4, style={'width': '100%', 'height': '400px'}),
            html.P("Figure 5: This graph shows the main reasons for sick absences from work and their percentage of occurrence. As the data depicts, the most dominant reason for work absence in 2022 is respiratory conditions, which have steadily increased from 2019.", 
                   style={'color': 'white', 'textAlign': 'center'})
        ], style={'width': '32%'}),

        html.Div(children=[
            dcc.Graph(figure=fig5, style={'width': '100%', 'height': '400px'}),
            html.P("Figure 6: This Pie chart shows the main air pollution sources and their percentages. From the data, we can see that the main contirbutor are cars.", 
                   style={'color': 'white', 'textAlign': 'center'})
        ], style={'width': '32%'})
    ]),

    # Third row of graphs
    html.Div(style={'display': 'flex', 'justifyContent': 'center'}, children=[
        html.Div(children=[
            dcc.Graph(figure=fig7, style={'width': '100%', 'height': '400px'}),
            html.P("Figure 7: Relationship between AQI levels and work absenteeism. As shown there is a clear strong correlation.", 
                   style={'color': 'white', 'textAlign': 'center'})
        ], style={'width': '32%'}),

        html.Div(children=[
            dcc.Graph(figure=gauge_fig, style={'width': '100%', 'height': '400px'}),
            html.P("Figure 8: This diagram shows a strong correlation (0.688) between AQI levels and work absenteeism.", 
                   style={'color': 'white', 'textAlign': 'center'})
        ], style={'width': '32%'}),

        html.Div(children=[
            dcc.Graph(figure=fig_inv2, style={'width': '100%', 'height': '400px'}),
            html.P("Figure 9: Inverse exponential scenario for e-bike adoption.", 
                   style={'color': 'white', 'textAlign': 'center'})
        ], style={'width': '32%'})
    ]),

    # Fifth row: Full-width image
    html.Div(style={'display': 'flex', 'justifyContent': 'center', 'alignItems': 'center', 'flexDirection': 'column', 'padding': '20px'}, children=[
        html.Img(src='assets/airQuality.png', style={'maxWidth': '100%', 'height': 'auto', 'borderRadius': '8px'}),
        html.P("Figure 13: Shows what the Air Qulity is like during 05:00 AM,  a periopd whitout many cars",
            style={'color': 'white', 'textAlign': 'center', 'marginTop': '10px'})
    ]),
])

if __name__ == '__main__':
    app.run_server(debug=True)
