import flet as ft
from helpers.app_settings import AppSettings

# create a settings context with a default context
app_settings_default = AppSettings()
app_settings_context = ft.create_context(app_settings_default)