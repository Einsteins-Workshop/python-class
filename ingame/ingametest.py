from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import json
import sys

app = Ursina()
player = FirstPersonController()

# EditorCamera()
app_sky = Sky()

Entity(collider="box", model="cube", texture="white_cube")


def load() -> None:
    global app_sky

    with open("project.json", "r") as f:
        data = json.load(f)
        f.close()

    if data.get("sky") is not None:
        sky: dict = data.get("sky")
        if isinstance(sky, dict) and sky.get("texture"):
            app_sky.texture = str(sky.get("texture"))


def update() -> None:
    pass


def input(key: str) -> None:
    if key == "escape":
        sys.exit()
    elif key == "`":
        load()


app.run()
