import sys
from pathlib import Path, PurePath

import ruamel.yaml

# Add the parent directory to the path so that the module can be found
sys.path.insert(0, str(Path(__file__).parents[1]))

from dronedesigner.components.component_types import get_yaml_structure
from dronedesigner.components.drone import Drone
from dronedesigner.components.loaders import (
    components_path,
    load_component,
    load_components,
)

output_path: PurePath = PurePath("output")
yaml: ruamel.yaml.YAML = get_yaml_structure()

## Create a new default drone
drone: Drone = Drone()
# save the default drone to a file
with open(
    file=output_path / "default_drone.yaml", mode="w", encoding="utf-8"
) as file:
    yaml.dump(data=drone, stream=file)  # dump the result to a new file
# Load the default drone from the file
with open(
    file=output_path / "default_drone.yaml", mode="r", encoding="utf-8"
) as file:
    loaded_drone: Drone = yaml.load(stream=file)
    assert loaded_drone == drone
    with open(
        file=components_path / "drone.yaml", mode="w", encoding="utf-8"
    ) as file:
        yaml.dump(data=[loaded_drone], stream=file)
    loaded_drone = load_components(filename="drone")[0]
    assert loaded_drone == drone

# Print some infromation about the drone
print(f"Default drone mass: {drone.mass()}")
print(f"Default drone cost: {drone.cost()}")

# Load some real components
drone.battery = load_component(
    filename="batteries",
    component_name="Tattu R-Line Version 5.0 1400mAh 6S 150C 22.2V Lipo Battery Pack with XT60 Plug",
)
drone.frame = load_component(
    filename="frames", component_name="Source One V5 5inch"
)
drone.frame.arms_spacer = 8
drone.stack = load_component(
    filename="stacks",
    component_name="SpeedyBee F405 V4 BLS 60A 30x30 FC&ESC Stack",
)
drone.propeller = load_component(
    filename="propellers", component_name="HQ Holdbar prop 5X4.8X3V1S"
)
drone.propeller.number_of_units = 4
drone.receiver = load_component(
    filename="receivers",
    component_name="RP4TD ExpressLRS 2.4GHz True Diversity Receiver",
)
drone.motor = load_component(
    filename="motors", component_name="XING2 2207 4S 6S FPV Motor"
)
drone.motor.number_of_units = 4
drone.vtx_kit = load_component(
    filename="vtx_kits",
    component_name="Walksnail Avatar HD Pro Kit (Dual Antennas Version)",
)
drone.battery_strap = load_component(
    filename="battery_straps",
    component_name="Bronto Hook and Loop",
)
drone.battery_strap.number_of_units = 2
drone.receiver_antenna = load_component(
    filename="receiver_antennas",
    component_name="Sequre Antenna",
)
drone.receiver_antenna.number_of_units = 2
drone.rear_holder = load_component(
    filename="custom_parts",
    component_name="5 Inch rear dual RX & VTX antennas mount with XT60 holder",
)
drone.arm_guards = load_component(
    filename="custom_parts",
    component_name="5 Inch arm guard",
)
drone.arm_guards.number_of_units = 4
drone.front_bumper = load_component(
    filename="custom_parts",
    component_name="5 Inch front bumper",
)
drone.cap_holder = load_component(
    filename="custom_parts",
    component_name="5 Inch cap and rx holder",
)
drone.motors_connectors_female = load_component(
    filename="connectors",
    component_name="MR30-FB",
)
drone.motors_connectors_female.number_of_units = 4
drone.motors_connectors_male = load_component(
    filename="connectors",
    component_name="MR30-M",
)
drone.motors_connectors_male.number_of_units = 4
drone.battery_connector = load_component(
    filename="connectors",
    component_name="XT60H-M",
)

# Print some infromation about the drone again
print(f"Drone mass: {drone.mass()}")
print(f"Drone cost: {drone.cost()}")

with open(
    file=output_path / "new_drone.yaml", mode="w", encoding="utf-8"
) as file:
    yaml.dump(data=drone, stream=file)  # dump the result to a new file
