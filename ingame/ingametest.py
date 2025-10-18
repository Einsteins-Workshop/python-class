from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import sys
from enum import Enum
import math

app = Ursina()

player = FirstPersonController()
editor_camera = None

shift_clicked = False
app_sky = Sky()

Entity(collider="box", model="cube", texture="white_cube")


class State(Enum):
    EDITOR = "editor"
    PLAYER = "player"


state = State.PLAYER


def update_editor_state() -> None:
    global state, editor_camera, player

    if state == State.PLAYER:
        destroy(editor_camera)
        player = FirstPersonController()
    elif state == State.EDITOR:
        destroy(player)
        editor_camera = EditorCamera()


def toggle_state() -> None:
    global state

    state = State.EDITOR if state == State.PLAYER else State.PLAYER
    update_editor_state()


def update() -> None:
    pass


def input(key: str) -> None:
    if key == "escape":
        sys.exit()
    elif key == "c":
        toggle_state()
    elif key == "left mouse down" and mouse.world_point is not None and state == State.EDITOR:
        Entity(position=mouse.world_point, texture='white_cube', collider='box', model='cube')


app.run()
