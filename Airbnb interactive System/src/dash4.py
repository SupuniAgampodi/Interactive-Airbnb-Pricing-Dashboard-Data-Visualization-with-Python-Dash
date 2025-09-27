from dash import html

template_type = 'plotly_dark'
theme_color = '#ff385c'


# Define visualizations
def generate_visualizations(df):
    content = html.Div([
        html.H3("Introduction", style={'color': theme_color}),
        html.P(
            "This project focuses on developing an interactive data visualization system for Airbnb listings to "
            "aid in understanding and optimizing rental pricing. With the dynamic growth of Airbnb, hosts and investors "
            "face the challenge of setting competitive prices to maximize occupancy and revenue. The dashboard provides a "
            "platform for users to explore factors influencing pricing, such as location, property features, and host "
            "characteristics, using an intuitive, interactive interface..",
            style={'color': 'white', 'fontSize': '16px'}
        ),
        html.H3("Problem Definition", style={'color': theme_color}),
        html.P(
            "What factors significantly affect Airbnb listing prices, and how can hosts leverage this data to "
            "maximize occupancy and revenue?",
            style={'color': 'white', 'fontSize': '16px'}
        ),
        html.H3("Narrative", style={'color': theme_color}),
        html.P(
            "Imagine Sam, an aspiring Airbnb host unsure how to price his listing in a competitive market. Through "
            "the interactive dashboard, Sam can explore rental trends, identify high-demand neighbourhoods, and analyze which "
            "room types justify higher prices. This tool empowers Sam to make data-driven decisions, set competitive prices, "
            "and increase his listing’s profitability.",
            style={'color': 'white', 'fontSize': '16px'}
        ),
        html.H3("Target Audience", style={'color': theme_color}),
        html.Ul([
            html.Li("Existing Airbnb Hosts: To refine pricing strategies", style={'color': 'white'}),
            html.Li("Prospective Property Investors: To identify high-demand areas and profitable property types.",
                    style={'color': 'white'}),
            html.Li("Real Estate Analysts: To generate market trend insights.", style={'color': 'white'}),
            html.Li("Data Enthusiasts and Researchers: To leverage the platform for extended data exploration.",
                    style={'color': 'white'}),
        ], style={'padding': '20px', 'backgroundColor': '#333', 'borderRadius': '10px', 'marginBottom': '20px'}),
        html.H3("Introduction to Data Set", style={'color': theme_color}),
        html.P(
            "The dataset used for this project comes from Inside Airbnb (Western Australia, 2024), an open-data platform "
            "that provides detailed information about Airbnb listings in cities of Western Australia. This comprehensive "
            "dataset aims to foster transparency within the short-term rental market by offering extensive details beneficial "
            "to hosts, investors, analysts, and researchers. ", style={'color': 'white'}),
        html.H3("Data Analysis Summary", style={'color': theme_color}),
        html.P(
            "The Airbnb data shows a right-skewed price distribution, with most listings priced low and a few luxury options "
            "forming a long tail. Smaller properties (1-2 bedrooms, 1 bathroom) are common, with specific neighborhoods dominating. "
            "Host characteristics impact pricing slightly, with Super Hosts and verified hosts generally listing higher-priced properties. "
            "Entire homes/apartments have the highest prices, while private and shared rooms are more affordable, especially in urban "
            "centers where demand is highest. Correlations indicate that more bedrooms, beds, and guest capacity slightly raise prices, "
            "though location and host responsiveness remain key factors.", style={'color': 'white'}),
        html.H3("Hypothesis", style={'color': theme_color}),
        html.Ul([
            html.Li(
                "Listings in tourist-heavy or central areas are priced significantly higher than those in suburbs.",
                style={'color': 'white'}),
            html.Li(
                "How do specific listing features (e.g., number of bedrooms, bathrooms, and amenities) affect the price of a property?",
                style={'color': 'white'}),
            html.Li(
                "Do host characteristics (e.g., superhost status, host response rate, and host verified status) affect the price of a listing?",
                style={'color': 'white'}),
        ], style={'padding': '20px', 'backgroundColor': '#333', 'borderRadius': '10px', 'marginBottom': '20px'}),
    ], style={'padding': '20px', 'backgroundColor': '#333', 'borderRadius': '10px', 'marginBottom': '20px'}),
    return content
