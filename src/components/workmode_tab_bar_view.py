import flet as ft

from components.image_viewer import ImageViewer
from components.stacked_bars_chart import StackedBarsChart
from helpers.experiment import Experiment

@ft.component
def WorkmodeTabBarView(image_file: ft.FilePickerFile, experiment: Experiment):
    return ft.Container(
        expand=True,
        padding=5,
        content=ft.TabBarView(
            expand=True,
            height=500,
            controls=[
                ft.Container(
                    content=ImageViewer(image_file)
                ),
                ft.Container(
                    content=ft.Text("2"),
                    alignment=ft.Alignment.CENTER,
                ),
                ft.Container(
                    content=ft.Text("3"),
                    alignment=ft.Alignment.CENTER,
                ),
                ft.Container(
                    content=ft.Text("4"),
                    alignment=ft.Alignment.CENTER,
                ),
                ft.Container(
                    content=StackedBarsChart(experiment)
                ),
                ft.Container(
                    content=ft.Text("6"),
                    alignment=ft.Alignment.CENTER,
                ),
                ft.Container(
                    content=ft.Text("7"),
                    alignment=ft.Alignment.CENTER,
                ),
                ft.Container(
                    content=ft.Text("8"),
                    alignment=ft.Alignment.CENTER,
                ),
                ft.Container(
                    content=ft.Text("9"),
                    alignment=ft.Alignment.CENTER,
                )
            ]
        )
    )