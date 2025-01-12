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
    pass


def update_frame(name) -> None:
    drone.frame = load_component(filename="frames", component_name=name.new)
    update_mass_display()
    update_cost_display()


def update_stack(name) -> None:
    drone.stack = load_component(filename="stacks", component_name=name.new)
    update_mass_display()
    update_cost_display()


def update_receiver(name) -> None:
    drone.receiver = load_component(
        filename="receivers", component_name=name.new
    )
    update_mass_display()
    update_cost_display()


def update_motor(name) -> None:
    drone.motor = load_component(filename="motors", component_name=name.new)

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
frames_w.observe(handler=update_frame, names="value")


stacks_w = Dropdown(
    options=list_components(objects_list=load_components(filename="stacks")),
    value="Default Stack",
    description="Stack: ",
)
stacks_w.observe(handler=update_stack, names="value")

receivers_w = Dropdown(
    options=list_components(
        objects_list=load_components(filename="receivers")
    ),
    value="Default Receiver",
    description="Receiver: ",
)
receivers_w.observe(handler=update_receiver, names="value")

motors_w = Dropdown(
    options=list_components(objects_list=load_components(filename="motors")),
    value="Default Motor",
    description="Motor: ",
)
motors_w.observe(handler=update_motor, names="value")

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

outputs: list[Box] = [
    Box(
        children=[
            Label(value="Calculated mass: "),
            mass_value,
            Label(value="  [grams]"),
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
