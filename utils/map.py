import plotly.plotly as py
from apiManager import censusAPIManager

hi = censusAPIManager('https://api.census.gov/data/')
result = hi.getAPIData(2015, 'acs5?get=NAME,B01001_001E&for=state:*')
scl = [[0.0, 'rgb(242,240,247)'],[0.2, 'rgb(218,218,235)'],[0.4, 'rgb(188,189,220)'],\
            [0.6, 'rgb(158,154,200)'],[0.8, 'rgb(117,107,177)'],[1.0, 'rgb(84,39,143)']]

print result


data = [ dict(
        type='choropleth',
        colorscale = scl,
        autocolorscale = False,
        locations = "NY",
        z = 0.5,#.astype(float),
        locationmode = 'USA-states',
        text = "random",
        marker = dict(
            line = dict (
                color = 'rgb(255,255,255)',
                width = 2
            ) ),
        colorbar = dict(
            title = "Millions USD")
        ) ]

layout = dict(
        title = 'New Map<br>(Hover for breakdown)',
        geo = dict(
            scope='usa',
            projection=dict( type='albers usa' ),
            showlakes = True,
            lakecolor = 'rgb(255, 255, 255)'),
             )
    
fig = dict( data=data, layout=layout )
print fig
py.plot( fig, filename='hello' )
