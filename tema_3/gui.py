import numpy as np
import PySimpleGUI as sg

from tema_3.main import get_b, solve_householder, compute_inv
from tema_3.main import householder

background_color = '#A47551'


def init(size):
    a = np.random.uniform(0, 100, size=(size, size))
    s = np.random.uniform(0, 100, size=(size, 1))
    b = get_b(a, s)

    for _x in range(size):
        a[_x][_x] = sum(abs(a[_x][j]) if _x != j else 0 for j in range(size)) + 1

    a_init = a.copy()

    q = householder(a, size, b)

    x = solve_householder(a_init.copy(), s)

    inv = compute_inv(a_init.copy())

    matrix_a, matrix_s, matrix_b, matrix_r, matrix_q, matrix_x, matrix_inv = \
        build_matrix(size, a_init, a, s, b, q, x, inv)
    layout = build_layout(size, matrix_a, matrix_s, matrix_b, matrix_r, matrix_q, matrix_x, matrix_inv)
    return a, q, matrix_a, matrix_s, matrix_b, matrix_r, matrix_q, matrix_x, matrix_inv, layout


def build_matrix(size, a_init, a, s, b, q, x_, inv):
    global background_color

    matrix_a = [[
        sg.InputText(
            default_text=round(a_init[x][y], 2),
            size=(7, 7),
            key=f"matrix_a_{y}_{x}",
            enable_events=True)
        for x in range(size)] for y in range(size)]
    matrix_s = [
        sg.InputText(
            default_text=round(s[x][0], 2),
            size=(7, 7),
            key=f"matrix_s_{x}_{0}",
            enable_events=True)
        for x in range(size)]
    matrix_b = [
        sg.Text(
            round(b[x][0], 2),
            background_color=background_color,
            size=(8, 1))
        for x in range(size)]
    matrix_r = [[
        sg.Text(
            round(a[y][x], 2),
            background_color=background_color,
            size=(5, 1))
        for x in range(size)] for y in range(size)]
    matrix_q = [[
        sg.Text(
            round(q[y][x], 2),
            background_color=background_color,
            size=(5, 1))
        for x in range(size)] for y in range(size)]
    matrix_x = [
        sg.Text(
            round(x_[x], 2),
            background_color=background_color,
            size=(5, 1))
        for x in range(size)]
    matrix_inv = [[
        sg.Text(
            round(inv[y][x], 2),
            background_color=background_color,
            size=(5, 1))
        for x in range(size)] for y in range(size)]
    return matrix_a, matrix_s, matrix_b, matrix_r, matrix_q, matrix_x, matrix_inv


def build_layout(size, matrix_a, matrix_s, matrix_b, matrix_r, matrix_q, matrix_x, matrix_inv):
    global background_color

    layout = [
        [
            sg.Text('Matrix size: '),
            sg.Spin([i for i in range(2, 100)], initial_value=size, key='size'),
        ],
        [
            [sg.Text('A'), sg.Text(''), sg.Text('')],
            matrix_a
        ],
        [
            [sg.Text('S'), sg.Text(''), sg.Text('')],
            matrix_s
        ],
        [
            [sg.Text('B'), sg.Text(''), sg.Text('')],
            matrix_b
        ],
        [
            [sg.Text('R'), sg.Text(''), sg.Text('')],
            matrix_r
        ],
        [
            [sg.Text('Q'), sg.Text(''), sg.Text('')],
            matrix_q
        ],
        [
            [sg.Text('X'), sg.Text(''), sg.Text('')],
            matrix_x
        ],
        [
            [sg.Text('Inv'), sg.Text(''), sg.Text('')],
            matrix_inv
        ],
        [
            sg.Button('Compute'),
            sg.Button('Reset'),
            sg.Button('Switch')
        ]
    ]
    return layout


def get_input_matrix(row, col, values, matrix):
    input_matrix = np.zeros((row, col))
    for x in range(row):
        for y in range(col):
            try:
                input_matrix[x][y] = float(values[f"matrix_{matrix}_{x}_{y}"])
            except ValueError:
                sg.popup(f"Invalid value found! Please enter a float value!")
                return None
    return input_matrix


def get_input_vector(size, values):
    input_vector = np.zeros(size)
    for x in range(size):
        try:
            input_vector[x] = float(values[f"matrix_b_{x}"])
        except ValueError:
            sg.popup(f"Invalid value found! Please enter a float value!")
            return None
    return input_vector


def open_gui():
    sg.theme('DarkAmber')
    sg.set_options(font=('Helvetica', 15))

    size = 3

    a, q, matrix_a, matrix_s, matrix_b, matrix_r, matrix_q, matrix_x, matrix_inv, layout = init(size)

    window = sg.Window('Window', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'Compute':
            size = int(values['size'])
            a = get_input_matrix(size, size, values, 'a')
            if a is not None:
                a_init = a.copy()
                s = get_input_matrix(size, 1, values, 's')
                b = get_b(a, s)
                b_init = b.copy()
                q = householder(a, size, b)
                if q is None:
                    sg.popup(f"Matrix is not non-singular!")
                    continue
                x = solve_householder(a_init.copy(), s)
                inv = compute_inv(a_init.copy())
                matrix_a, matrix_s, matrix_b, matrix_r, matrix_q, matrix_x, matrix_inv = \
                    build_matrix(size, a_init, a, s, b_init, q, x, inv)
                layout = build_layout(size, matrix_a, matrix_s, matrix_b, matrix_r, matrix_q, matrix_x, matrix_inv)
                window.close()
                window = sg.Window('Window', layout)
        elif event == 'Reset':
            size = int(values['size'])
            sg.set_options(font=('Helvetica', int(60/size)))
            a, q, matrix_a, matrix_s, matrix_b, matrix_r, matrix_q, matrix_x, matrix_inv, layout = init(size)
            layout = build_layout(size, matrix_a, matrix_s, matrix_b, matrix_r, matrix_q, matrix_x, matrix_inv)
            window.close()
            window = sg.Window('Window Title', layout)

    window.close()


open_gui()
