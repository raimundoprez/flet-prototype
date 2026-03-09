import flet as ft
import flet_charts as fch
import plotly.graph_objects as go
import os

from datetime import datetime

from common.app_globals import refs, _
from common.utils import pretty_exception
from helpers.experiment import Experiment

@ft.component
def StackedBarsChart(experiment: Experiment):
    # usable data
    positions = experiment.positions
    elements_data = [element_data for element_data in experiment.elements_data if element_data.active]

    # create figure
    fig = go.Figure()

    # add a series per element
    for element_data in elements_data:
        fig.add_bar(
            name=element_data.name,
            x=positions,
            y=element_data.measurements
        )

    # set layout
    fig.update_layout(
        barmode="stack",
        title=_("PLOT_MEASUREMENTS_BY_POSITION"),
        xaxis_title=_("PLOT_POSITIONS"),
        yaxis_title=_("PLOT_MEASUREMENTS")
    )

    # download func
    def download(event):
        try:
            output = os.getenv("OUTPUT_DIR")
            os.makedirs(output, exist_ok=True)

            now = datetime.now()
            formatted_date = now.strftime("_%Y_%m_%d_%H_%M_%S_%f")

            fig.write_image(output + "/stacked_bars_chart" + formatted_date + ".png")
        except Exception as e:
            refs["logger"].error(pretty_exception("Failed to download a stacked bars chart image", e))

            ft.context.page.show_dialog(ft.AlertDialog(
                title=_("DOWNLOAD_IMAGE_FAILED_TITLE"),
                shape=ft.RoundedRectangleBorder(radius=0),
                content=ft.Text(_("DOWNLOAD_IMAGE_FAILED_DESCRIPTION")),
                actions=[ft.TextButton(_("DOWNLOAD_IMAGE_FAILED_DISMISS"), on_click=lambda _: ft.context.page.pop_dialog())]
            ))

    # create chart
    chart = fch.PlotlyChart(figure=fig, expand=True)

    return ft.Stack(
        expand=True,
        controls=[
            chart,
            ft.Button(
                content=ft.Text(_("DOWNLOAD_BUTTON_TEXT")),
                on_click=download,
                left=5,
                bottom=5,
                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0))
            )
        ]
    )