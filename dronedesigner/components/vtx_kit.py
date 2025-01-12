from dataclasses import dataclass, field
from typing import ClassVar

from dronedesigner.components.camera import Camera
from dronedesigner.components.component import ComponentType, Kit
from dronedesigner.components.vtx import VTX
from dronedesigner.components.vtx_antenna import VTX_Antenna


@dataclass
class VTX_Kit(Kit):

    yaml_tag: ClassVar = "!VTX_Kit"

    component_type: ComponentType = ComponentType("vtx_kit")

    camera: Camera = field(default_factory=Camera)
    vtx: VTX = field(default_factory=VTX)
    vtx_antenna: VTX_Antenna = field(default_factory=VTX_Antenna)
