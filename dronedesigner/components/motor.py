from dataclasses import dataclass
from typing import ClassVar

from dronedesigner.components.component import Component, ComponentType


@dataclass
class Motor(Component):

    yaml_tag: ClassVar = "!Motor"

    component_type: ComponentType = ComponentType("motor")

    number_of_units: int = 4
