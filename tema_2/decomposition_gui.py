import numpy as np
import PySimpleGUI as sg

from tema_2 import choleski_decomposition, compute_det


background_color = '#A47551'


def init(size, m):

    a = np.random.uniform(0, 20, size=(size, size))
    a = a + a.T

    for i in range(size):
        a[i][i] = sum(abs(a[i][j]) if i != j else 0 for j in range(size)) + 1

    a_init = a.copy()

    d = choleski_decomposition(a, size, 10 ** -m)

    det_a = compute_det(d)
    matrix_a, matrix_l, matrix_d, matrix_l_t = build_matrix(size, a_init, a, d)
    layout = build_layout(size, m, matrix_a, matrix_l, matrix_d, matrix_l_t, det_a)
    return a, d, det_a, matrix_a, matrix_l, matrix_d, matrix_l_t, layout


def build_matrix(size, a_init, a, d):
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


def build_layout(size, m, matrix_a, matrix_l, matrix_d, matrix_l_t, det_a):
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
            sg.Button('Reset')
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


def open_gui():
    sg.theme('DarkAmber')
    sg.set_options(font=('Helvetica', 20))

    size = 3
    m = 5

    a, d, det_a, matrix_a, matrix_l, matrix_d, matrix_l_t, layout = init(size, m)

    window = sg.Window('Window Title', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event.startswith('matrix_a_'):
            x, y = [int(i) for i in event.split('_')[2:]]
            if x > y:
                window[f"matrix_a_{y}_{x}"].update(values[event])
        elif event == 'Compute':
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
                matrix_a, matrix_l, matrix_d, matrix_l_t = build_matrix(size, a_init, a, d)
                layout = build_layout(size, m, matrix_a, matrix_l, matrix_d, matrix_l_t, det_a)
                window.close()
                window = sg.Window('Window Title', layout)
        elif event == 'Reset':
            size = int(values['size'])
            m = int(values['m'])
            sg.set_options(font=('Helvetica', int(60 / size)))
            a, d, det_a, matrix_a, matrix_l, matrix_d, matrix_l_t, layout = init(size, m)
            window.close()
            window = sg.Window('Window Title', layout)
    window.close()


open_gui()
