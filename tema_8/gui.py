import PySimpleGUI as sg

from tema_8.main import find_func_min_x, derivative_1_2, derivative_2
from math import *


def build_layout():
    layout = [
        [sg.Text('Function:'), sg.InputText(key='function')],
        [sg.Text('Target:'), sg.InputText(key='target')],
        [sg.Text(f'Found minimum using G1: -', background_color='#A47551', key='g1_min')],
        [sg.Text(f'Iters using G1: -', background_color='#A47551', key='g1_iters')],
        [sg.Text(f'Found minimum using G2: -', background_color='#A47551', key='g2_min')],
        [sg.Text(f'Iters using G2: -', background_color='#A47551', key='g2_iters')],
        [sg.Button('Compute')]
    ]
    return layout


def create_function(expression):
    return lambda x: eval(expression)


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
            if values['function'] == '':
                sg.popup(f"Invalid values!")
                continue

            function = values['function']
            f = create_function(function)

            if values['target'] == '':
                g1_min, g1_iters = find_func_min_x(f, derivative_1_2, derivative_2)
                g2_min, g2_iters = find_func_min_x(f, derivative_1_2, derivative_2)
            else:
                try:
                    target = float(eval(values['target']))
                    g1_min, g1_iters = find_func_min_x(f, derivative_1_2, derivative_2, target)
                    g2_min, g2_iters = find_func_min_x(f, derivative_1_2, derivative_2, target)
                except ValueError:
                    sg.popup(f"Invalid values!")
                    continue

            window['g1_min'].update(f'Found minimum using G1: {g1_min}')
            window['g1_iters'].update(f'Iters using G1: {g1_iters}')

            window['g2_min'].update(f'Found minimum using G2: {g2_min}')
            window['g2_iters'].update(f'Iters using G2: {g2_iters}')

    window.close()


open_gui()
