from dataclasses import dataclass
from typing import ClassVar

from dronedesigner.components.component import Component, ComponentType


@dataclass
class Camera(Component):

    yaml_tag: ClassVar = "!Camera"

    component_type: ComponentType = ComponentType("camera")
