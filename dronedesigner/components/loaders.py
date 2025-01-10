#!/usr/bin/env python3
from pathlib import Path

import ruamel.yaml

from dronedesigner.components.batteries import Battery
from dronedesigner.components.component_types import ComponentLike
from dronedesigner.components.drone import Drone
from dronedesigner.components.frames import Frame
from dronedesigner.components.motors import Motor
from dronedesigner.components.receivers import Receiver
from dronedesigner.components.stacks import Stack

components_path: Path = (
    Path(__file__).absolute().parent.parent / "components_data"
)

yaml = ruamel.yaml.YAML()
yaml.register_class(cls=Drone)
yaml.register_class(cls=Stack)
yaml.register_class(cls=Frame)
yaml.register_class(cls=Receiver)
yaml.register_class(cls=Motor)
yaml.register_class(cls=Battery)


@staticmethod
def list_components(objects_list: list[ComponentLike]) -> list[str]:
    components: list[str] = [component.name for component in objects_list]
    return components


@staticmethod
def list_components_with_short_name(
    objects_list: list[ComponentLike],
) -> list[str]:
    components: list[str] = [
        component.short_name for component in objects_list
    ]
    return components


@staticmethod
def load_components(filename: str) -> list[ComponentLike]:
    with open(
        file=f"{components_path / filename}.yaml", mode="r", encoding="utf-8"
    ) as file:
        return yaml.load(stream=file)


@staticmethod
def load_component(filename: str, component_name: str) -> ComponentLike:
    loaded_components: list[ComponentLike] = load_components(filename=filename)
    component: ComponentLike = [
        comp for comp in loaded_components if comp.name == component_name
    ][0]
    return component


@staticmethod
def load_drone(filename: str) -> Drone:
    # must be one drone design per file
    loaded_drone: Drone = load_components(filename=filename)[0]
    # if drone.frame.name != "default_name":
    #     new_frame: Frame = load_component(filename="frames",
    #                                       component_name=drone.frame.name)
    #     if new_frame:
    #         drone.frame = new_frame

    return loaded_drone


if __name__ == "__main__":

    # for component_type in ComponentType:
    #     if component_type == "frame":
    #         frames: list[Frame] = load_components(filename="frames")
    #         print(frames)
    #     elif component_type == "stack":
    #         stacks: list[Stack] = load_components(filename="stacks")
    #         print(stacks)
    #     elif component_type == "receiver":
    #         receivers: list[Receiver] = \
    #             load_components(filename="receivers")
    #         print(receivers)

    drone: Drone = load_drone(filename="drone")

    print(drone)
