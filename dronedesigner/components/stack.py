from dataclasses import dataclass
from typing import ClassVar

from dronedesigner.components.component import Component, ComponentType


@dataclass
class Stack(Component):

    yaml_tag: ClassVar = "!Stack"

    mounting_size: str = "unknown"
    component_type: ComponentType = ComponentType("stack")


if __name__ == "__main__":

    from dronedesigner.components.loaders import load_components

    stacks = load_components(filename="stacks")
    print(stacks)
