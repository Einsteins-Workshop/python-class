from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import sys
from enum import Enum
from typing import Optional

app = Ursina()

player = FirstPersonController()
editor_camera = None

app_sky = Sky()

platform = Entity(collider="box", model="cube", texture="white_cube")
blocks = []


class State(Enum):
    EDITOR = "editor"
    PLAYER = "player"


print(f'Initializing States: {State._member_names_}')

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


def correct_world_point(world_point: Vec3) -> Vec3:
    return Vec3(int(round(world_point.x)), int(round(world_point.y)), int(round(world_point.z)))


def input(key: str) -> None:  # type: ignore
    if key == "escape":
        sys.exit()
    elif key == "c":
        toggle_state()
    elif key == "left mouse down" and state == State.EDITOR:
        if mouse.world_point is not None:
            hit_pos: Vec3 = (mouse.world_point + (mouse.normal or Vec3(0, 0, 0)) * 0.5) or Vec3(0, 0, 0)
            corrected_world_point = correct_world_point(hit_pos)

            blocks.append(Entity(position=corrected_world_point, texture='white_cube', collider='box', model='cube'))
    elif key == "middle mouse down":
        hovered_entity: Optional[Entity] = mouse.hovered_entity

        if hovered_entity:
            if hovered_entity in blocks:
                blocks.remove(hovered_entity)

            destroy(hovered_entity)


# TODO: Make ursina.ico

app.run(info=False)