from dataclasses import dataclass, field
from typing import List

import flet as ft

class ElementData:
    def __init__(self, name: str, measurements: List[float]):
        self.name = name
        self.measurements = measurements
        self.active = False

@dataclass
@ft.observable
class Experiment:
    positions: List[int] = field(default_factory=list)
    elements_data: List[ElementData] = field(default_factory=list)

    def toggle_element(self, pos: int, active: bool):
        elements_data = [*self.elements_data]

        old_element = self.elements_data[pos]
        new_element = ElementData(old_element.name, old_element.measurements)
        new_element.active = active
        elements_data[pos] = new_element

        self.elements_data = elements_data

    def toggle_elements(self, active: bool):
        elements_data = []

        for old_element in self.elements_data:
            new_element = ElementData(old_element.name, old_element.measurements)
            new_element.active = active
            elements_data.append(new_element)
        
        self.elements_data = elements_data