from shiny import App, ui, render
import pandas as pd
import plotly.express as px
import htmltools

df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")

app_ui = ui.page_fluid(
    ui.h2("🌸 Visualisation IRIS interactive avec Plotly"),
    ui.layout_sidebar(
        ui.sidebar(
            ui.input_select("feature", "Choisir une variable", {
                "sepal_length": "Longueur sépale",
                "sepal_width": "Largeur sépale",
                "petal_length": "Longueur pétale",
                "petal_width": "Largeur pétale"
            }),
        ),
        ui.output_ui("iris_plot")
    )
)

def server(input, output, session):
    @output
    @render.ui
    def iris_plot():
        fig = px.histogram(df, x=input.feature(), color="species", barmode="overlay")
        fig.update_layout(template="plotly_white", height=400)

        # On renvoie le composant HTML du graphique Plotly
        return htmltools.HTML(fig.to_html(include_plotlyjs="cdn", full_html=False))

app = App(app_ui, server)
