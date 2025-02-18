from ucimlrepo import fetch_ucirepo
import plotly.express as px
import pandas as pd
from dash import Dash, dcc, html
import dash_bootstrap_components as dbc

# Carregando e preparando os dados
heart_disease = fetch_ucirepo(id=45)
dados = pd.DataFrame(heart_disease.data.features)
dados["doenca"] = (heart_disease.data.targets > 0).astype(int)

# Criando os gráficos iniciais
figura_histograma = px.histogram(dados, x='age', title='Histograma de Idades')
div_do_histograma = html.Div([
    html.H2('Histograma de Idades', className='text-center'),
    dcc.Graph(figure=figura_histograma),
])

figura_boxplot = px.box(dados, x='doenca', y='age', color='doenca', title='Distribuição das Idades')
div_do_boxplot = html.Div([
    html.H2('Distribuição das Idades', className='text-center'),
    dcc.Graph(figure=figura_boxplot)
])

# Adicionando os novos gráficos
figura_boxplot_chol = px.box(dados, x='doenca', y='chol', color='doenca', title='Colesterol Sérico')
div_do_boxplot_chol = html.Div([
    html.H2('Colesterol Sérico', className='text-center'),
    dcc.Graph(figure=figura_boxplot_chol)
])

figura_boxplot_trestbps = px.box(dados, x='doenca', y='trestbps', color='doenca', title='Pressão Sanguínea em Repouso')
div_do_boxplot_trestbps = html.Div([
    html.H2('Pressão Sanguínea em Repouso', className='text-center'),
    dcc.Graph(figure=figura_boxplot_trestbps)
])

# Organizando o layout
layout = html.Div([
    html.H1('Análise de Dados do UCI Repository Heart Disease', className='text-center mb-5'),
    dbc.Container([
        dbc.Row([
            dbc.Col([div_do_histograma, div_do_boxplot], md=6),
            dbc.Col([div_do_boxplot_chol, div_do_boxplot_trestbps], md=6)
        ], align="start"),    
    ])
])
