from typing import TypeVar

import ruamel.yaml

from dronedesigner.components.battery import Battery
from dronedesigner.components.battery_strap import Battery_Strap
from dronedesigner.components.camera import Camera
from dronedesigner.components.component import Component, ComponentType, Kit
from dronedesigner.components.connector import Connector
from dronedesigner.components.custom_part import Custom_Part
from dronedesigner.components.drone import Drone
from dronedesigner.components.frame import Frame
from dronedesigner.components.motor import Motor
from dronedesigner.components.propeller import Propeller
from dronedesigner.components.receiver import Receiver
from dronedesigner.components.receiver_antenna import Receiver_Antenna
from dronedesigner.components.stack import Stack
from dronedesigner.components.vtx import VTX
from dronedesigner.components.vtx_antenna import VTX_Antenna
from dronedesigner.components.vtx_kit import VTX_Kit

ComponentLike = TypeVar(
    "ComponentLike", Drone, Component, Stack, Frame, Receiver
)


def get_yaml_structure() -> ruamel.yaml.YAML:
    yaml = ruamel.yaml.YAML()
    yaml.register_class(cls=Battery)
    yaml.register_class(cls=Battery_Strap)
    yaml.register_class(cls=Camera)
    yaml.register_class(cls=Component)
    yaml.register_class(cls=ComponentType)
    yaml.register_class(cls=Connector)
    yaml.register_class(cls=Custom_Part)
    yaml.register_class(cls=Drone)
    yaml.register_class(cls=Frame)
    yaml.register_class(cls=Motor)
    yaml.register_class(cls=Propeller)
    yaml.register_class(cls=Receiver)
    yaml.register_class(cls=Receiver_Antenna)
    yaml.register_class(cls=Stack)
    yaml.register_class(cls=VTX)
    yaml.register_class(cls=VTX_Antenna)
    yaml.register_class(cls=VTX_Kit)
    yaml.register_class(cls=Kit)

    return yaml
