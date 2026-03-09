from dataclasses import dataclass
from dataclasses_json import dataclass_json
from typing import Optional

import flet as ft

@dataclass_json
@dataclass
@ft.observable
class AppSettings:
    language: Optional[str] = None