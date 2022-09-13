import dash
from dash import dcc,html
from dash.dependencies import Input, Output, State



########### Define your variables ######
myheading1='Predicting Home Sale Prices in Ames, Iowa'
image1='ames_welcome.jpeg'
tabtitle = 'Ames Housing'
sourceurl = 'http://jse.amstat.org/v19n3/decock.pdf'
githublink = 'https://github.com/manueldelreal/501-linear-reg-ames-housing'


########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout
app.layout = html.Div(children=[
    html.H1(myheading1),
    html.Div([
        html.Img(src=app.get_asset_url(image1), style={'width': '30%', 'height': 'auto'}, className='four columns'),
        html.Div([
                html.H3('Features of Home:'),
                html.Div('Year Built:'),
                dcc.Input(id='YearBuilt', value=2010, type='number', min=2006, max=2010, step=1),
                html.Div('Bathrooms:'),
                dcc.Input(id='Bathrooms', value=2, type='number', min=1, max=5, step=1),
                html.Div('Bedrooms:'),
                dcc.Input(id='BedroomAbvGr', value=4, type='number', min=1, max=5, step=1),
                html.Div('Total Square Feet:'),
                dcc.Input(id='TotalSF', value=2000, type='number', min=100, max=5000, step=1),
                html.Div('Single Family Home:'),
                dcc.Input(id='SingleFam', value=0, type='number', min=0, max=1, step=1),
                html.Div('Large Neighborhood:'),
                dcc.Input(id='LargeNeighborhood', value=0, type='number', min=0, max=1, step=1),
                html.Div('Garage Area:'),
                dcc.Input(id='GarageArea', value=500, type='number', min=0, max=2000, step=1),

            ], className='four columns'),
            html.Div([
                html.Button(children='Submit', id='submit-val', n_clicks=0,
                                style={
                                'background-color': 'red',
                                'color': 'white',
                                'margin-left': '5px',
                                'verticalAlign': 'center',
                                'horizontalAlign': 'center'}
                                ),
                html.H3('Predicted Home Value:'),
                html.Div(id='Results')
            ], className='four columns')
        ], className='twelve columns',
    ),
    html.Br(),
    html.Br(),
    html.Br(),
    html.H4('Regression Equation:'),
    html.Div('Predicted Price = (- $1,158.3K Baseline) + ($0.6K * Year Built) + ($12.4K * Bathrooms) + (- $6.8K * Bedrooms) + ($0.043K * Total Square Feet) + ($ 23.3K * Single Family Home) + (- $8.2 K * Large Neighborhood) + ($0.051K * Garage Area)'),
    html.Br(),
    html.A('Google Spreadsheet', href='https://docs.google.com/spreadsheets/d/1q2ustRvY-GcmPO5NYudvsBEGNs5Na5p_8LMeS4oM35U/edit?usp=sharing'),
    html.Br(),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A("Data Source", href=sourceurl),
    ]
)


######### Define Callback
@app.callback(
    Output(component_id='Results', component_property='children'),
    Input(component_id='submit-val', component_property='n_clicks'),
    State(component_id='YearBuilt', component_property='value'),
    State(component_id='Bathrooms', component_property='value'),
    State(component_id='BedroomAbvGr', component_property='value'),
    State(component_id='TotalSF', component_property='value'),
    State(component_id='SingleFam', component_property='value'),
    State(component_id='LargeNeighborhood', component_property='value'),
    State(component_id='GarageArea', component_property='value')

)
def ames_lr_function(clicks, YearBuilt,Bathrooms,BedroomAbvGr,TotalSF,SingleFam,LargeNeighborhood,GarageArea):
    if clicks==0:
        return "waiting for inputs"
    else:
        y = [-1158329.5822 + 597.5647*YearBuilt + 12388.176*Bathrooms + -6790.7793*BedroomAbvGr + 43.6953*TotalSF+ 23371.5406*SingleFam+ -8242.1543*LargeNeighborhood+ 51.4906*GarageArea]
        formatted_y = "${:,.2f}".format(y[0])
        return formatted_y



############ Deploy
if __name__ == '__main__':
    app.run_server(debug=True)
