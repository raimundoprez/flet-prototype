# global objects
refs = {
    "logger": None,
    "translator": None
}

# convenient translate func
def _(msg_id: str, *args, **kwargs) -> str:
    return refs["translator"].translate(msg_id, None, *args, **kwargs)

# colors used frequently in the app
colors = {
    "main_area_background": "#353535",
    "important_panel_background": "#242424",
    "submenu_button_background": "#1B1B1B",
    "submenu_button_border_color": "#4E4E4E"
}

# typical screen size values
screen_sizes = {
    "xs": 0,
    "sm": 576,
    "md": 768,
    "lg": 992,
    "xl": 1200,
    "xxl": 1400
}