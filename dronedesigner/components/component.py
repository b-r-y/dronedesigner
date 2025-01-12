from dataclasses import dataclass
from enum import StrEnum
from typing import ClassVar


class ComponentType(StrEnum):
    yaml_tag: ClassVar = "!ComponentType"

    NONE = "undefined"
    BATTERY = "battery"
    BATTERY_STRAP = "battery_strap"
    CONNECTOR = "connector"
    FRAME = "frame"
    RECEIVER = "receiver"
    RECEIVER_ANTENNA = "receiver_antenna"
    ESC = "ecs"
    FC = "fc"
    STACK = "stack"
    MOTOR = "motor"
    PROPELLER = "propeller"
    VTX = "vtx"
    VTX_ANTENNA = "vtx_antenna"
    VTX_KIT = "vtx_kit"
    CAMERA = "camera"
    GPS = "gps"
    CUSTOM_PART = "custom_part"

    @classmethod
    def to_yaml(cls, representer, node):
        return representer.represent_scalar(cls.yaml_tag, f"{node.name}")

    @classmethod
    def from_yaml(cls, constructor, node) -> "ComponentType":
        return cls[node.value]


@dataclass
class Component:

    name: str = "default_name"
    short_name: str = "default_name"
    mass: float = 0  # individual components have cost
    cost: float = 0  # individual components have mass
    number_of_units: int = 1
    component_type: ComponentType = ComponentType("undefined")


class Kit:

    name: str = "default_kit_name"
    short_name: str = "default_kit_short_name"
    cost: float = (
        0  # Kits have cost as a whole and individual component costs are ignored
    )
    number_of_units: int = 1

    component_type: ComponentType = ComponentType("undefined")

    def _get_components(self) -> list:
        return [p for p in vars(self) if isinstance(vars(self)[p], Component)]

    # Kits have mass which is the sum of their components' mass
    @property
    def mass(self) -> float:
        return sum(
            [
                getattr(self, p).mass * getattr(self, p).number_of_units
                for p in self._get_components()
            ]
        )
