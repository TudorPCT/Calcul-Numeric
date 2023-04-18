import numpy as np
import PySimpleGUI as sg

from tema_4.GaussSeidelRareSystem import GaussSeidelRareSystem


def build_layout(norm=0, iters=0):
    layout = [
        [sg.Text('Path for the coefficients matrix:'), sg.InputText(key='path_a')],
        [sg.Text('Path for the vector:'), sg.InputText(key='path_b')],
        [sg.Text('Path for the solution: '), sg.InputText(key='path_x')],
        [sg.Text('Epsilon:'), sg.Spin([i for i in range(0, 100)], initial_value=8, key='epsilon')],
        [sg.Text('Epsilon:'), sg.Spin([i for i in range(1, 1000000)], initial_value=10000, key='kmax')],
        [sg.Text(f'Solution norm: {norm}', background_color='#A47551', key='norm')],
        [sg.Text(f'Iters: {iters}', background_color='#A47551', key='iters')],
        [sg.Button('Compute')]
    ]

    return layout


def open_gui():
    sg.theme('DarkAmber')
    sg.set_options(font=('Helvetica', 15))

    layout = build_layout()

    window = sg.Window('Gauss-Seidel', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'Compute':
            path_a = values['path_a']
            path_b = values['path_b']
            path_x = values['path_x']
            epsilon = 10 ** -int(values['epsilon'])
            kmax = int(values['kmax'])

            try:
                with open(path_a, 'r') as f:
                    pass
            except FileNotFoundError:
                sg.popup(f"Invalid path for the coefficients matrix!")
                continue

            try:
                with open(path_b, 'r') as f:
                    pass
            except FileNotFoundError:
                sg.popup(f"Invalid path for the vector!")
                continue

            system = GaussSeidelRareSystem(path_a, path_b, kmax, epsilon)

            try:
                with open(path_x, 'w') as f:
                    x = system.solve()

                    for index, i in enumerate(x):
                        for j in i:
                            f.write(f"{j}, {index}\n")

                    window['norm'].update(f'Solution norm: {system.norm}')
                    window['iters'].update(f'Iters: {system.gauss_seidel_iterations}')
            except FileNotFoundError:
                sg.popup(f"Invalid path for the solution!")
                continue

    window.close()


open_gui()
