"""
ABS Engine - A GUI-based First Person Game Engine for Panda3D
Creates compiled first-person games with WASD controls
"""

import tkinter as tk
from tkinter import ttk, messagebox, colorchooser, filedialog
import json
import os


class ABSEngine:
    def __init__(self, root):
        self.root = root
        self.root.title("ABS Engine - First Person Game Editor")
        self.root.geometry("1000x700")

        # Game configuration
        self.config = {
            'title': 'My First Person Game',
            'window_size': [800, 600],
            'background_color': [0.5, 0.7, 1.0, 1.0],
            'move_speed': 10.0,
            'mouse_sensitivity': 0.2,
            'objects': [],
            'player_start': [0, 0, 0]
        }

        self.setup_ui()

    def setup_ui(self):
        # Menu bar
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New Project", command=self.new_project)
        file_menu.add_command(label="Load Project", command=self.load_project)
        file_menu.add_command(label="Save Project", command=self.save_project)
        file_menu.add_separator()
        file_menu.add_command(label="Export Game", command=self.export_game)

        # Main container
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Left panel - Settings
        left_frame = ttk.LabelFrame(main_frame, text="Game Settings", padding="10")
        left_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=5)

        # Game title
        ttk.Label(left_frame, text="Game Title:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.title_var = tk.StringVar(value=self.config['title'])
        ttk.Entry(left_frame, textvariable=self.title_var, width=30).grid(row=0, column=1, pady=5)

        # Window size
        ttk.Label(left_frame, text="Window Width:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.width_var = tk.IntVar(value=self.config['window_size'][0])
        ttk.Spinbox(left_frame, from_=640, to=1920, textvariable=self.width_var, width=28).grid(row=1, column=1, pady=5)

        ttk.Label(left_frame, text="Window Height:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.height_var = tk.IntVar(value=self.config['window_size'][1])
        ttk.Spinbox(left_frame, from_=480, to=1080, textvariable=self.height_var, width=28).grid(row=2, column=1,
                                                                                                 pady=5)

        # Movement speed
        ttk.Label(left_frame, text="Move Speed:").grid(row=3, column=0, sticky=tk.W, pady=5)
        self.speed_var = tk.DoubleVar(value=self.config['move_speed'])
        ttk.Spinbox(left_frame, from_=1.0, to=50.0, increment=0.5, textvariable=self.speed_var, width=28).grid(row=3,
                                                                                                               column=1,
                                                                                                               pady=5)

        # Mouse sensitivity
        ttk.Label(left_frame, text="Mouse Sensitivity:").grid(row=4, column=0, sticky=tk.W, pady=5)
        self.sensitivity_var = tk.DoubleVar(value=self.config['mouse_sensitivity'])
        ttk.Spinbox(left_frame, from_=0.1, to=1.0, increment=0.05, textvariable=self.sensitivity_var, width=28).grid(
            row=4, column=1, pady=5)

        # Background color
        ttk.Label(left_frame, text="Sky Color:").grid(row=5, column=0, sticky=tk.W, pady=5)
        self.color_button = ttk.Button(left_frame, text="Choose Color", command=self.choose_color)
        self.color_button.grid(row=5, column=1, pady=5, sticky=tk.W)

        # Player start position
        ttk.Label(left_frame, text="Player Start Position:", font=('', 10, 'bold')).grid(row=6, column=0, columnspan=2,
                                                                                         sticky=tk.W, pady=(10, 5))

        pos_frame = ttk.Frame(left_frame)
        pos_frame.grid(row=7, column=0, columnspan=2, pady=5)

        ttk.Label(pos_frame, text="X:").grid(row=0, column=0)
        self.start_x = tk.DoubleVar(value=0)
        ttk.Spinbox(pos_frame, from_=-100, to=100, textvariable=self.start_x, width=8).grid(row=0, column=1, padx=2)

        ttk.Label(pos_frame, text="Y:").grid(row=0, column=2)
        self.start_y = tk.DoubleVar(value=0)
        ttk.Spinbox(pos_frame, from_=-100, to=100, textvariable=self.start_y, width=8).grid(row=0, column=3, padx=2)

        ttk.Label(pos_frame, text="Z:").grid(row=0, column=4)
        self.start_z = tk.DoubleVar(value=0)
        ttk.Spinbox(pos_frame, from_=-100, to=100, textvariable=self.start_z, width=8).grid(row=0, column=5, padx=2)

        # Right panel - Objects
        right_frame = ttk.LabelFrame(main_frame, text="Scene Objects", padding="10")
        right_frame.grid(row=0, column=1, sticky=(tk.W, tk.E, tk.N, tk.S), padx=5)

        # Object list
        self.object_listbox = tk.Listbox(right_frame, height=15, width=40)
        self.object_listbox.grid(row=0, column=0, columnspan=2, pady=5, sticky=(tk.W, tk.E))

        # Object buttons
        ttk.Button(right_frame, text="Add Cube", command=lambda: self.add_object('cube')).grid(row=1, column=0, pady=5,
                                                                                               sticky=tk.W)
        ttk.Button(right_frame, text="Add Sphere", command=lambda: self.add_object('sphere')).grid(row=1, column=1,
                                                                                                   pady=5, sticky=tk.W)
        ttk.Button(right_frame, text="Add Ground Plane", command=lambda: self.add_object('plane')).grid(row=2, column=0,
                                                                                                        pady=5,
                                                                                                        sticky=tk.W)
        ttk.Button(right_frame, text="Remove Selected", command=self.remove_object).grid(row=2, column=1, pady=5,
                                                                                         sticky=tk.W)

        # Object properties
        ttk.Label(right_frame, text="Selected Object Properties:", font=('', 9, 'bold')).grid(row=3, column=0,
                                                                                              columnspan=2,
                                                                                              pady=(15, 5))

        props_frame = ttk.Frame(right_frame)
        props_frame.grid(row=4, column=0, columnspan=2, pady=5)

        ttk.Label(props_frame, text="Position X:").grid(row=0, column=0, sticky=tk.W)
        self.obj_x = tk.DoubleVar(value=0)
        ttk.Entry(props_frame, textvariable=self.obj_x, width=10).grid(row=0, column=1, padx=5)

        ttk.Label(props_frame, text="Y:").grid(row=0, column=2)
        self.obj_y = tk.DoubleVar(value=0)
        ttk.Entry(props_frame, textvariable=self.obj_y, width=10).grid(row=0, column=3, padx=5)

        ttk.Label(props_frame, text="Z:").grid(row=0, column=4)
        self.obj_z = tk.DoubleVar(value=0)
        ttk.Entry(props_frame, textvariable=self.obj_z, width=10).grid(row=0, column=5, padx=5)

        ttk.Label(props_frame, text="Scale:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.obj_scale = tk.DoubleVar(value=1.0)
        ttk.Entry(props_frame, textvariable=self.obj_scale, width=10).grid(row=1, column=1, padx=5, pady=5)

        ttk.Button(props_frame, text="Update Object", command=self.update_object).grid(row=2, column=0, columnspan=6,
                                                                                       pady=10)

        # Export button
        export_frame = ttk.Frame(main_frame)
        export_frame.grid(row=1, column=0, columnspan=2, pady=20)

        ttk.Button(export_frame, text="🎮 Export Standalone Game", command=self.export_game,
                   style='Accent.TButton').pack(pady=10)

        # Bind listbox selection
        self.object_listbox.bind('<<ListboxSelect>>', self.on_object_select)

        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(0, weight=1)

    def choose_color(self):
        color = colorchooser.askcolor(title="Choose Sky Color")
        if color[0]:
            r, g, b = [c / 255.0 for c in color[0]]
            self.config['background_color'] = [r, g, b, 1.0]
            messagebox.showinfo("Color Set", f"Sky color updated to RGB({r:.2f}, {g:.2f}, {b:.2f})")

    def add_object(self, obj_type):
        obj_id = len(self.config['objects'])
        obj = {
            'id': obj_id,
            'type': obj_type,
            'position': [0, 10, 0],
            'scale': 1.0
        }
        self.config['objects'].append(obj)
        self.object_listbox.insert(tk.END, f"{obj_type.capitalize()} {obj_id}")

    def remove_object(self):
        selection = self.object_listbox.curselection()
        if selection:
            idx = selection[0]
            self.config['objects'].pop(idx)
            self.object_listbox.delete(idx)
            self.refresh_object_list()

    def on_object_select(self, event):
        selection = self.object_listbox.curselection()
        if selection:
            idx = selection[0]
            obj = self.config['objects'][idx]
            self.obj_x.set(obj['position'][0])
            self.obj_y.set(obj['position'][1])
            self.obj_z.set(obj['position'][2])
            self.obj_scale.set(obj['scale'])

    def update_object(self):
        selection = self.object_listbox.curselection()
        if selection:
            idx = selection[0]
            self.config['objects'][idx]['position'] = [
                self.obj_x.get(),
                self.obj_y.get(),
                self.obj_z.get()
            ]
            self.config['objects'][idx]['scale'] = self.obj_scale.get()
            messagebox.showinfo("Updated", "Object properties updated!")

    def refresh_object_list(self):
        self.object_listbox.delete(0, tk.END)
        for i, obj in enumerate(self.config['objects']):
            self.object_listbox.insert(tk.END, f"{obj['type'].capitalize()} {i}")

    def new_project(self):
        if messagebox.askyesno("New Project", "Create a new project? Unsaved changes will be lost."):
            self.config = {
                'title': 'My First Person Game',
                'window_size': [800, 600],
                'background_color': [0.5, 0.7, 1.0, 1.0],
                'move_speed': 10.0,
                'mouse_sensitivity': 0.2,
                'objects': [],
                'player_start': [0, 0, 0]
            }
            self.refresh_object_list()
            messagebox.showinfo("Success", "New project created!")

    def save_project(self):
        filename = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("ABS Project", "*.json")]
        )
        if filename:
            self.update_config()
            with open(filename, 'w') as f:
                json.dump(self.config, f, indent=2)
            messagebox.showinfo("Success", f"Project saved to {filename}")

    def load_project(self):
        filename = filedialog.askopenfilename(
            filetypes=[("ABS Project", "*.json")]
        )
        if filename:
            with open(filename, 'r') as f:
                self.config = json.load(f)
            self.refresh_object_list()
            messagebox.showinfo("Success", "Project loaded!")

    def update_config(self):
        self.config['title'] = self.title_var.get()
        self.config['window_size'] = [self.width_var.get(), self.height_var.get()]
        self.config['move_speed'] = self.speed_var.get()
        self.config['mouse_sensitivity'] = self.sensitivity_var.get()
        self.config['player_start'] = [self.start_x.get(), self.start_y.get(), self.start_z.get()]

    def export_game(self):
        directory = filedialog.askdirectory(title="Select Export Directory")
        if not directory:
            return

        self.update_config()

        # Create game directory
        game_dir = os.path.join(directory, self.config['title'].replace(' ', '_'))
        os.makedirs(game_dir, exist_ok=True)

        # Generate game code
        game_code = self.generate_game_code()

        # Write main game file
        with open(os.path.join(game_dir, 'main.py'), 'w') as f:
            f.write(game_code)

        # Write config file
        with open(os.path.join(game_dir, 'config.json'), 'w') as f:
            json.dump(self.config, f, indent=2)

        # Create run script
        run_script = "#!/usr/bin/env python3\nimport subprocess\nimport sys\n\nsubprocess.run([sys.executable, 'main.py'])\n"
        with open(os.path.join(game_dir, 'run_game.py'), 'w') as f:
            f.write(run_script)

        messagebox.showinfo("Export Complete",
                            f"Game exported to:\n{game_dir}\n\nRun 'python main.py' to play!\n\n" +
                            "Make sure Panda3D is installed:\npip install panda3d")

    def generate_game_code(self):
        code = f'''"""
{self.config['title']}
Generated by ABS Engine
"""

from direct.showbase.ShowBase import ShowBase
from panda3d.core import Vec3, WindowProperties
from direct.task import Task
import json
import sys

class FirstPersonGame(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        # Load configuration
        try:
            with open('config.json', 'r') as f:
                self.config = json.load(f)
        except:
            print("Error: config.json not found!")
            sys.exit(1)

        # Set window properties
        props = WindowProperties()
        props.setTitle(self.config['title'])
        props.setSize(self.config['window_size'][0], self.config['window_size'][1])
        self.win.requestProperties(props)

        # Set background color
        bg = self.config['background_color']
        self.setBackgroundColor(bg[0], bg[1], bg[2])

        # Disable default mouse camera control
        self.disableMouse()

        # Player properties
        self.player_pos = Vec3(*self.config['player_start'])
        self.heading = 0
        self.pitch = 0
        self.move_speed = self.config['move_speed']
        self.mouse_sensitivity = self.config['mouse_sensitivity']

        # Set camera position
        self.camera.setPos(self.player_pos)
        self.camera.setHpr(self.heading, self.pitch, 0)

        # Movement keys
        self.keys = {{
            'w': False,
            'a': False,
            's': False,
            'd': False,
            'space': False,
            'shift': False
        }}

        self.setup_controls()
        self.create_scene()

        # Add movement task
        self.taskMgr.add(self.update, 'update')

        # Center and hide mouse
        props = WindowProperties()
        props.setCursorHidden(True)
        props.setMouseMode(WindowProperties.M_relative)
        self.win.requestProperties(props)

    def setup_controls(self):
        self.accept('w', self.set_key, ['w', True])
        self.accept('w-up', self.set_key, ['w', False])
        self.accept('a', self.set_key, ['a', True])
        self.accept('a-up', self.set_key, ['a', False])
        self.accept('s', self.set_key, ['s', True])
        self.accept('s-up', self.set_key, ['s', False])
        self.accept('d', self.set_key, ['d', True])
        self.accept('d-up', self.set_key, ['d', False])
        self.accept('space', self.set_key, ['space', True])
        self.accept('space-up', self.set_key, ['space', False])
        self.accept('shift', self.set_key, ['shift', True])
        self.accept('shift-up', self.set_key, ['shift', False])
        self.accept('escape', sys.exit)

    def set_key(self, key, value):
        self.keys[key] = value

    def create_scene(self):
        # Create objects from config
        for obj in self.config['objects']:
            if obj['type'] == 'cube':
                model = self.loader.loadModel('models/box')
            elif obj['type'] == 'sphere':
                model = self.loader.loadModel('models/sphere')
            elif obj['type'] == 'plane':
                model = self.loader.loadModel('models/box')
                model.setScale(obj['scale'] * 10, obj['scale'] * 10, 0.1)
                model.setPos(*obj['position'])
                model.reparentTo(self.render)
                continue

            model.setScale(obj['scale'])
            model.setPos(*obj['position'])
            model.reparentTo(self.render)

    def update(self, task):
        dt = globalClock.getDt()

        # Mouse look
        if self.mouseWatcherNode.hasMouse():
            md = self.win.getPointer(0)
            x = md.getX()
            y = md.getY()

            centerX = self.win.getProperties().getXSize() // 2
            centerY = self.win.getProperties().getYSize() // 2

            self.heading -= (x - centerX) * self.mouse_sensitivity
            self.pitch -= (y - centerY) * self.mouse_sensitivity

            # Clamp pitch
            self.pitch = max(-89, min(89, self.pitch))

            # Reset mouse to center
            self.win.movePointer(0, centerX, centerY)

        self.camera.setHpr(self.heading, self.pitch, 0)

        # Movement
        move_vec = Vec3(0, 0, 0)

        if self.keys['w']:
            move_vec.y += 1
        if self.keys['s']:
            move_vec.y -= 1
        if self.keys['a']:
            move_vec.x -= 1
        if self.keys['d']:
            move_vec.x += 1
        if self.keys['space']:
            move_vec.z += 1
        if self.keys['shift']:
            move_vec.z -= 1

        if move_vec.lengthSquared() > 0:
            move_vec.normalize()
            move_vec *= self.move_speed * dt

            # Rotate movement based on heading
            import math
            rad = math.radians(self.heading)
            cos_h = math.cos(rad)
            sin_h = math.sin(rad)

            new_x = move_vec.x * cos_h - move_vec.y * sin_h
            new_y = move_vec.x * sin_h + move_vec.y * cos_h

            self.player_pos.x += new_x
            self.player_pos.y += new_y
            self.player_pos.z += move_vec.z

            self.camera.setPos(self.player_pos)

        return Task.cont

if __name__ == '__main__':
    game = FirstPersonGame()
    game.run()
'''
        return code


def main():
    root = tk.Tk()
    app = ABSEngine(root)
    root.mainloop()


if __name__ == '__main__':
    main()