import sys
from pathlib import Path, PurePath

# Add the parent directory to the path so that the module can be found
sys.path.insert(0, str(Path(__file__).parents[1]))

import ruamel.yaml

from dronedesigner.components.component import ComponentType
from dronedesigner.components.drone import Drone
from dronedesigner.components.frames import Frame
from dronedesigner.components.loaders import load_component, load_components
from dronedesigner.components.motors import Component

output_path: PurePath = PurePath("output")

yaml = ruamel.yaml.YAML()
yaml.register_class(cls=Drone)
# yaml.register_class(cls=Stack)
yaml.register_class(cls=ComponentType)
yaml.register_class(cls=Component)
yaml.register_class(cls=Frame)
# yaml.register_class(cls=Receiver)
# yaml.register_class(cls=Motor)
# yaml.register_class(cls=Battery)

drone: list = load_components(
    filename="drone"
)  # loads a deafult drone design stored in drone.yaml

with open(
    file=output_path / "drone_new.yaml", mode="w", encoding="utf-8"
) as file:
    yaml.dump(
        data=drone, stream=file
    )  # dumps the default drone into a new file.

print(drone[0].mass())  # print the mass of the drone

drone[0].frame = load_component(
    filename="frames", component_name="Source One V5 5inch"
)  # assign frame to drone
drone[0].frame.arms_spacer = 8  # change frame parameter
drone[0].stack = load_component(
    filename="stacks",
    component_name="SpeedyBee F405 V4 BLS 60A 30x30 FC&ESC Stack",
)  # assign stack to drone
drone[0].receiver = load_component(
    filename="receivers",
    component_name="RP4TD ExpressLRS 2.4GHz True Diversity Receiver",
)  # assign receiver to drone
drone[0].motor = load_component(
    filename="motors", component_name="XING2 2207 4S 6S FPV Motor"
)  # assign receiver to drone
drone[0].battery = load_component(
    filename="batteries",
    component_name="Tattu R-Line Version 5.0 1400mAh 6S 150C 22.2V Lipo Battery Pack with XT60 Plug",
)  # assign receiver to drone

print(drone[0].mass())  # print the mass of the drone
print(drone[0].cost())  # print the mass of the drone

with open(
    file=output_path / "drone_new_new.yaml", mode="w", encoding="utf-8"
) as file:
    yaml.dump(data=drone[0], stream=file)  # dump the result to a new file

# loaded_drone = load_drone("drone_new_new")  # load the new drone

new_drone: Drone = Drone()
with open(
    file=output_path / "default_drone.yaml", mode="w", encoding="utf-8"
) as file:
    yaml.dump(data=new_drone, stream=file)  # dump the result to a new file

with open(
    file=output_path / "drone_new_new.yaml", mode="r", encoding="utf-8"
) as file:
    newer_drone: Drone = yaml.load(stream=file)

    b = 1

a = 1
