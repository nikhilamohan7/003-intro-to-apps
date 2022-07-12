######### import libraries 

import dash
from dash import html
from dash import dcc
import plotly.graph_objs as go

########### Define your variables
beers=['California', 'Texas', 'Florida', 'New York']
ibu_values=[37.2, 25.1, 18.8, 19.3]
abv_values=[39.2, 29.5, 21.7, 19.8]
color1='blue'
color2='green'
mytitle='Census population by State and Year'

label1='2020 (in M)'
label2='2021 (in M)'

########### Set up the chart

def make_that_cool_barchart(beers, ibu_values, abv_values, color1, color2, mytitle):
    bitterness = go.Bar(
        x=beers,
        y=ibu_values,
        name=label1,
        marker={'color':color1}
    )
    alcohol = go.Bar(
        x=beers,
        y=abv_values,
        name=label2,
        marker={'color':color2}
    )

    beer_data = [bitterness, alcohol]
    beer_layout = go.Layout(
        barmode='group',
        title = mytitle
    )

    beer_fig = go.Figure(data=beer_data, layout=beer_layout)
    return beer_fig


######### Run the function #######

if __name__ == '__main__':
    fig = make_that_cool_barchart(beers, ibu_values, abv_values, color1, color2, mytitle)
    fig.write_html('docs/barchartnew2.html')
    print('We successfully updated the barchart!')
