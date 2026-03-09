import flet as ft

from common.app_globals import _
from components.elements_selector import ElementsSelector
from helpers.experiment import Experiment

@ft.component
def ConfigurationMenu(experiment: Experiment):
    current_tab, set_current_tab = ft.use_state(0)

    return ft.Tabs(
        expand=True,
        selected_index=current_tab,
        length=5,
        on_change=lambda e: set_current_tab(e.control.selected_index),
        content=ft.Column(
            expand=True,
            controls=[
                ft.TabBar(
                    label_padding=ft.Padding(left=10, right=10),
                    tabs=[
                        ft.Tab(label=_("CONFIG_TAB_SPECTRAL")),
                        ft.Tab(label=_("CONFIG_TAB_LABELS")),
                        ft.Tab(label=_("CONFIG_TAB_POSITIONS")),
                        ft.Tab(label=_("CONFIG_TAB_SETTINGS")),
                        ft.Tab(label=_("CONFIG_TAB_MASKS"))
                    ]
                ),
                ft.Container(
                    expand=True,
                    padding=ft.Padding(left=5, right=5, bottom=5),
                    content=ft.TabBarView(
                        expand=True,
                        height=500,
                        controls=[
                            ft.Container(
                                content=ElementsSelector(experiment)
                            ),
                            ft.Container(
                                content=ft.Text("labels"),
                                alignment=ft.Alignment.CENTER,
                            ),
                            ft.Container(
                                content=ft.Text("positions"),
                                alignment=ft.Alignment.CENTER,
                            ),
                            ft.Container(
                                content=ft.Text("settings"),
                                alignment=ft.Alignment.CENTER,
                            ),
                            ft.Container(
                                content=ft.Text("masks"),
                                alignment=ft.Alignment.CENTER,
                            )
                        ]
                    )
                )
            ]
        )
    )