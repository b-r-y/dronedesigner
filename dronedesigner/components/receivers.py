from dataclasses import dataclass
from typing import ClassVar

from dronedesigner.components.component import Component, ComponentType


@dataclass
class Receiver(Component):

    yaml_tag: ClassVar = "!Receiver"

    region: str = "unknown"
    frequency: float = 0
    component_type: ComponentType = ComponentType("receiver")


if __name__ == "__main__":

    from loaders import load_components

    stacks = load_components("receivers")
    print(stacks)
