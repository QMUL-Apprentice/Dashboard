import dash
from dash import dcc, html
import plotly.graph_objs as go
import numpy as np


app = dash.Dash(__name__)


x = [i for i in range (2005, 2025)]
y1 = [i for i in range (12, 18, 2)]
y2 = [i for i in range (1200, 8900, 120)]
y3 = [i for i in range (1, 18, 1)]
y4 = [i for i in range (12, 18, 2)]


pieChartCategories = ['Cars', 'Factories', 'Other']
barChartCategories = ['10<', '10-18', '18-25', '25-40', '40-60', '60+']

values1 = [190, 48, 55]
values2 = [32, 42, 20, 18, 22, 45]

x_scatter = np.random.rand(100) * 10 
y_scatter = 2 * x_scatter + np.random.randn(100) * 2 


m, c = np.polyfit(x_scatter, y_scatter, 1)  
y_regression = m * x_scatter + c 


fig1 = go.Figure(go.Scatter(x=x, y=y1, mode='lines'))
fig1.update_layout(
    title='Particulate Matter',
    template='plotly_dark',
    plot_bgcolor='rgba(0, 0, 0, 0)',  
    paper_bgcolor='rgba(0, 0, 0, 0)',
    font=dict(color='white'),
    xaxis=dict(title='Year', showgrid=False, zeroline=True, showline=True, linewidth=1, linecolor='white'),
    yaxis=dict(title='PM 2.5', showgrid=False, zeroline=True, showline=True, linewidth=1, linecolor='white'),
    title_x=0.5 
)

fig2 = go.Figure(go.Scatter(x=x, y=y2, mode='lines', name='Cosine Wave'))
fig2.update_layout(
    title='Respiratory Diseases Cases',
    template='plotly_dark',
    plot_bgcolor='rgba(0, 0, 0, 0)',
    paper_bgcolor='rgba(0, 0, 0, 0)',
    font=dict(color='white'),
    xaxis=dict(title='Year', showgrid=False, zeroline=True, showline=True, linewidth=1, linecolor='white'),
    yaxis=dict(title='Number of cases', showgrid=False, zeroline=True, showline=True, linewidth=1, linecolor='white'),
    title_x=0.5 
)

fig3 = go.Figure(go.Scatter(x=x, y=y3, mode='lines', name='Tangent Wave'))
fig3.update_layout(
    title='Work Absenteeism',
    template='plotly_dark',
    plot_bgcolor='rgba(0, 0, 0, 0)',
    paper_bgcolor='rgba(0, 0, 0, 0)',
    font=dict(color='white'),
    xaxis=dict(title='Year', showgrid=False, zeroline=True, showline=True, linewidth=1, linecolor='white'),
    yaxis=dict(title='Number of absences', showgrid=False, zeroline=True, showline=True, linewidth=1, linecolor='white'),
    title_x=0.5
)

fig4 = go.Figure(go.Scatter(x=x, y=y4, mode='lines', name='Exponential Decay'))
fig4.update_layout(
    title='School Absenteeism',
    template='plotly_dark',
    plot_bgcolor='rgba(0, 0, 0, 0)',
    paper_bgcolor='rgba(0, 0, 0, 0)',
    font=dict(color='white'),
    xaxis=dict(title='Year', showgrid=False, zeroline=True, showline=True, linewidth=1, linecolor='white'),
    yaxis=dict(title='Number of absences', showgrid=False, zeroline=True, showline=True, linewidth=1, linecolor='white'),
    title_x=0.5
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


fig_inv = go.Figure(go.Scatter(x=xinv, y=yinv, mode='lines', name='Inverse Exponential'))
fig_inv.update_layout(
    title='Scenario: Number of e-bikes/e-scooters increase',
    template='plotly_dark',
    plot_bgcolor='rgba(0, 0, 0, 0)',
    paper_bgcolor='rgba(0, 0, 0, 0)', 
    font=dict(color='white'),
    xaxis=dict(title='Number of e-Bikes', showgrid=False, zeroline=True, showline=True, linewidth=1, linecolor='white'),
    yaxis=dict(title='respiratory health cases logarithmic', showgrid=False, zeroline=True, showline=True, linewidth=1, linecolor='white'),
    title_x=0.5 
)

fig_inv2 = go.Figure(go.Scatter(x=xinv, y=yinv, mode='lines', name='Inverse Exponential'))
fig_inv2.update_layout(
    title='Scenario: Number of e-bikes/e-scooters increase',
    template='plotly_dark',
    plot_bgcolor='rgba(0, 0, 0, 0)',
    paper_bgcolor='rgba(0, 0, 0, 0)',
    font=dict(color='white'),
    xaxis=dict(title='Number of e-Bikes', showgrid=False, zeroline=True, showline=True, linewidth=1, linecolor='white'),
    yaxis=dict(title='Work abstenesim logarithmic', showgrid=False, zeroline=True, showline=True, linewidth=1, linecolor='white'),
    title_x=0.5 
)

gauge_fig = go.Figure(go.Indicator(
    mode="gauge+number+delta",
    value=0.85, 
    title={"text": "correlation coefficient AQI vs Work Abstenesim"},
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
gauge_fig.update_layout(
    template="plotly_dark",
    plot_bgcolor='rgba(0, 0, 0, 0)',
    paper_bgcolor='rgba(0, 0, 0, 0)',
    font=dict(color='white'),
    title_x=0.5
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

# Generate 20 random locations within a radius of London
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
    text=[f"Air Quality: {value:.2f}" for value in air_quality_values],  # Tooltip with air quality info
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


fig7 = go.Figure()
fig7.add_trace(go.Scatter(x=x_scatter, y=y_scatter, mode='markers', name='Data Points'))
fig7.add_trace(go.Scatter(x=x_scatter, y=y_regression, mode='lines', name='Regression Line', line=dict(color='red')))

fig7.update_layout(
    title='AQI vs Work Abstenesim',
    template='plotly_dark',
    plot_bgcolor='rgba(0, 0, 0, 0)',
    paper_bgcolor='rgba(0, 0, 0, 0)',
    font=dict(color='white'),
    xaxis=dict(title='AQI Levels', showgrid=False, zeroline=True, showline=True, linewidth=1, linecolor='white'),
    yaxis=dict(title='Health Cases', showgrid=False, zeroline=True, showline=True, linewidth=1, linecolor='white'),
    title_x=0.5
)




fig8 = go.Figure()
fig8.add_trace(go.Scatter(x=x_scatter, y=y_scatter, mode='markers', name='Data Points'))
fig8.add_trace(go.Scatter(x=x_scatter, y=y_regression, mode='lines', name='Regression Line', line=dict(color='red')))

fig8.update_layout(
    title='AQI vs Respiratory Health Cases',
    template='plotly_dark',
    plot_bgcolor='rgba(0, 0, 0, 0)', 
    paper_bgcolor='rgba(0, 0, 0, 0)', 
    font=dict(color='white'),
    xaxis=dict(title='AQI Levels', showgrid=False, zeroline=True, showline=True, linewidth=1, linecolor='white'),
    yaxis=dict(title='Health Cases', showgrid=False, zeroline=True, showline=True, linewidth=1, linecolor='white'),
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
    title_x=0.5 
)
app.layout = html.Div(style={'backgroundColor': '#000000', 'padding': '20px'}, children=[
    html.H1('London Air Quality Findings: ', style={'color': 'white', 'textAlign': 'center'}),
        html.Div(style={'display': 'flex', 'flexWrap': 'wrap', 'justifyContent': 'space-between'}, children=[
        dcc.Graph(figure=fig1, style={'width': '32%', 'height': '400px'}),
        dcc.Graph(figure=fig2, style={'width': '32%', 'height': '400px'}),
        dcc.Graph(figure=fig6, style={'width': '32%', 'height': '400px'}),
    ]),
        html.Div(style={'display': 'flex', 'flexWrap': 'wrap', 'justifyContent': 'space-between'}, children=[
        dcc.Graph(figure=fig3, style={'width': '32%', 'height': '400px'}),
        dcc.Graph(figure=fig4, style={'width': '32%', 'height': '400px'}),
        dcc.Graph(figure=fig5, style={'width': '32%', 'height': '400px'}),
    ]),
    html.Div(style={'display': 'flex', 'justifyContent': 'center'}, children=[
        dcc.Graph(figure=fig7, style={'width': '32%', 'height': '400px'}),
        dcc.Graph(figure=gauge_fig, style={'width': '32%', 'height': '400px'}),
        dcc.Graph(figure=fig_inv, style={'width': '32%', 'height': '400px'})
    ]),
    html.Div(style={'display': 'flex', 'justifyContent': 'center'}, children=[
        dcc.Graph(figure=fig8, style={'width': '32%', 'height': '400px'}),
        dcc.Graph(figure=gauge_fig2, style={'width': '32%', 'height': '400px'}),
        dcc.Graph(figure=fig_inv2, style={'width': '32%', 'height': '400px'})
    ]),

    html.Div(style={'display': 'flex', 'justifyContent': 'center'}, children=[
        dcc.Graph(figure=figlond, style={'width': '100%', 'height': '800px'}),
    ]),
])

if __name__ == '__main__':
    app.run_server(debug=True)
