import plotly.graph_objects as go
import streamlit as st

def grafico(aluno, temporada):
    categories = ['total','corretas','incorretas']

    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=[temporada['total'], temporada['corretas'], temporada['incorretas']],
        theta=categories,
        fill='toself',
        name='Temporada',
        line=dict(color='red')
    ))

    fig.add_trace(go.Scatterpolar(
        r=[aluno['total'], aluno['corretas'], aluno['incorretas']],
        theta=categories,
        fill='toself',
        name='Aluno',
        line=dict(color='blue')

    ))

    fig.update_layout(
    polar=dict(
        radialaxis=dict(
        visible=True,
        range=[0, max(temporada['total'], aluno['total'])]
        )),
    showlegend=True
    )

    st.write(fig)