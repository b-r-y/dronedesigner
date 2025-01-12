from dataclasses import dataclass
from typing import ClassVar

from dronedesigner.components.component import Component, ComponentType


@dataclass
class Connector(Component):

    yaml_tag: ClassVar = "!Connector"

    component_type: ComponentType = ComponentType("connector")
