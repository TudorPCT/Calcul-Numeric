import numpy as np
import PySimpleGUI as sg

from tema_2 import choleski_decomposition, compute_det
from tema_2 import solve_system

background_color = '#A47551'


def init_cd(size, m):

    a = np.random.uniform(0, 20, size=(size, size))
    a = a + a.T

    for i in range(size):
        a[i][i] = sum(abs(a[i][j]) if i != j else 0 for j in range(size)) + 1

    a_init = a.copy()

    d = choleski_decomposition(a, size, 10 ** -m)

    det_a = compute_det(d)
    matrix_a, matrix_l, matrix_d, matrix_l_t = build_matrix_cd(size, a_init, a, d)
    layout = build_layout_cd(size, m, matrix_a, matrix_l, matrix_d, matrix_l_t, det_a)
    return a, d, det_a, matrix_a, matrix_l, matrix_d, matrix_l_t, layout


def init_cds(size, m):
    a = np.random.uniform(0, 20, size=(size, size))
    a = a + a.T

    for i in range(size):
        a[i][i] = sum(abs(a[i][j]) if i != j else 0 for j in range(size)) + 1

    b = np.random.uniform(0, 20, size=size)
    a_init = a.copy()

    d = choleski_decomposition(a, size, 10 ** -m)
    x = solve_system(a, b, d, 10 ** -m)

    matrix_a, matrix_b, matrix_x = build_matrix_cds(size, a_init, b, x)
    layout = build_layout_cds(size, m, matrix_a, matrix_b, matrix_x)
    return a, b, x, matrix_a, matrix_b, matrix_x, layout


def build_matrix_cd(size, a_init, a, d):
    global background_color

    l = np.tril(a, -1)
    np.fill_diagonal(l, 1)

    matrix_a = [[
        sg.InputText(
            default_text=round(a_init[y][x], 2),
            size=(10, 10),
            key=f"matrix_a_{x}_{y}",
            enable_events=True) if x >= y else
        sg.InputText(
            default_text=round(a_init[y][x], 2),
            size=(10, 10),
            key=f"matrix_a_{x}_{y}",
            disabled=True,
            disabled_readonly_background_color='#523A28')
        for x in range(size)] for y in range(size)]
    matrix_l = [[
        sg.Text(
            round(l[y][x], 2),
            background_color=background_color,
            size=(8, 1))
        for x in range(size)] for y in range(size)]
    matrix_d = [
        sg.Text(
            round(d[x], 2),
            background_color=background_color,
            size=(8, 1))
        for x in range(size)]
    matrix_l_t = [[
        sg.Text(
            round(l[x][y], 2),
            background_color=background_color,
            size=(8, 1))
        for x in range(size)] for y in range(size)]
    return matrix_a, matrix_l, matrix_d, matrix_l_t


def build_matrix_cds(size, a, b, x):
    global background_color

    l = np.tril(a, -1)
    np.fill_diagonal(l, 1)

    matrix_a = [[
        sg.InputText(
            default_text=round(a[j][i], 2),
            size=(10, 10),
            key=f"matrix_a_{i}_{j}",
            enable_events=True) if i >= j else
        sg.InputText(
            default_text=round(a[j][i], 2),
            size=(10, 10),
            key=f"matrix_a_{i}_{j}",
            disabled=True,
            disabled_readonly_background_color='#523A28')
        for i in range(size)] for j in range(size)]
    matrix_b = [sg.InputText(
        default_text=b[i],
        size=(10, 10),
        key=f"matrix_b_{i}") for i in range(size)]
    matrix_x = [
        sg.Text(
            round(x[i], 2),
            background_color=background_color,
            size=(8, 1))
        for i in range(size)]
    return matrix_a, matrix_b, matrix_x


def build_layout_cd(size, m, matrix_a, matrix_l, matrix_d, matrix_l_t, det_a):
    global background_color

    layout = [
        [
            sg.Text('Matrix size: '),
            sg.Spin([i for i in range(2, 100)], initial_value=size, key='size'),
            sg.Text('Epsilon power of -10: '),
            sg.Spin([i for i in range(5, 100)], initial_value=m, key='m')
        ],
        [
            [sg.Text('A'), sg.Text(''), sg.Text('')],
            matrix_a
        ],
        [
            [sg.Text('L'), sg.Text(''), sg.Text('')],
            matrix_l
        ],
        [
            [sg.Text('D'), sg.Text(''), sg.Text('')],
            matrix_d
        ],
        [
            [sg.Text('LT'), sg.Text(''), sg.Text('')],
            matrix_l_t
        ],
        [
            sg.Text(' det(A)', background_color=background_color), sg.Text('='),
            sg.Text(' det(L)', background_color=background_color), sg.Text('*'),
            sg.Text(' det(D)', background_color=background_color), sg.Text('*'),
            sg.Text(' det(LT)', background_color=background_color), sg.Text('='),
            sg.Text(f' {round(det_a, 2)}', background_color=background_color)
        ],
        [
            sg.Button('Compute'),
            sg.Button('Reset'),
            sg.Button('Switch')
        ]
    ]
    return layout


def build_layout_cds(size, m, matrix_a, matrix_b, matrix_x):
    global background_color

    layout = [
        [
            sg.Text('Matrix size: '),
            sg.Spin([i for i in range(2, 100)], initial_value=size, key='size'),
            sg.Text('Epsilon power of -10: '),
            sg.Spin([i for i in range(5, 100)], initial_value=m, key='m')
        ],
        [
            [sg.Text('A'), sg.Text(''), sg.Text('')],
            matrix_a
        ],
        [
            [sg.Text('B'), sg.Text(''), sg.Text('')],
            matrix_b
        ],
        [
            [sg.Text('X'), sg.Text(''), sg.Text('')],
            matrix_x
        ],
        [
            sg.Button('Compute'),
            sg.Button('Reset'),
            sg.Button('Switch')
        ]
    ]
    return layout


def get_input_matrix(size, values):
    input_matrix = np.zeros((size, size))
    for x in range(size):
        for y in range(size):
            try:
                input_matrix[x][y] = float(values[f"matrix_a_{x}_{y}"])
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
    sg.set_options(font=('Helvetica', 20))

    current_window = "cd"
    size = 3
    m = 5

    a, d, det_a, matrix_a, matrix_l, matrix_d, matrix_l_t, layout = init_cd(size, m)

    window = sg.Window('Choleski Decomposition', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event.startswith('matrix_a_'):
            x, y = [int(i) for i in event.split('_')[2:]]
            if x > y:
                window[f"matrix_a_{y}_{x}"].update(values[event])
        elif event == 'Compute' and current_window == 'cd':
            size = int(values['size'])
            m = int(values['m'])
            a = get_input_matrix(size, values)
            if a is not None:
                a_init = a.copy()
                d = choleski_decomposition(a, size, 10 ** -m)
                if d is None:
                    sg.popup(f"Matrix is not positive definite!")
                    continue
                det_a = compute_det(d)
                matrix_a, matrix_l, matrix_d, matrix_l_t = build_matrix_cd(size, a_init, a, d)
                layout = build_layout_cd(size, m, matrix_a, matrix_l, matrix_d, matrix_l_t, det_a)
                window.close()
                window = sg.Window('Window Title', layout)
        elif event == 'Compute' and current_window == 'cds':
            size = int(values['size'])
            m = int(values['m'])
            a = get_input_matrix(size, values)
            if a is not None:
                a_init = a.copy()
                b = get_input_vector(size, values)
                if b is not None:
                    b_init = b.copy()
                    d = choleski_decomposition(a, size, 10 ** -m)
                    if d is None:
                        sg.popup(f"Matrix is not positive definite!")
                        continue
                    x = solve_system(a, b, d, 10 ** -m)
                    if x is None:
                        sg.popup(f"Matrix is not positive definite!")
                        continue
                    matrix_a, matrix_b, matrix_x = build_matrix_cds(size, a_init, b_init, x)
                    layout = build_layout_cds(size, m, matrix_a, matrix_b, matrix_x)
                    window.close()
                    window = sg.Window('Window Title', layout)
        elif (event == 'Reset' and current_window == 'cd') or (event == 'Switch' and current_window == 'cds'):
            size = int(values['size'])
            m = int(values['m'])
            sg.set_options(font=('Helvetica', int(60 / size)))
            a, d, det_a, matrix_a, matrix_l, matrix_d, matrix_l_t, layout = init_cd(size, m)
            current_window = 'cd'
            window.close()
            window = sg.Window('Choleski Decomposition', layout)
        elif (event == 'Reset' and current_window == 'cds') or (event == 'Switch' and current_window == 'cd'):
            size = int(values['size'])
            m = int(values['m'])
            sg.set_options(font=('Helvetica', int(60 / size)))
            a, b, x, matrix_a, matrix_b, matrix_x, layout = init_cds(size, m)
            current_window = 'cds'
            window.close()
            window = sg.Window('Choleski Decomposition System Solver', layout)

    window.close()


open_gui()
