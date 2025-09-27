import plotly.express as px

font_color = '#fcde9c'
template_type = 'plotly_dark'


def generate_visualizations(df):
    top_neighbourhoods = df['neighbourhood_cleansed'].value_counts().head(10).reset_index(name='count')
    top_neighbourhoods.rename(columns={'index': 'neighbourhood'}, inplace=True)

    # Calculate the percentage for each neighborhood
    total_count_neighbourhoods = top_neighbourhoods['count'].sum()
    top_neighbourhoods['percentage'] = (top_neighbourhoods['count'] / total_count_neighbourhoods) * 100

    # Create a horizontal bar chart with Plotly Express
    fig_neighbourhoods = px.bar(
        top_neighbourhoods,
        x='count',
        y='neighbourhood_cleansed',
        orientation='h',
        color='count',
        text='percentage',
        title='Top Neighborhoods in Western Australia',
        labels={'count': 'Count', 'neighbourhood': 'Neighborhood', 'percentage': 'Percentage'},
        color_continuous_scale='Sunsetdark'
    )

    # Display percentages as text outside the bars
    fig_neighbourhoods.update_traces(texttemplate='%{text:.2f}%', textposition='outside')
    fig_neighbourhoods.update_layout(
        template=template_type,
        font=dict(color='#fcde9c'),
        yaxis=dict(categoryorder='total ascending')  # Longest bar at the top
    )

    ## MAP
    # Aggregate data by latitude and longitude to get count or average price per location
    df['count'] = df.groupby(['latitude', 'longitude'])['price'].transform('size')
    df_agg = df.drop_duplicates(subset=['latitude', 'longitude'])  # Keep only unique locations for density

    # Create the density mapbox
    fig_density = px.density_mapbox(
        df_agg,
        lat="latitude",
        lon="longitude",
        z="count",
        radius=10,
        center={"lat": -31.9505, "lon": 115.8605},  # Center on Western Australia (e.g., Perth)
        zoom=10,
        mapbox_style="carto-darkmatter",
        color_continuous_scale="Sunsetdark",
        title="Listing Density in Western Australia"
    )

    # Customize layout for dark theme
    fig_density.update_layout(
        template=template_type,
        font=dict(color="#fcde9c")
    )

    return fig_neighbourhoods, fig_density, fig_neighbourhoods, fig_neighbourhoods
