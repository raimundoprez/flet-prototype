import flet as ft

from common.app_globals import _, colors
from components.language_selector import LanguageSelector
from helpers.project_loader import ProjectLoader

@ft.component
def OptionsBar(set_image_file, set_experiment):
    settings_open, set_settings_open = ft.use_state(False)
    language_selector = LanguageSelector(settings_open, set_settings_open)

    async def load_project():
        await ProjectLoader.load_project(set_image_file, set_experiment)

    return ft.MenuBar(
        style=ft.MenuStyle(
            padding=0,
            bgcolor=colors["important_panel_background"]
        ),
        controls=[
            ft.SubmenuButton(
                content=ft.Text(_("FILE"), text_align=ft.TextAlign.CENTER),
                menu_style=ft.MenuStyle(
                    shape=ft.RoundedRectangleBorder(radius=4),
                    side=ft.BorderSide(2, colors["submenu_button_border_color"]),
                    padding=0,
                    bgcolor=colors["submenu_button_background"]
                ),
                controls=[
                    ft.MenuItemButton(
                        content=ft.Text(_("LOAD_PROJECT")),
                        leading=ft.Icon(ft.Icons.FILE_OPEN),
                        on_click=load_project
                    ),
                    ft.MenuItemButton(
                        content=ft.Text(_("SETTINGS")),
                        leading=ft.Icon(ft.Icons.SETTINGS),
                        on_click=lambda: set_settings_open(True)
                    )
                ]
            ),
            ft.SubmenuButton(
                content=ft.Text(_("VIEW"), text_align=ft.TextAlign.CENTER),
                menu_style=ft.MenuStyle(
                    shape=ft.RoundedRectangleBorder(radius=4),
                    side=ft.BorderSide(2, colors["submenu_button_border_color"]),
                    padding=0,
                    bgcolor=colors["submenu_button_background"]
                ),
                controls=[
                    ft.MenuItemButton(
                        content=ft.Text("Option"),
                        leading=ft.Icon(ft.Icons.TAG_ROUNDED),
                        on_click=lambda: None
                    ),
                    ft.MenuItemButton(
                        content=ft.Text("Option"),
                        leading=ft.Icon(ft.Icons.TAG_ROUNDED),
                        on_click=lambda: None
                    )
                ]
            ),
            language_selector
        ]
    )