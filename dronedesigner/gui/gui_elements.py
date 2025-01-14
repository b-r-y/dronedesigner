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
    update_mass_display()
    update_cost_display()


def update_motor_count(name) -> None:
    drone.motor.number_of_units = int(name.new)
    update_mass_display()
    update_cost_display()


form_item_layout = Layout(
    display="flex", flex_flow="row", justify_content="space-between"
)

frames_w = Dropdown(
    options=list_components(objects_list=load_components(filename="frames")),
    value="Default Frame",
    description="Frame: ",
)
frames_w.observe(
    handler=partial(update_drone, "frame", "frames"), names="value"
)


stacks_w = Dropdown(
    options=list_components(objects_list=load_components(filename="stacks")),
    value="Default Stack",
    description="Stack: ",
)
stacks_w.observe(
    handler=partial(update_drone, "stack", "stacks"), names="value"
)

receivers_w = Dropdown(
    options=list_components(
        objects_list=load_components(filename="receivers")
    ),
    value="Default Receiver",
    description="Receiver: ",
)
receivers_w.observe(
    handler=partial(update_drone, "receiver", "receivers"), names="value"
)

motors_w = Dropdown(
    options=list_components(objects_list=load_components(filename="motors")),
    value="Default Motor",
    description="Motor: ",
)
motors_w.observe(
    handler=partial(update_drone, "motor", "motors"), names="value"
)

motor_count_w = Dropdown(
    options=["1", "2", "3", "4"],
    value="4",
    description="No: ",
)
motor_count_w.observe(handler=update_motor_count, names="value")

selections: list[Box] = [
    Box(
        children=[Label(value="Drone:")],
        layout=form_item_layout,
    ),
    Box(
        children=[
            frames_w,
        ],
        layout=form_item_layout,
    ),
    Box(
        children=[
            stacks_w,
        ],
        layout=form_item_layout,
    ),
    Box(
        children=[
            receivers_w,
        ],
        layout=form_item_layout,
    ),
    Box(children=[motors_w, motor_count_w], layout=form_item_layout),
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
            Label(value="Calculated mass: "),
            mass_value,
            Label(value="  [grams]"),
        ],
        layout=form_item_layout,
    ),
    Box(
        children=[
            Label(value="Calculated cost: "),
            cost_value,
            Label(value="  [DKK]"),
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
