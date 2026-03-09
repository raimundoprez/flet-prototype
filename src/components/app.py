import flet as ft
import os

from common.app_globals import refs, screen_sizes
from components.master import Master
from contexts.app_settings_context import app_settings_context
from contexts.screen_size_context import screen_size_context
from helpers.app_settings_io import AppSettingsIO

@ft.component
def App():
    def init_settings():
        settings_file = os.getenv("SETTINGS_FILE")
        app_settings_io = AppSettingsIO(settings_file)

        default_language = refs["translator"].get_default()
        app_settings = app_settings_io.read_settings(language=default_language)

        return app_settings_io, app_settings
    
    app_settings_io, app_settings = ft.use_memo(init_settings)
    app_settings, _ = ft.use_state(app_settings)

    refs["translator"].set_default(app_settings.language)

    is_first_render = ft.use_ref(True)

    def update_settings_file():
        if is_first_render.current:
            is_first_render.current = False
        else:
            app_settings_io.write_settings(app_settings)

    # update the settings file when the app settings change
    settings_list = list(app_settings.to_dict().values())
    ft.use_effect(setup=update_settings_file, dependencies=settings_list)

    def get_screen_size():
        if ft.context.page.width < screen_sizes["sm"]:
            return screen_sizes["xs"]
        elif ft.context.page.width < screen_sizes["md"]:
            return screen_sizes["sm"]
        elif ft.context.page.width < screen_sizes["lg"]:
            return screen_sizes["md"]
        elif ft.context.page.width < screen_sizes["xl"]:
            return screen_sizes["lg"]
        elif ft.context.page.width < screen_sizes["xxl"]:
            return screen_sizes["xl"]
        else:
            return screen_sizes["xxl"]
    
    screen_size, set_screen_size = ft.use_state(get_screen_size())

    def on_resize(_):
        current_size = get_screen_size()

        if current_size != screen_size:
            set_screen_size(current_size)
    
    ft.context.page.on_resize = on_resize
    
    return app_settings_context(app_settings, lambda: screen_size_context(screen_size, Master))