import flet as ft

from common.app_globals import screen_sizes
from contexts.screen_size_context import screen_size_context

@ft.component
def ImageViewer(image_file: ft.FilePickerFile):
    screen_size = ft.use_context(screen_size_context)

    if image_file is None:
        return ft.Icon(
            ft.Icons.IMAGE,
            color="#EBEBEB",
            size=500 if screen_size >= screen_sizes["lg"] else 250
        )

    return ft.InteractiveViewer(
        content=ft.Image(src=image_file.bytes),
        pan_enabled=True,
        min_scale=0.6, # default 0.8
        max_scale=15.0 # default 2.5
    )