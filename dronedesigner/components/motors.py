from dataclasses import dataclass
from typing import ClassVar

from dronedesigner.components.component import Component, ComponentType


@dataclass
class Motor(Component):

    yaml_tag: ClassVar = "!Motor"

    component_type: ComponentType = ComponentType("motor")
    number_of_units: int = 4


if __name__ == "__main__":
    import ruamel.yaml

    from dronedesigner.components.loaders import (
        load_component,
        load_components,
    )

    yaml = ruamel.yaml.YAML()

    motors: list[Motor] = load_components(filename="motors")

    selected_frame: Motor = load_component(
        filename="motors", component_name="XING2 2207 4S 6S FPV Motor"
    )

    with open("motors_new.yaml", mode="w", encoding="utf-8") as file:
        yaml.dump(data=motors, stream=file)  # type: ignore

    print(motors)
