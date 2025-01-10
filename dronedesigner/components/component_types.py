from typing import TypeVar

from dronedesigner.components.component import Component
from dronedesigner.components.drone import Drone
from dronedesigner.components.frames import Frame
from dronedesigner.components.receivers import Receiver
from dronedesigner.components.stacks import Stack

ComponentLike = TypeVar(
    "ComponentLike", Drone, Component, Stack, Frame, Receiver
)
