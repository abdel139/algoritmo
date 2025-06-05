import streamlit.components.v1 as components
import os

_component_dir = os.path.dirname(os.path.abspath(__file__))
_build_path = os.path.join(_component_dir, "frontend")
print(_build_path)
my_component = components.declare_component(
    "my_component",
    path=_build_path
)
