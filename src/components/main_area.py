import flet as ft

from common.app_globals import colors, screen_sizes
from components.workmode_tab_bar import WorkmodeTabBar
from components.workmode_tab_bar_view import WorkmodeTabBarView
from components.configuration_menu import ConfigurationMenu
from contexts.screen_size_context import screen_size_context
from helpers.experiment import Experiment

@ft.component
def MainArea(image_file: ft.FilePickerFile, experiment: Experiment):
    screen_size = ft.use_context(screen_size_context)
    workmode, set_workmode = ft.use_state(0)

    return ft.Container(
        expand=True,
        padding=5,
        bgcolor=colors["main_area_background"],
        content=ft.Tabs(
            expand=True,
            selected_index=workmode,
            length=9,
            on_change=lambda e: set_workmode(e.control.selected_index),
            content=ft.Column(
                expand=True,
                spacing=5,
                horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
                scroll=ft.ScrollMode.HIDDEN if screen_size <= screen_sizes["md"] else None,
                controls=[
                    WorkmodeTabBar(),
                    ft.ResponsiveRow(
                        expand=True,
                        spacing=5,
                        run_spacing=5,
                        vertical_alignment=ft.CrossAxisAlignment.STRETCH,
                        controls=[
                            ft.Container(
                                bgcolor=colors["important_panel_background"],
                                col={"md": 12, "lg": 7, "xl": 9},
                                content=WorkmodeTabBarView(image_file, experiment)
                            ),
                            ft.Container(
                                bgcolor=colors["important_panel_background"],
                                col={"md": 12, "lg": 5, "xl": 3},
                                content=ConfigurationMenu(experiment)
                            )
                        ]
                    )
                ]
            )
        )
    )