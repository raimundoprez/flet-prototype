import flet as ft

class AlertDialogAutoClose(ft.AlertDialog):
    def __init__(self, set_open, **kwargs):
        self.set_open = set_open
        super().__init__(on_dismiss=self.handle_dismiss, **kwargs)
    
    def handle_dismiss(self):
        self.set_open(False)