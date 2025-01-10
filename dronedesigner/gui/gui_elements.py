from ipywidgets import Dropdown

from dronedesigner.components.loaders import list_components, load_components


def on_change(change) -> None:
    print(change.new)


frames_w = Dropdown(
    options=list_components(objects_list=load_components(filename="frames"))
)
frames_w.observe(handler=on_change, names="value")

stacks_w = Dropdown(
    options=list_components(objects_list=load_components(filename="stacks"))
)
stacks_w.observe(handler=on_change, names="value")

receivers_w = Dropdown(
    options=list_components(objects_list=load_components(filename="receivers"))
)
receivers_w.observe(handler=on_change, names="value")
