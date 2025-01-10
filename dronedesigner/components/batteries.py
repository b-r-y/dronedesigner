from dataclasses import dataclass
from typing import ClassVar

from dronedesigner.components.component import Component, ComponentType


@dataclass
class Battery(Component):

    yaml_tag: ClassVar = "!Battery"

    component_type: ComponentType = ComponentType("battery")


if __name__ == "__main__":
    import ruamel.yaml
    from loaders import load_component, load_components

    yaml = ruamel.yaml.YAML()

    motors: list[Battery] = load_components(filename="batteries")

    selected_frame: Battery = load_component(
        filename="batteries",
        component_name="Tattu R-Line Version 5.0 1400mAh 6S 150C 22.2V Lipo Battery Pack with XT60 Plug",
    )

    with open("battteries_new.yaml", mode="w", encoding="utf-8") as file:
        yaml.dump(data=motors, stream=file)  # type: ignore

    print(motors)
