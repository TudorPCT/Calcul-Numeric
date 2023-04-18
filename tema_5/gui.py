import numpy as np
import PySimpleGUI as sg

from tema_4.GaussSeidelRareSystem import GaussSeidelRareSystem
from tema_4.RareMatrix import RareMatrix
from tema_5.symmetrical_rare_matrix import power_iteration


def build_layout(iters=0, lamda=0):
    layout = [
        [sg.Text('Path for the matrix:'), sg.InputText(key='path_a')],
        [sg.Text('Path for the solution: '), sg.InputText(key='path_x')],
        [sg.Text('Epsilon:'), sg.Spin([i for i in range(0, 100)], initial_value=8, key='epsilon')],
        [sg.Text('Kmax:'), sg.Spin([i for i in range(1, 1000000)], initial_value=10000, key='kmax')],
        [sg.Text(f'Lambda: {lamda}', background_color='#A47551', key='lambda')],
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
            path_x = values['path_x']
            epsilon = 10 ** -int(values['epsilon'])
            kmax = int(values['kmax'])

            try:
                with open(path_a, 'r') as f:
                    pass
            except FileNotFoundError:
                sg.popup(f"Invalid path for the matrix!")
                continue

            try:
                with open(path_x, 'w') as f:
                    a = RareMatrix(path=path_a,epsilon=epsilon)
                    r, v, k = power_iteration(a, epsilon, kmax)

                    f.write(f"{r}\n")
                    f.write(f"{v.size}\n")

                    for index, i in enumerate(v):
                        for j in i:
                            f.write(f"{j}, {index}\n")

                    window['lambda'].update(f'Lambda: {r}')
                    window['iters'].update(f'Iters: {k}')
            except FileNotFoundError:
                sg.popup(f"Invalid path for the solution!")
                continue

    window.close()


open_gui()
