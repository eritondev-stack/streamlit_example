import os
import streamlit.components.v1 as components

_USE_WEB_DEV_SERVER = False

if _USE_WEB_DEV_SERVER:
    _component_func = components.declare_component(
        "component1", url="http://localhost:3001"
    )
else:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    #print("Caminho: " + build_dir)
    _component_func = components.declare_component("component1", path=build_dir)


def component1_events(nome, key):
    component_value = _component_func(spec=nome, default=None, key=key)
    return component_value
