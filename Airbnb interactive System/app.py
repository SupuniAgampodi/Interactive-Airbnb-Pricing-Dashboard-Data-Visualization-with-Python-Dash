from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
from src.const import get_constants
import numpy as np

from src.dash1 import generate_visualizations as generate_visualizations1
from src.dash2 import generate_visualizations as generate_visualizations2
from src.dash3 import generate_visualizations as generate_visualizations3
from src.dash4 import generate_visualizations as generate_visualizations4

theme_color = '#ff385c'
tile_color = 'dfa19b'
bg_color = 'black'
font_color = '#fcde9c'

# Load the Airbnb data
df = pd.read_csv('listings.csv')  # Update this path as needed

# Data Preprocessing Steps
df.dropna(subset=['room_type', 'bedrooms', 'price'], inplace=True)
df['price'] = df['price'].replace({'\$': '', ',': ''}, regex=True).astype(float)
df['log_price'] = np.log(df['price'])
df['host_acceptance_rate'] = df['host_acceptance_rate'].str.replace('%', '').astype(float)
df['host_response_rate'] = df['host_response_rate'].str.replace('%', '').astype(float)
df['log_host_acceptance_rate'] = np.log(df['host_acceptance_rate'])
df['log_host_response_rate'] = np.log(df['host_response_rate'])

top_room_types = df['room_type'].value_counts().nlargest(5).index.tolist()
room_type_options = [{'label': room_type, 'value': room_type} for room_type in top_room_types]

total_listings, neighbourhood_count, property_type_count, room_type_count = get_constants(df)

# Initialize the app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], title='Airbnb Data Analysis Dashboard')
server = app.server


def generate_stats_card(title, value, image_path):
    return html.Div(
        dbc.Card([
            dbc.CardImg(src=image_path, top=True, style={'width': '50px', 'alignSelf': 'center'}),
            dbc.CardBody([
                html.P(value, className="card-value",
                       style={'margin': '0px', 'fontSize': '22px', 'fontWeight': 'bold'}),
                html.H4(title, className="card-title",
                        style={'margin': '0px', 'fontSize': '18px', 'fontWeight': 'bold'})
            ], style={'textAlign': 'center'}),
        ], style={'paddingBlock': '10px', "backgroundColor": theme_color, 'border': 'none', 'borderRadius': '10px'})
    )


tab_style = {
    'idle': {
        'borderRadius': '10px',
        'padding': '0px',
        'marginInline': '5px',
        'display': 'flex',
        'alignItems': 'center',
        'justifyContent': 'center',
        'fontWeight': 'bold',
        'backgroundColor': '#ff385c',
        'border': 'none'
    },
    'active': {
        'borderRadius': '10px',
        'padding': '0px',
        'marginInline': '5px',
        'display': 'flex',
        'alignItems': 'center',
        'justifyContent': 'center',
        'fontWeight': 'bold',
        'border': 'none',
        'textDecoration': 'underline',
        'backgroundColor': '#dfa19b'
    }
}

# Define the layout of the app
app.layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(
                html.Div(
                    html.H2("Airbnb Listing Analysis of Western Australia",
                            style={'color': theme_color, 'marginTop': '10px', 'textAlign': 'center'}),
                )
            ),
        ]),
        dbc.Row([
            # dbc.Col(html.Img(src="./assets/airbnb_icon.png", width=150), width=2),
            dbc.Col(
                dcc.Tabs(id='graph-tabs', value='overview', children=[
                    dcc.Tab(label='Home', value='overview', style=tab_style['idle'],
                            selected_style=tab_style['active']),
                    dcc.Tab(label='Location', value='location', style=tab_style['idle'],
                            selected_style=tab_style['active']),
                    dcc.Tab(label='Listings', value='listings', style=tab_style['idle'],
                            selected_style=tab_style['active']),
                    dcc.Tab(label='Host', value='host', style=tab_style['idle'],
                            selected_style=tab_style['active'])
                ], style={'marginTop': '15px', 'width': '600px', 'height': '50px', 'marginTop': '10px'}), width=6),
        ]),
        # Radio buttons container (visible only on the 'Host' tab)
        html.Div(id="radio-container", children=[
            html.Div([
                html.Label("Select X-axis:", style={'color': '#fcde9c', 'marginRight': '10px'}),
                dcc.RadioItems(
                    id='xaxis-radio',
                    options=[
                        {'label': 'Superhost Status', 'value': 'host_is_superhost'},
                        {'label': 'Identity Verified', 'value': 'host_identity_verified'},
                        {'label': 'Profile Picture Available', 'value': 'host_has_profile_pic'}
                    ],
                    value='host_is_superhost',  # Default selection
                    labelStyle={'display': 'inline-block', 'margin-right': '10px', 'color': '#fcde9c'}
                ),
            ], style={'display': 'flex', 'alignItems': 'center', 'marginBottom': '10px'}),

            html.Div([
                html.Label("Select Y-axis:", style={'color': '#fcde9c', 'marginRight': '10px'}),
                dcc.RadioItems(
                    id='yaxis-radio',
                    options=[
                        {'label': 'Log Price', 'value': 'log_price'},
                        {'label': 'Host Acceptance Rate', 'value': 'host_acceptance_rate'},
                        {'label': 'Host Response Rate', 'value': 'host_response_rate'}
                    ],
                    value='log_price',  # Default selection
                    labelStyle={'display': 'inline-block', 'margin-right': '10px', 'color': '#fcde9c'}
                ),
            ], style={'display': 'flex', 'alignItems': 'center', 'marginBottom': '10px'}),
        ], style={'textAlign': 'left', 'marginTop': '20px'}),

        # Checklist container (visible only on the 'Listings' tab)
        html.Div(id="checkbox-container", children=[
            html.Div([
                html.Label("X-axsis:", style={'color': '#fcde9c', 'marginRight': '10px'}),
                dcc.RadioItems(
                    id='room_type_checklist',
                    options=[
                        {'label': 'Room Type', 'value': 'room_type'},
                        {'label': 'Property Type', 'value': 'property_type'},
                        {'label': 'Bedrooms', 'value': 'bedrooms'},
                        {'label': 'Bathrooms', 'value': 'bathrooms'}
                    ],
                    value='room_type',  # Default selection
                    labelStyle={'display': 'inline-block', 'margin-right': '10px', 'color': '#fcde9c'}
                ),
            ], style={'display': 'flex', 'alignItems': 'center', 'marginBottom': '10px', 'marginTop': '20px'}),
        ], style={'textAlign': 'left', 'marginTop': '20px'}),

        dbc.Row([
            dcc.Loading([
                html.Div(id='tabs-content')
            ], type='default', color=theme_color)
        ]),
    ], style={'padding': '0px'})
], style={'backgroundColor': bg_color, 'minHeight': '100vh'})


@app.callback(
    [Output("radio-container", "style"),
     Output("checkbox-container", "style")],
    Input("graph-tabs", "value")
)
def show_controls(tab):
    if tab == 'host':  # Show only for 'Host' tab
        return {'display': 'block', 'textAlign': 'center', 'marginTop': '20px'}, {'display': 'none'}
    elif tab == 'listings':  # Show only for 'Listings' tab
        return {'display': 'none'}, {'display': 'block'}
    return {'display': 'none'}, {'display': 'none'}


@app.callback(
    Output('tabs-content', 'children'),
    [Input('graph-tabs', 'value')],
    [Input('xaxis-radio', 'value'),
     Input('yaxis-radio', 'value'),
     Input('room_type_checklist', 'value')]
)
def update_tab(tab, xaxis_name, yaxis_name, listings_categories):
    if tab == 'overview':
        content = generate_visualizations4(df)
        return html.Div([
            html.Div(content, style={'width': '100%', 'display': 'inline-block'}),
        ]),
    elif tab == 'location':
        fig1, fig2, fig3, fig4 = generate_visualizations1(df)
        return html.Div([
            html.Div([
                dcc.Graph(id='graph1', figure=fig1),
            ], style={'width': '50%', 'display': 'inline-block'}),
            html.Div([
                dcc.Graph(id='graph2', figure=fig2),
            ], style={'width': '50%', 'display': 'inline-block'})
        ])
    elif tab == 'listings':
        fig1, fig2, fig3, fig4 = generate_visualizations2(df, listings_categories)
        return html.Div([
            html.Div([
                dcc.Graph(id='graph6', figure=fig1),
            ], style={'width': '100%', 'display': 'inline-block'}),
            html.Div([
                dcc.Graph(id='graph4', figure=fig3),
            ], style={'width': '50%', 'display': 'inline-block'}),
            html.Div([
                dcc.Graph(id='graph5', figure=fig4),
            ], style={'width': '50%', 'display': 'inline-block'}),
            html.Div([
                dcc.Graph(id='graph3', figure=fig2),
            ], style={'width': '100%', 'display': 'inline-block'}),
        ])
    elif tab == 'host':
        fig1, fig2 = generate_visualizations3(df, xaxis_name, yaxis_name)
        # fig2 = generate_visualizations5(df)
        return html.Div([
            html.Div([
                dcc.Graph(id='graph7', figure=fig1),
            ], style={'width': '100%', 'display': 'inline-block'}),
            html.Div([
                dcc.Graph(id='graph8', figure=fig2),
            ], style={'width': '100%', 'display': 'inline-block'}),
        ])


if __name__ == '__main__':
    app.run_server(debug=False)
