import random
import numpy as np
import PySimpleGUI as sg

from strassen_matrix_multiplication import multiply_strassen


def init(size):
    a = [[random.randint(0, 20) for _ in range(size)] for _ in range(size)]
    b = [[random.randint(0, 20) for _ in range(size)] for _ in range(size)]
    output = [[0 for _ in range(size)] for _ in range(size)]
    return a, b, output


def build_matrix(size, a, b, output):
    matrix_a = [[
        sg.InputText(
            default_text=a[y][x],
            size=(10, 10),
            key=f"matrix_a_{x}_{y}")
        for x in range(size)] for y in range(size)]
    matrix_b = [[sg.InputText(
        default_text=b[y][x],
        size=(10, 10),
        key=f"matrix_b_{x}_{y}") for x in range(size)] for y in range(size)]
    output = [[
        sg.Text(
            output[y][x],
            background_color="#523600",
            size=(5, 1))
        for x in range(size)] for y in range(size)]
    return matrix_a, matrix_b, output


def get_input_matrix(size, values, matrix):
    input_matrix = [[0.0 for _ in range(size)] for _ in range(size)]
    for x in range(size):
        for y in range(size):
            try:
                input_matrix[x][y] = float(values[f"{matrix}_{x}_{y}"])
            except ValueError:
                return None
    return input_matrix


def get_input(size, values):
    matrix_a = get_input_matrix(size, values, "matrix_a")
    matrix_b = get_input_matrix(size, values, "matrix_b")
    if matrix_a is None or matrix_b is None:
        sg.popup(f"Invalid value found! Please enter an integer value!")
    return matrix_a, matrix_b


def build_layout(size, min_size, matrix_a, matrix_b, output):
    layout = [
        [
            sg.Text('Matrix size: '),
            sg.Spin([i for i in range(2, 100)], initial_value=size, key='size'),
            sg.Text('Minimum size to compute: '),
            sg.Spin([i for i in range(1, 100)], initial_value=min_size, key='min_size')
        ],
        [
            [sg.Text('First Matrix'), sg.Text(''), sg.Text('')],
            matrix_a
        ],
        [
            [sg.Text('Second Matrix'), sg.Text(''), sg.Text('')],
            matrix_b
        ],
        [
            [sg.Text('Output Matrix'), sg.Text(''), sg.Text('')],
            output
        ],
        [
            sg.Button('Compute'),
            sg.Button('Reset')
        ]
    ]
    return layout


def open_gui():
    sg.theme('DarkAmber')
    sg.set_options(font=('Helvetica', 20))
    
    size = 3
    min_size = 3
    a, b, c = init(size)

    matrix_a, matrix_b, output = build_matrix(size, a, b, c)
    layout = build_layout(size, min_size, matrix_a, matrix_b, output)

    window = sg.Window('Window Title', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'Compute':
            a, b = get_input(size, values)
            min_size = int(values['min_size'])
            if matrix_a is None or matrix_b is None:
                continue
            else:
                try:
                    print("Numpy:", np.matmul(a, b))
                    print("a: ", a)
                    print("b: ", b)
                except:
                    print("Numpy error")
                c = multiply_strassen(a, b, size, int(values['min_size']))
                matrix_a, matrix_b, output = build_matrix(size, a, b, c)
                layout = build_layout(size, min_size, matrix_a, matrix_b, output)
                window.close()
                window = sg.Window('Window Title', layout)
        elif event == 'Reset':
            size = int(values['size'])
            min_size = int(values['min_size'])
            sg.set_options(font=('Helvetica', int(60/size)))
            a, b, c = init(size)
            matrix_a, matrix_b, output = build_matrix(size, a, b, c)
            layout = build_layout(size, min_size, matrix_a, matrix_b, output)
            window.close()
            window = sg.Window('Window Title', layout)
    window.close()


open_gui()
