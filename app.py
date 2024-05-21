from flask import Flask
import dash
from dash import html, dcc, Input, Output
import dash_bootstrap_components as dbc

server = Flask(__name__)
app = dash.Dash(__name__, server=server, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("Calculadora de Pontuação", className='text-center my-4'), width=12)
    ]),
    dbc.Row([
        dbc.Col([
            html.H3("Dashboards"),
            dbc.Row([
                dbc.Col(dbc.Label("Descrição Dash:"), width=4),
                dbc.Col(dcc.Input(id='descricao_dash', type='number', value=0, step=1, className='mb-2'), width=8)
            ]),
            dbc.Row([
                dbc.Col(dbc.Label("Custom Properties:"), width=4),
                dbc.Col(dcc.Input(id='custom_properties', type='number', value=0, step=1, className='mb-2'), width=8)
            ]),
            dbc.Row([
                dbc.Col(dbc.Label("Owner:"), width=4),
                dbc.Col(dcc.Input(id='owner_dash', type='number', value=0, step=1, className='mb-2'), width=8)
            ]),
            dbc.Row([
                dbc.Col(dbc.Label("Qtd Charts:"), width=4),
                dbc.Col(dcc.Input(id='qtd_charts', type='number', value=0, step=1, className='mb-2'), width=8)
            ]),
            dbc.Row([
                dbc.Col(dbc.Label("Qtd Data Models:"), width=4),
                dbc.Col(dcc.Input(id='qtd_data_models', type='number', value=0, step=1, className='mb-2'), width=8)
            ]),
            dbc.Row([
                dbc.Col(dbc.Label("Qtd Colunas (Catalogadas):"), width=4),
                dbc.Col(dcc.Input(id='qtd_colunas', type='number', value=0, step=1, className='mb-2'), width=8)
            ]),
            dbc.Row([
                dbc.Col(dbc.Label("Qtd Tags:"), width=4),
                dbc.Col(dcc.Input(id='qtd_tags', type='number', value=0, step=1, className='mb-2'), width=8)
            ]),
            dbc.Row([
                dbc.Col(dbc.Label("Domínio de Dados:"), width=4),
                dbc.Col(dcc.Input(id='dominio_dados', type='number', value=0, step=1, className='mb-4'), width=8)
            ])
        ], width=6),
        dbc.Col([
            html.H3("Tabelas"),
            dbc.Row([
                dbc.Col(dbc.Label("Descrição Tabela:"), width=4),
                dbc.Col(dcc.Input(id='descricao_tabela', type='number', value=0, step=1, className='mb-2'), width=8)
            ]),
            dbc.Row([
                dbc.Col(dbc.Label("Owner:"), width=4),
                dbc.Col(dcc.Input(id='owner_tabela', type='number', value=0, step=1, className='mb-2'), width=8)
            ]),
            dbc.Row([
                dbc.Col(dbc.Label("Qtd Colunas (Catalogadas):"), width=4),
                dbc.Col(dcc.Input(id='qtd_colunas_tabela', type='number', value=0, step=1, className='mb-2'), width=8)
            ]),
            dbc.Row([
                dbc.Col(dbc.Label("Qtd Tags:"), width=4),
                dbc.Col(dcc.Input(id='qtd_tags_tabela', type='number', value=0, step=1, className='mb-2'), width=8)
            ]),
            dbc.Row([
                dbc.Col(dbc.Label("Domínio de Dados:"), width=4),
                dbc.Col(dcc.Input(id='dominio_dados_tabela', type='number', value=0, step=1, className='mb-4'), width=8)
            ])
        ], width=6)
    ]),
    dbc.Row([
        dbc.Col(dbc.Button('Calcular', id='button', color='primary', className='mt-3 mb-3'), width=12)
    ]),
    dbc.Row([
        dbc.Col(html.Div(id='output-container-button', className='text-center'), width=12)
    ])
], fluid=True)

@app.callback(
    Output('output-container-button', 'children'),
    [Input('button', 'n_clicks')],
    [
        Input('descricao_dash', 'value'),
        Input('custom_properties', 'value'),
        Input('owner_dash', 'value'),
        Input('qtd_charts', 'value'),
        Input('qtd_data_models', 'value'),
        Input('qtd_colunas', 'value'),
        Input('qtd_tags', 'value'),
        Input('dominio_dados', 'value'),
        Input('descricao_tabela', 'value'),
        Input('owner_tabela', 'value'),
        Input('qtd_colunas_tabela', 'value'),
        Input('qtd_tags_tabela', 'value'),
        Input('dominio_dados_tabela', 'value')
    ]
)
def calculate_score(n_clicks, desc_dash, custom_prop, owner_dash, qtd_charts, qtd_models, qtd_cols, qtd_tags, domain_data, desc_table, owner_table, qtd_cols_table, qtd_tags_table, domain_data_table):
    score_dash = (3 * desc_dash) + (4 * custom_prop) + (2 * owner_dash) + (3 * qtd_charts) + (3 * qtd_models) + (1 * qtd_cols) + (2 * qtd_tags) + (2 * domain_data)
    score_table = (2 * desc_table) + (2 * owner_table) + (3 * qtd_cols_table) + (1 * qtd_tags_table) + (2 * domain_data_table)
    
    total_score = score_dash + score_table
    
    return f"A pontuação total é: {total_score}"

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0')
