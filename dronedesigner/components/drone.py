from dataclasses import dataclass, field
from typing import ClassVar

from dronedesigner.components.batteries import Battery
from dronedesigner.components.component import Component, ComponentType
from dronedesigner.components.frames import Frame
from dronedesigner.components.motors import Motor
from dronedesigner.components.receivers import Receiver
from dronedesigner.components.stacks import Stack


@dataclass
class Drone:

    yaml_tag: ClassVar = "!Drone"

    frame: Frame = field(default_factory=Frame)
    stack: Stack = field(default_factory=Stack)
    receiver: Receiver = field(default_factory=Receiver)

    def _get_components(self) -> list:
        return [p for p in vars(self) if isinstance(vars(self)[p], Component)]

    def mass(self) -> float:
        return sum(
            [
                getattr(self, p).mass * getattr(self, p).number_of_units
                for p in self._get_components()
            ]
        )

    def cost(self) -> float:
        return sum(
            [
                getattr(self, p).cost * getattr(self, p).number_of_units
                for p in self._get_components()
            ]
        )


# def __post_init__(self) -> None:
#     if self.Frame.name != "default_name":
#         self._update_frame()

# def _update_frame(self) -> None:
#     new_frame: Frame = load_component(filename="frames",
#                                       component_name=self.Frame.name)
#     if new_frame:
#         self.Frame = new_frame
