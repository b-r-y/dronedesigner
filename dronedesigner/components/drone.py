from dataclasses import dataclass, field
from typing import ClassVar

from dronedesigner.components.battery import Battery
from dronedesigner.components.battery_strap import Battery_Strap
from dronedesigner.components.component import Component, Kit
from dronedesigner.components.frame import Frame
from dronedesigner.components.motor import Motor
from dronedesigner.components.propeller import Propeller
from dronedesigner.components.receiver import Receiver
from dronedesigner.components.receiver_antenna import Receiver_Antenna
from dronedesigner.components.stack import Stack
from dronedesigner.components.vtx_kit import VTX_Kit


@dataclass
class Drone:

    yaml_tag: ClassVar = "!Drone"

    battery: Battery = field(default_factory=Battery)
    battery_strap: Battery_Strap = field(default_factory=Battery_Strap)
    frame: Frame = field(default_factory=Frame)
    motor: Motor = field(default_factory=Motor)
    receiver: Receiver = field(default_factory=Receiver)
    stack: Stack = field(default_factory=Stack)
    propeller: Propeller = field(default_factory=Propeller)
    receiver_antenna: Receiver_Antenna = field(
        default_factory=Receiver_Antenna
    )
    vtx_kit: VTX_Kit = field(default_factory=VTX_Kit)

    def _get_components(self) -> list:
        return [
            p
            for p in vars(self)
            if isinstance(vars(self)[p], (Component, Kit))
        ]

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
    #     if self.frame.name != "default_name":
    #         self._update_frame()

    # def _update_frame(self) -> None:
    #     new_frame: Frame = load_component(
    #         filename="frames", component_name=self.frame.name
    #     )
    #     if new_frame:
    #         self.frame = new_frame
