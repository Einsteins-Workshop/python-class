import PySimpleGUI as sg
from PIL import Image, ImageTk, ImageSequence
gif_filename = 'file:///C:/Users/Einstein/Downloads/dance-happy.gif'
layout = [[sg.Image(key='-IMAGE-')]]
window = sg.Window('Window Title', layout, element_justification='c', margins=(0,0), element_padding=(0,0), finalize=True)
interframe_duration = Image.open(gif_filename).info['duration']
while True:
    for frame in ImageSequence.Iterator(Image.open(gif_filename)):
        event, values = window.read(timeout=interframe_duration)
        if event == sg.WIN_CLOSED:
            exit(0)
        window['-IMAGE-'].update(data=ImageTk.PhotoImage(frame) ) 