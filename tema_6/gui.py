import numpy as np
import PySimpleGUI as sg

from tema_6.main import generate_x, generate_y, min_square_interpolation, horner, div_dif, lagrange_interpolation, \
    lagrange_norm, min_square_norm


def build_layout():
    layout = [
        [sg.Text('Function:'), sg.InputText(key='function')],
        [sg.Text('a:'), sg.InputText(key='a')],
        [sg.Text('b: '), sg.InputText(key='b')],
        [sg.Text('n: '), sg.InputText(key='n')],
        [sg.Text('x: '), sg.InputText(key='x')],
        [sg.Text(f'L(x): -', background_color='#A47551', key='lagrange')],
        [sg.Text(f'|L(x)-f(x)|: -', background_color='#A47551', key='norm_1')],
        [sg.Text(f'P(x): -', background_color='#A47551', key='square')],
        [sg.Text(f'|P(x)-f(x)|: -', background_color='#A47551', key='norm_2')],
        [sg.Text(f'sum(|L(xi)-f(xi)|): -', background_color='#A47551', key='norm_3')],
        [sg.Button('Compute')]
    ]
    return layout


def create_function(expression):
    function = lambda x: eval(expression)
    return function


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
            if values['function'] == '' \
                    or values['a'] == '' \
                    or values['b'] == '' \
                    or values['n'] == '' \
                    or values['x'] == '':
                sg.popup(f"Invalid values!")
                continue

            function = values['function']
            f = create_function(function)

            try:
                a = float(values['a'])
                b = float(values['b'])
                x = float(values['x'])
                n = int(values['n'])
            except ValueError:
                sg.popup(f"Invalid values!")
                continue

            x_values = generate_x(n, a, b)
            y_values = generate_y(x_values, f)

            a_values = min_square_interpolation(x_values, y_values)

            div_dif(x_values, y_values)

            window['lagrange'].update(f'L({x}): {lagrange_interpolation(x_values, y_values, x)}')
            window['norm_1'].update(f'|L({x})-f({x})|: {lagrange_norm(x_values, y_values, x, f)}')
            window['square'].update(f'P({x}): {horner(a_values, x)}')

            norm_2, norm_3 = min_square_norm(a_values, x_values, x, f)

            window['norm_2'].update(f'|P({x})-f({x})|: {norm_2}')
            window['norm_3'].update(f'sum(|L(xi)-f(xi)|): {norm_3}')

    window.close()


open_gui()
