import dash
from dash import dcc, html
import plotly.graph_objs as go
import numpy as np

# Initialize the Dash app
app = dash.Dash(__name__)

# Data for the graphs
x = [i for i in range (2005, 2025)]
y1 = [i for i in range (12, 18, 2)]
y2 = [i for i in range (1200, 8900, 120)]
y3 = [i for i in range (1, 18, 1)]
y4 = [i for i in range (12, 18, 2)]

# Data for bar graphs
pieChartCategories = ['Cars', 'Factories', 'Other']
barChartCategories = ['10<', '10-18', '18-25', '25-40', '40-60', '60+']

values1 = [190, 48, 55]
values2 = [32, 42, 20, 18, 22, 45]

# Data for scatter plot with regression line
x_scatter = np.random.rand(100) * 10  # Random x values
y_scatter = 2 * x_scatter + np.random.randn(100) * 2  # Linear relationship with some noise

# Calculate the regression line (y = mx + c)
m, c = np.polyfit(x_scatter, y_scatter, 1)  # Linear fit
y_regression = m * x_scatter + c  # Regression line

# Create the figures for the graphs
fig1 = go.Figure(go.Scatter(x=x, y=y1, mode='lines'))
fig1.update_layout(
    title='Particulate Matter',
    template='plotly_dark',
    plot_bgcolor='rgba(0, 0, 0, 0)',  # Transparent plot background
    paper_bgcolor='rgba(0, 0, 0, 0)',  # Transparent paper background
    font=dict(color='white'),
    xaxis=dict(title='Year', showgrid=False, zeroline=True, showline=True, linewidth=1, linecolor='white'),
    yaxis=dict(title='PM 2.5', showgrid=False, zeroline=True, showline=True, linewidth=1, linecolor='white'),
    title_x=0.5  # Center the title
)

fig2 = go.Figure(go.Scatter(x=x, y=y2, mode='lines', name='Cosine Wave'))
fig2.update_layout(
    title='Respiratory Diseases Cases',
    template='plotly_dark',
    plot_bgcolor='rgba(0, 0, 0, 0)',  # Transparent plot background
    paper_bgcolor='rgba(0, 0, 0, 0)',  # Transparent paper background
    font=dict(color='white'),
    xaxis=dict(title='Year', showgrid=False, zeroline=True, showline=True, linewidth=1, linecolor='white'),
    yaxis=dict(title='Number of cases', showgrid=False, zeroline=True, showline=True, linewidth=1, linecolor='white'),
    title_x=0.5  # Center the title
)

fig3 = go.Figure(go.Scatter(x=x, y=y3, mode='lines', name='Tangent Wave'))
fig3.update_layout(
    title='Work Absenteeism',
    template='plotly_dark',
    plot_bgcolor='rgba(0, 0, 0, 0)',  # Transparent plot background
    paper_bgcolor='rgba(0, 0, 0, 0)',  # Transparent paper background
    font=dict(color='white'),
    xaxis=dict(title='Year', showgrid=False, zeroline=True, showline=True, linewidth=1, linecolor='white'),
    yaxis=dict(title='Number of absences', showgrid=False, zeroline=True, showline=True, linewidth=1, linecolor='white'),
    title_x=0.5  # Center the title
)

fig4 = go.Figure(go.Scatter(x=x, y=y4, mode='lines', name='Exponential Decay'))
fig4.update_layout(
    title='School Absenteeism',
    template='plotly_dark',
    plot_bgcolor='rgba(0, 0, 0, 0)',  # Transparent plot background
    paper_bgcolor='rgba(0, 0, 0, 0)',  # Transparent paper background
    font=dict(color='white'),
    xaxis=dict(title='Year', showgrid=False, zeroline=True, showline=True, linewidth=1, linecolor='white'),
    yaxis=dict(title='Number of absences', showgrid=False, zeroline=True, showline=True, linewidth=1, linecolor='white'),
    title_x=0.5  # Center the title
)

# Create pie chart
fig5 = go.Figure(go.Pie(labels=pieChartCategories, values=values1, name='Pie Chart 1'))
fig5.update_layout(
    title='Air Pollution Source',
    template='plotly_dark',
    plot_bgcolor='rgba(0, 0, 0, 0)',  # Transparent plot background
    paper_bgcolor='rgba(0, 0, 0, 0)',  # Transparent paper background
    font=dict(color='white'),
    title_x=0.5  # Center the title
)

fig6 = go.Figure(go.Bar(x=barChartCategories, y=values2, name='Bar Graph 2'))
fig6.update_layout(
    title='Respiratory Diseases Cases By Age',
    template='plotly_dark',
    plot_bgcolor='rgba(0, 0, 0, 0)',  # Transparent plot background
    paper_bgcolor='rgba(0, 0, 0, 0)',  # Transparent paper background
    font=dict(color='white'),
    title_x=0.5  # Center the title
)

xinv = np.linspace(0, 10, 100)
xcal = np.linspace(0, 10, 100)
yinv = np.exp(-xcal)


# Create the figure for the inverse exponential graph
fig_inv = go.Figure(go.Scatter(x=xinv, y=yinv, mode='lines', name='Inverse Exponential'))
fig_inv.update_layout(
    title='Scenario: Number of e-bikes/e-scooters increase',
    template='plotly_dark',
    plot_bgcolor='rgba(0, 0, 0, 0)',  # Transparent plot background
    paper_bgcolor='rgba(0, 0, 0, 0)',  # Transparent paper background
    font=dict(color='white'),
    xaxis=dict(title='Number of e-Bikes', showgrid=False, zeroline=True, showline=True, linewidth=1, linecolor='white'),
    yaxis=dict(title='respiratory health cases logarithmic', showgrid=False, zeroline=True, showline=True, linewidth=1, linecolor='white'),
    title_x=0.5  # Center the title
)

# Create the figure for the inverse exponential graph
fig_inv2 = go.Figure(go.Scatter(x=xinv, y=yinv, mode='lines', name='Inverse Exponential'))
fig_inv2.update_layout(
    title='Scenario: Number of e-bikes/e-scooters increase',
    template='plotly_dark',
    plot_bgcolor='rgba(0, 0, 0, 0)',  # Transparent plot background
    paper_bgcolor='rgba(0, 0, 0, 0)',  # Transparent paper background
    font=dict(color='white'),
    xaxis=dict(title='Number of e-Bikes', showgrid=False, zeroline=True, showline=True, linewidth=1, linecolor='white'),
    yaxis=dict(title='Work abstenesim logarithmic', showgrid=False, zeroline=True, showline=True, linewidth=1, linecolor='white'),
    title_x=0.5  # Center the title
)

# Create a gauge counter
gauge_fig = go.Figure(go.Indicator(
    mode="gauge+number+delta",
    value=0.85,  # Initial value
    title={"text": "correlation coefficient AQI vs Work Abstenesim"},
    gauge={
        "axis": {"range": [0, 1]},  # Set the range of the gauge
        "bar": {"color": "green"},  # Bar color
        "steps": [
            {"range": [0, 0.3], "color": "red"},  # Red zone
            {"range": [0.3, 0.6], "color": "yellow"},  # Yellow zone
            {"range": [0.6, 1], "color": "green"}  # Green zone
        ],
    },
    number={"font": {"size": 40}},  # Number formatting
))
gauge_fig.update_layout(
    template="plotly_dark",
    plot_bgcolor='rgba(0, 0, 0, 0)',  # Transparent plot background
    paper_bgcolor='rgba(0, 0, 0, 0)',  # Transparent paper background
    font=dict(color='white'),
    title_x=0.5  # Center the title
)


# Create a gauge counter
gauge_fig2 = go.Figure(go.Indicator(
    mode="gauge+number+delta",
    value=0.7,  # Initial value
    title={"text": "correlation coefficient AQI vs Health Cases"},
    gauge={
        "axis": {"range": [0, 1]},  # Set the range of the gauge
        "bar": {"color": "green"},  # Bar color
        "steps": [
            {"range": [0, 0.3], "color": "red"},  # Red zone
            {"range": [0.3, 0.6], "color": "yellow"},  # Yellow zone
            {"range": [0.6, 1], "color": "green"}  # Green zone
        ],
    },
    number={"font": {"size": 40}},  # Number formatting
))
gauge_fig2.update_layout(
    template="plotly_dark",
    plot_bgcolor='rgba(0, 0, 0, 0)',  # Transparent plot background
    paper_bgcolor='rgba(0, 0, 0, 0)',  # Transparent paper background
    font=dict(color='white'),
    title_x=0.5  # Center the title
)

# Generate random locations (latitude and longitude) within London
np.random.seed(42)
london_lat = 51.5074  # Latitude of London
london_lon = -0.1278  # Longitude of London

# Generate 20 random locations within a radius of London
num_hotspots = 20
latitudes = london_lat + np.random.uniform(-0.05, 0.05, num_hotspots)
longitudes = london_lon + np.random.uniform(-0.05, 0.05, num_hotspots)

# Random air quality values (higher values for worse air quality)
air_quality_values = np.random.uniform(0, 100, num_hotspots)

# Create the map figure with scattermapbox
figlond = go.Figure(go.Scattermapbox(
    lat=latitudes,
    lon=longitudes,
    mode='markers',
    marker=dict(
        size=12,
        color=air_quality_values,  # Color based on air quality
        colorscale='Viridis',  # Colorscale for bad air
        showscale=True,  # Show color scale on the side
        colorbar=dict(title="Air Quality Index (AQI)"),
    ),
    text=[f"Air Quality: {value:.2f}" for value in air_quality_values],  # Tooltip with air quality info
))

figlond.update_layout(
    title="London Air Quality Hotspots",
    mapbox=dict(
        style="carto-positron",  # Use a light map style
        center=dict(lat=london_lat, lon=london_lon),
        zoom=10,  # Zoom level for London
    ),
    template="plotly_dark",
    plot_bgcolor='rgba(0, 0, 0, 0)',  # Transparent plot background
    paper_bgcolor='rgba(0, 0, 0, 0)',  # Transparent paper background
    font=dict(color='white'),
    title_x=0.5  # Center the title
)


# Create scatter plot with regression line
fig7 = go.Figure()

# Scatter points
fig7.add_trace(go.Scatter(x=x_scatter, y=y_scatter, mode='markers', name='Data Points'))

# Regression line
fig7.add_trace(go.Scatter(x=x_scatter, y=y_regression, mode='lines', name='Regression Line', line=dict(color='red')))

fig7.update_layout(
    title='AQI vs Respiratory Health Cases',
    template='plotly_dark',
    plot_bgcolor='rgba(0, 0, 0, 0)',  # Transparent plot background
    paper_bgcolor='rgba(0, 0, 0, 0)',  # Transparent paper background
    font=dict(color='white'),
    xaxis=dict(title='AQI Levels', showgrid=False, zeroline=True, showline=True, linewidth=1, linecolor='white'),
    yaxis=dict(title='Work Abstenesim', showgrid=False, zeroline=True, showline=True, linewidth=1, linecolor='white'),
    title_x=0.5  # Center the title
)

# Create scatter plot with regression line
fig7 = go.Figure()

# Scatter points
fig7.add_trace(go.Scatter(x=x_scatter, y=y_scatter, mode='markers', name='Data Points'))

# Regression line
fig7.add_trace(go.Scatter(x=x_scatter, y=y_regression, mode='lines', name='Regression Line', line=dict(color='red')))

fig7.update_layout(
    title='AQI vs Work Abstenesim',
    template='plotly_dark',
    plot_bgcolor='rgba(0, 0, 0, 0)',  # Transparent plot background
    paper_bgcolor='rgba(0, 0, 0, 0)',  # Transparent paper background
    font=dict(color='white'),
    xaxis=dict(title='AQI Levels', showgrid=False, zeroline=True, showline=True, linewidth=1, linecolor='white'),
    yaxis=dict(title='Health Cases', showgrid=False, zeroline=True, showline=True, linewidth=1, linecolor='white'),
    title_x=0.5  # Center the title
)




# Create scatter plot with regression line
fig8 = go.Figure()

# Scatter points
fig8.add_trace(go.Scatter(x=x_scatter, y=y_scatter, mode='markers', name='Data Points'))

# Regression line
fig8.add_trace(go.Scatter(x=x_scatter, y=y_regression, mode='lines', name='Regression Line', line=dict(color='red')))

fig8.update_layout(
    title='AQI vs Respiratory Health Cases',
    template='plotly_dark',
    plot_bgcolor='rgba(0, 0, 0, 0)',  # Transparent plot background
    paper_bgcolor='rgba(0, 0, 0, 0)',  # Transparent paper background
    font=dict(color='white'),
    xaxis=dict(title='AQI Levels', showgrid=False, zeroline=True, showline=True, linewidth=1, linecolor='white'),
    yaxis=dict(title='Health Cases', showgrid=False, zeroline=True, showline=True, linewidth=1, linecolor='white'),
    title_x=0.5  # Center the title
)

# Create scatter plot with regression line
fig8 = go.Figure()

# Scatter points
fig8.add_trace(go.Scatter(x=x_scatter, y=y_scatter, mode='markers', name='Data Points'))

# Regression line
fig8.add_trace(go.Scatter(x=x_scatter, y=y_regression, mode='lines', name='Regression Line', line=dict(color='red')))

fig8.update_layout(
    title='AQI vs Respiratory Cases',
    template='plotly_dark',
    plot_bgcolor='rgba(0, 0, 0, 0)',  # Transparent plot background
    paper_bgcolor='rgba(0, 0, 0, 0)',  # Transparent paper background
    font=dict(color='white'),
    xaxis=dict(title='AQI Levels', showgrid=False, zeroline=True, showline=True, linewidth=1, linecolor='white'),
    yaxis=dict(title='Health Cases', showgrid=False, zeroline=True, showline=True, linewidth=1, linecolor='white'),
    title_x=0.5  # Center the title
)

# Layout of the dashboard
app.layout = html.Div(style={'backgroundColor': '#000000', 'padding': '20px'}, children=[
    html.H1('London Air Quality Findings: ', style={'color': 'white', 'textAlign': 'center'}),
    
    # First Row: Three graphs (adjusting width to fit them)
    html.Div(style={'display': 'flex', 'flexWrap': 'wrap', 'justifyContent': 'space-between'}, children=[
        dcc.Graph(figure=fig1, style={'width': '32%', 'height': '400px'}),
        dcc.Graph(figure=fig2, style={'width': '32%', 'height': '400px'}),
        dcc.Graph(figure=fig6, style={'width': '32%', 'height': '400px'}),
    ]),
    
    # Second Row: Three more graphs (adjusting width to fit them)
    html.Div(style={'display': 'flex', 'flexWrap': 'wrap', 'justifyContent': 'space-between'}, children=[
        dcc.Graph(figure=fig3, style={'width': '32%', 'height': '400px'}),
        dcc.Graph(figure=fig4, style={'width': '32%', 'height': '400px'}),
        dcc.Graph(figure=fig5, style={'width': '32%', 'height': '400px'}),
    ]),

    # Third Row: Scatter plot with regression line
    html.Div(style={'display': 'flex', 'justifyContent': 'center'}, children=[
        dcc.Graph(figure=fig7, style={'width': '32%', 'height': '400px'}),
        dcc.Graph(figure=gauge_fig, style={'width': '32%', 'height': '400px'}),
        dcc.Graph(figure=fig_inv, style={'width': '32%', 'height': '400px'})
    ]),

        # Third Row: Scatter plot with regression line
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
