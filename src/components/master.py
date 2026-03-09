import flet as ft

from common.app_globals import _
from components.main_area import MainArea
from components.options_bar import OptionsBar
from helpers.experiment import Experiment

@ft.component
def Master():
    ft.context.page.title = _("PAGE_TITLE")
    ft.context.page.padding = 0

    ft.context.page.theme = ft.Theme(
        color_scheme=ft.ColorScheme(
            primary=ft.Colors.BLUE_300
        ),
        scrollbar_theme=ft.ScrollbarTheme(
            thumb_color=ft.Colors.with_opacity(0.5, ft.Colors.BLACK),
            thickness=10
        ),
        checkbox_theme=ft.CheckboxTheme(
            border_side=ft.BorderSide(color=ft.Colors.BLACK)
        ),
        icon_theme=ft.IconTheme(
            color=ft.Colors.BLACK
        )
    )

    image_file, set_image_file = ft.use_state(None)
    experiment, set_experiment = ft.use_state(Experiment())

    return ft.Column(
        expand=True,
        spacing=0,
        horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
        controls=[OptionsBar(set_image_file, set_experiment), MainArea(image_file, experiment)]
    )