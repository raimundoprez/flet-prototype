import flet as ft

from common.app_globals import refs
from components.alert_dialog_auto_close import AlertDialogAutoClose
from contexts.app_settings_context import app_settings_context

@ft.component
def LanguageSelector(open, set_open):
    translator = refs["translator"]
    context = ft.use_context(app_settings_context)

    return AlertDialogAutoClose(
        set_open,
        open=open,
        title=ft.Text(translator.translate("LANGUAGE_SELECTOR_TITLE", None)),
        shape=ft.RoundedRectangleBorder(radius=0),
        content=ft.RadioGroup(
            content=ft.Column([
                ft.Radio(value=lang_code, label=lang_code)
                for lang_code in translator.get_languages()
            ], tight=True),
            value=context.language,
            on_change=lambda e: setattr(context, "language", e.control.value)
        )
    )