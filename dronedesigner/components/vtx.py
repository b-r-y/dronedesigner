from dataclasses import dataclass
from typing import ClassVar

from dronedesigner.components.component import Component, ComponentType


@dataclass
class VTX(Component):

    yaml_tag: ClassVar = "!VTX"

    component_type: ComponentType = ComponentType("vtx")
