import plotly.express as px

template_type = 'plotly_dark'


def generate_visualizations(df, xaxis_name, yaxis_name):
    fig_violin1 = px.violin(
        df,
        x=xaxis_name,
        y=yaxis_name,
        title=f'{yaxis_name} Distribution by {xaxis_name}',
        labels={xaxis_name: xaxis_name, yaxis_name: yaxis_name},
        color=xaxis_name,
        box=True,
        points='all',
        color_discrete_sequence=['crimson', 'blue']
    )
    fig_violin1.update_layout(
        template=template_type, font=dict(color='#fcde9c'),
    )
    # Update legend labels
    fig_violin1.for_each_trace(
        lambda t: t.update(name='True' if t.name == 't' else 'False' if t.name == 'f' else t.name))

    fig_hist = px.histogram(
        df,
        x='log_price',
        color='instant_bookable',
        title='Log Price Distribution by Instant Bookable Status',
        labels={'log_price': 'Log Price', 'instant_bookable': 'Instant Bookable?'},
        barmode='overlay',
        color_discrete_sequence=['white', 'blue']
    )
    fig_hist.update_layout(
        template=template_type, font=dict(color='#fcde9c'),
    )

    # Update legend labels
    fig_hist.for_each_trace(
        lambda t: t.update(name='True' if t.name == 't' else 'False' if t.name == 'f' else t.name))

    return fig_violin1, fig_hist
