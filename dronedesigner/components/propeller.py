from dataclasses import dataclass
from typing import ClassVar

from dronedesigner.components.component import Component, ComponentType


@dataclass
class Propeller(Component):

    yaml_tag: ClassVar = "!Propeller"

    component_type: ComponentType = ComponentType("propeller")
