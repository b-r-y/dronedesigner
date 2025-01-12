from dataclasses import dataclass
from typing import ClassVar

from dronedesigner.components.component import Component, ComponentType


@dataclass
class GPS(Component):

    yaml_tag: ClassVar = "!GPS"

    component_type: ComponentType = ComponentType("gps")
