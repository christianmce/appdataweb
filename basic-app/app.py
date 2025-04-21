from shiny import App, Inputs, Outputs, Session, render, ui
import numpy as np
import matplotlib.pyplot as plt

app_ui = ui.page_fluid(
    ui.layout_sidebar(
        ui.sidebar(
            ui.h2("Valores"),
            ui.input_slider("n", "y = x + 2", min=2, max=5, value=5),
        ),
        ui.output_plot("plot"),
    ),
)


def server(input: Inputs, output: Outputs, session: Session):
    @render.plot(alt="Ejemplo de Gráfico")
    def plot() -> object:
        
        x = np.arange(1, input.n()+1) 
        y = x + 2
        
        # Plot the chart          
        plt.figure(figsize=(8, 6))        
        plt.title('Título de un gráfico')
        plt.xlabel('Leyenda del eje X')
        plt.ylabel('Leyenda del eje Y')
        
        # Display grid
        plt.grid(True)
        fig = plt.plot(x, y, marker='o', linestyle='-')   
        for i, (xi, yi) in enumerate(zip(x, y)):
            plt.annotate(f'({xi}, {yi})', (xi, yi), textcoords="offset points", xytext=(0, 10), ha='center')     

        return fig


app = App(app_ui, server)