from dash import html, dcc
import dash_bootstrap_components as dbc
from app import app

list_of_locations ={
    "Todos": 0,
    "Manhattan": 1,
    "Bronx": 2,
    "Brooklyn": 3,
    "Queens": 4,
    "Staten Island": 5,
}

slider_size = [100, 500, 1000,  10000, 10000000]

controls = dbc.Row([
    html.Img(id="logo", src=app.get_asset_url("logo_dark.png"),style={"width":"80%", "margin-top":"15px"}),
    html.H1("VENDAS DE IMÓVEIS EM NYC", style={"margin-top": "20px", "font-size": "24px"}),
    html.P("""Este painel é um registro de cada edifício ou unidade de construção (apartamento, etc.) vendido no mercado imobiliário da cidade de Nova York durante um período de 12 meses."""),
    html.H3("""Borough""", style={"margin-top": "10px", "margin-bottom": "10px"}),
    dcc.Dropdown(
        id="location-dropdown",
        options=[{"label": i, "value": j} for i, j in list_of_locations.items()],
        value=0,
        placeholder="Selecione um Borough"
    ),
     html.H3("""Metragem(m²)""", style={"margin-top": "30px", "margin-bottom": "20px"}),
     dcc.Slider(min=0, max=4, id="slider-square-size",
                marks={i: str(j) for i, j in enumerate(slider_size)}),
    html.H3("""Parâmetro""", style={"margin-top": "30px", "margin-bottom": "20px"}),
    dcc.Dropdown(
        id="dropdown_color",
        options=[
            {'label': 'Ano de construção', 'value':'YEAR BUILT'},
            {'label': 'Total de unidades', 'value':'TOTAL UNITS'},
            {'label': 'Preço de venda', 'value':'SALE PRICE'},
            ],
            value='SALE PRICE'

    )
])