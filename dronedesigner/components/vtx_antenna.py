from dataclasses import dataclass
from typing import ClassVar

from dronedesigner.components.component import Component, ComponentType


@dataclass
class VTX_Antenna(Component):

    yaml_tag: ClassVar = "!VTX_Antenna"

    component_type: ComponentType = ComponentType("vtx_antenna")
