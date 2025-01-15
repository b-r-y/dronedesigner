from functools import partial

from ipywidgets import Box, Dropdown, Label, Layout, Text

from dronedesigner.components.drone import Drone
from dronedesigner.components.loaders import (
    list_components,
    load_component,
    load_components,
)

drone = Drone()


def update_mass_display() -> None:
    mass_value.value = str(drone.mass())


def update_cost_display() -> None:
    cost_value.value = str(drone.cost())


def update_drone(component: str, source_file: str, value) -> None:
    new_component = load_component(
        filename=source_file, component_name=value.new
    )
    setattr(drone, component, new_component)
    if component == "motor":
        drone.motor.number_of_units = 4
    if component == "propeller":
        drone.propeller.number_of_units = 4
    if component == "battery_strap":
        drone.battery_strap.number_of_units = 2
    update_mass_display()
    update_cost_display()


form_item_layout = Layout(
    display="flex",
    flex_flow="row",
    justify_content="space-between",
)

frames_w = Dropdown(
    options=list_components(objects_list=load_components(filename="frames")),
    value="Default Frame",
    description="",
)
frames_w.observe(
    handler=partial(update_drone, "frame", "frames"), names="value"
)

stacks_w = Dropdown(
    options=list_components(objects_list=load_components(filename="stacks")),
    value="Default Stack",
    description="",
)
stacks_w.observe(
    handler=partial(update_drone, "stack", "stacks"), names="value"
)

receivers_w = Dropdown(
    options=list_components(
        objects_list=load_components(filename="receivers")
    ),
    value="Default Receiver",
    description="",
)
receivers_w.observe(
    handler=partial(update_drone, "receiver", "receivers"), names="value"
)

receiver_antennas_w = Dropdown(
    options=list_components(
        objects_list=load_components(filename="receiver_antennas")
    ),
    value="Default Receiver Antenna",
    description="",
)
receiver_antennas_w.observe(
    handler=partial(update_drone, "receiver_antenna", "receiver_antennas"),
    names="value",
)

motors_w = Dropdown(
    options=list_components(objects_list=load_components(filename="motors")),
    value="Default Motor",
    description="",
)
motors_w.observe(
    handler=partial(update_drone, "motor", "motors"), names="value"
)

propellers_w = Dropdown(
    options=list_components(
        objects_list=load_components(filename="propellers")
    ),
    value="Default Properller",
    description="",
)
propellers_w.observe(
    handler=partial(update_drone, "propeller", "propellers"), names="value"
)

batteries_w = Dropdown(
    options=list_components(
        objects_list=load_components(filename="batteries")
    ),
    value="Default Battery",
    description="",
)
batteries_w.observe(
    handler=partial(update_drone, "battery", "batteries"), names="value"
)

battery_straps_w = Dropdown(
    options=list_components(
        objects_list=load_components(filename="battery_straps")
    ),
    value="Default Battery Strap",
    description="",
)
battery_straps_w.observe(
    handler=partial(update_drone, "battery_strap", "battery_straps"),
    names="value",
)

vtx_kits_w = Dropdown(
    options=list_components(objects_list=load_components(filename="vtx_kits")),
    value="Default VTX Kit",
    description="",
)
vtx_kits_w.observe(
    handler=partial(update_drone, "vtx", "vtx_kits"), names="value"
)

selections: list[Box] = [
    Box(children=[Label(value="Drone:")], layout=form_item_layout),
    Box(
        children=[Label(value="Battery: "), batteries_w],
        layout=form_item_layout,
    ),
    Box(
        children=[Label(value="Battery Straps (x2): "), battery_straps_w],
        layout=form_item_layout,
    ),
    Box(
        children=[Label(value="Frame: "), frames_w],
        layout=form_item_layout,
    ),
    Box(
        children=[Label(value="Stack: "), stacks_w],
        layout=form_item_layout,
    ),
    Box(
        children=[Label(value="Receiver: "), receivers_w],
        layout=form_item_layout,
    ),
    Box(
        children=[Label(value="Receiver Antenna: "), receiver_antennas_w],
        layout=form_item_layout,
    ),
    Box(
        children=[Label(value="Motor: "), motors_w],
        layout=form_item_layout,
    ),
    Box(
        children=[Label(value="Properller: "), propellers_w],
        layout=form_item_layout,
    ),
    Box(
        children=[Label(value="VTX Kit: "), vtx_kits_w],
        layout=form_item_layout,
    ),
]

mass_value: Text = Text(
    value="0",
    placeholder="This is the total calculated mass of the drone",
    description="",
)

cost_value: Text = Text(
    value="0",
    placeholder="This is the total calculated cost of the drone",
    description="",
)

outputs: list[Box] = [
    Box(
        children=[
            Label(value="Calculated mass [gram]: "),
            mass_value,
        ],
        layout=form_item_layout,
    ),
    Box(
        children=[
            Label(value="Calculated cost [DKK]: "),
            cost_value,
        ],
        layout=form_item_layout,
    ),
]

selection_pane = Box(
    children=selections,
    layout=Layout(
        display="flex",
        flex_flow="column",
        border="solid 2px",
        align_items="stretch",
        width="33%",
    ),
)

output_data_pane = Box(
    children=outputs,
    layout=Layout(
        display="flex",
        flex_flow="column",
        border="solid 2px",
        align_items="stretch",
        width="50%",
    ),
)

drone_designer = Box(children=[selection_pane, output_data_pane])
