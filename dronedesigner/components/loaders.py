#!/usr/bin/env python3
from pathlib import Path

from dronedesigner.components.component_types import (
    ComponentLike,
    get_yaml_structure,
)
from dronedesigner.components.drone import Drone

components_path: Path = (
    Path(__file__).absolute().parent.parent / "components_data"
)


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
        return get_yaml_structure().load(stream=file)


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
