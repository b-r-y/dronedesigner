from dataclasses import dataclass
from typing import ClassVar

from dronedesigner.components.component import Component, ComponentType


@dataclass
class Custom_Part(Component):

    yaml_tag: ClassVar = "!Custom_Part"

    component_type: ComponentType = ComponentType("custom_part")
