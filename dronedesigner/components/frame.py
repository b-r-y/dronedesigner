from dataclasses import dataclass
from typing import ClassVar

from dronedesigner.components.component import Component, ComponentType


@dataclass
class Frame(Component):

    yaml_tag: ClassVar = "!Frame"

    component_type: ComponentType = ComponentType("frame")
    arms_spacer: float = 6


if __name__ == "__main__":
    import ruamel.yaml
    from loaders import load_component, load_components

    yaml = ruamel.yaml.YAML()
    yaml.register_class(cls=Frame)

    frames: list[Frame] = load_components(filename="frames")

    selected_frame: Frame = load_component(
        filename="frames", component_name="Source One V5 5inch"
    )

    with open("frames_new.yaml", mode="w", encoding="utf-8") as file:
        yaml.dump(data=frames, stream=file)

    new_frame: Frame = Frame()

    with open("default_frame.yaml", mode="w", encoding="utf-8") as file:
        yaml.dump(data=new_frame, stream=file)

    print(frames)
