from dataclasses import dataclass
from typing import ClassVar

from dronedesigner.components.component import Component, ComponentType


@dataclass
class Receiver_Antenna(Component):

    yaml_tag: ClassVar = "!Receiver_Antenna"

    component_type: ComponentType = ComponentType("receiver_antenna")
