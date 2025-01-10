from dataclasses import dataclass
from enum import StrEnum
from typing import ClassVar


class ComponentType(StrEnum):
    yaml_tag: ClassVar = "!ComponentType"

    NONE = "undefined"
    FRAME = "frame"
    RECEIVER = "receiver"
    RECEIVER_ANTENNA = "receiver_antenna"
    TRANSMITTER = "transmitter"
    ESC = "ecs"
    FC = "fc"
    STACK = "stack"
    MOTOR = "motor"
    PROPELLER = "propeller"
    VTX = "vtx"
    VTX_ANTENNA = "vtx_antenna"
    CAMERA = "camera"
    GPS = "gps"
    BATTERY = "battery"
    BATTERY_STRAP = "battery_strap"
    CUSTOM_PART = "custom_part"

    @classmethod
    def to_yaml(cls, representer, node):
        return representer.represent_scalar(
            cls.yaml_tag, f"{node.name}"  # .format(node, node)
        )

    @classmethod
    def from_yaml(cls, constructor, node):
        return cls[node.value]


@dataclass
class Component:

    name: str = "default_name"
    short_name: str = "default_name"
    mass: float = 0
    cost: float = 0
    number_of_units: int = 1
    component_type: ComponentType = ComponentType("undefined")


if __name__ == "__main__":
    import ruamel.yaml

    yaml = ruamel.yaml.YAML()
    yaml.register_class(cls=ComponentType)

    comp_type = ComponentType("frame")

    with open(file="test_yaml_dump.yaml", mode="w", encoding="utf-8") as file:
        yaml.dump(data=comp_type, stream=file)

    with open(file="test_yaml_dump.yaml", mode="r", encoding="utf-8") as file:
        newer_comp_type: ComponentType = yaml.load(stream=file)

        b = 1
