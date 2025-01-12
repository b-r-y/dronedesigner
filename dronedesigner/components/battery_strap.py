from dataclasses import dataclass
from typing import ClassVar

from dronedesigner.components.component import Component, ComponentType


@dataclass
class Battery_Strap(Component):

    yaml_tag: ClassVar = "!Battery_Strap"

    component_type: ComponentType = ComponentType("battery_strap")
