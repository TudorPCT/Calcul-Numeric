import PySimpleGUI as sg
import numpy as np
from math import *

from tema_7.main import find_roots


def build_layout():
    layout = [
        [sg.Text('Coefficients(list divided by comma):'), sg.InputText(key='coefficients')],
        [sg.Text('Output path:'), sg.InputText(key='path')],
        [sg.Text('Algorthm calls:'), sg.Spin([i for i in range(0, 100)], initial_value=10, key='m_max')],
        [sg.Text(f'Found roots: -', background_color='#A47551', key='roots')],
        [sg.Button('Compute')]
    ]
    return layout


def open_gui():
    sg.theme('DarkAmber')
    sg.set_options(font=('Helvetica', 15))

    layout = build_layout()

    window = sg.Window('Function minimum', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'Compute':

            try:
                a = np.fromstring(values['coefficients'], dtype=float, sep=',')
                m_max = int(values['m_max'])
                path = values['path']
            except ValueError:
                sg.popup(f"Invalid values!")
                continue

            roots = find_roots(a, m_max=m_max, file_path=path)

            window['roots'].update(f'Found roots: {roots}')

    window.close()


open_gui()
