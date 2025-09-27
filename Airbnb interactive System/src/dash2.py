import numpy as np
import plotly.express as px

template_type = 'plotly_dark'


def generate_visualizations(df, selected_type):
    # Pie Chart
    room_types = df["property_type"].value_counts().head(5).reset_index(name='count')
    fig_donut1 = px.pie(room_types,
                        names='property_type',
                        values='count',
                        title='Property Types',
                        hole=0.5)
    fig_donut1.update_layout(template=template_type, font=dict(color='#fcde9c'))

    # Violin Chart
    yaxis_name = 'Log Price'
    if selected_type == 'property_type':
        top_property_types = df['property_type'].value_counts().nlargest(5).index.tolist()
        filtered_data = df[df['property_type'].isin(top_property_types)].reset_index(drop=True)
    else:
        df['bathrooms'] = np.ceil(df['bathrooms'])
        filtered_data = df[(df['bathrooms'] < 6) & (df['bedrooms'] < 6)]

    fig_violin = px.violin(
        filtered_data,
        y='log_price',
        x=selected_type,
        color=selected_type,
        title=f'Log Price Distribution by {selected_type}',
        labels={selected_type: selected_type, yaxis_name: yaxis_name},
        box=True,
        points='all',
    )
    fig_violin.update_layout(
        template=template_type, font=dict(color='#fcde9c'),
        yaxis=dict(categoryorder='total ascending')
    )

    # HeatMap
    filtered_data = df[(df['room_type'] != 'Hotel room') & (df['bedrooms'] < 5) & (df['bathrooms'] < 5)]
    avg_price = filtered_data.groupby(['bedrooms', 'bathrooms'])['price'].mean().reset_index()
    heatmap_data = avg_price.pivot(index='bedrooms', columns='bathrooms', values='price')
    # Create the heatmap
    fig_heatmap = px.imshow(
        heatmap_data,
        labels=dict(x="Number of Bathrooms", y="Number of Bedrooms", color="Average Price"),
        title="Average Price by Number of Bedrooms and Bathrooms",
        color_continuous_scale='Sunsetdark'
    )
    fig_heatmap.update_layout(
        template=template_type, font=dict(color='#fcde9c'),
        yaxis=dict(categoryorder='total ascending')
    )

    # Scatter Plot
    # Create a new column for the count of amenities
    df['amenities_count'] = df['amenities'].apply(lambda x: len(x))
    fig_scatter = px.scatter(
        df,
        x='amenities_count',
        y='log_price',
        color='room_type',
        title='Log Price vs Number of Amenities by Room Type',
        labels={'amenities_count': 'Number of Amenities', 'price': 'Log Price', 'room_type': 'Room Type'},
        color_discrete_sequence=px.colors.qualitative.Set1,
        hover_data=['room_type', 'amenities_count', 'log_price']
    )
    fig_scatter.update_layout(
        template=template_type, font=dict(color='#fcde9c'),
    )

    # #Bar chart
    # filtered_data = df[(df['room_type'].isin(selected_room_types)) & (df['bedrooms'] < 6)]
    # avg_price = filtered_data.groupby(['room_type', 'bedrooms'])['price'].mean().reset_index()
    #
    # # Bar Chart for Room Types by Count
    # fig_bar_room_types = px.bar(
    #     avg_price,
    #     x='bedrooms',
    #     y='price',
    #     color='room_type',
    #     barmode='group',
    #     title='Average Price by Number of Bedrooms and Room Type',
    #     labels={'bedrooms': 'Number of Bedrooms', 'price': 'Average Price', 'room_type': 'Room Type'},
    #     color_discrete_sequence=px.colors.qualitative.Bold
    # )
    # fig_bar_room_types.update_layout(
    #     template=template_type, font=dict(color='#fcde9c'),
    #     yaxis=dict(categoryorder='total ascending')
    # )

    return fig_violin, fig_scatter, fig_donut1, fig_heatmap
