#import PySimpleGUIQt as sg
import PySimpleGUI as sg
import os, sys

def format_raw(data:list, width:int):
    out_txt = ''
    sz = len(data)
    for d in range(sz):
        if not d==0 and not d % width:
            out_txt += '\n'
        out_txt += str(data[d])
        if not d == sz-1:
            out_txt += ', '
    return out_txt

def format_c(data:list, width:int, name:str):
    out_txt = '#pragma once\n\n'
    out_txt += f'uint8_t {name}[] = {{'
    sz = len(data)
    for d in range(sz):
        if not d % width:
            out_txt += '\n    '
        out_txt += str(data[d])
        if not d == sz-1:
            out_txt += ', '
    out_txt += '\n};'
    return out_txt

def format_py(data:list, width:int, name:str):
    out_txt = f'{name} = ['
    sz = len(data)
    for d in range(sz):
        if not d % width:
            out_txt += '\n    '
        out_txt += str(data[d])
        if not d == sz-1:
            out_txt += ', '
    out_txt += '\n]'
    return out_txt

def start():
    layout = [
        [sg.T("")],
        [sg.Text('Datastructure name (optional): '), sg.Input(key='-DATASTRUCTURE-')],
        [sg.Text('BMP width (x): ',), sg.Input('16', key='-WIDTH-')],
        [sg.Text('BMP height (y):   '), sg.Input('16', key='-HEIGHT-')],
        [sg.Button('Submit')],
    ]

    window = sg.Window('BMP DRAWERRRRRRRR', layout, size=(300,200))

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            sys.exit()
        elif event == "Submit":
            data_ok = False
            try:
                x = int(values['-WIDTH-'].strip())
                y = int(values['-HEIGHT-'].strip())
                data_ok = True
            except Exception as e:
                sg.popup_no_wait('ERROR: Must specify VALID width and height...',title='ERROR')
                print(e)
            if data_ok:
                return [values['-DATASTRUCTURE-'], x, y]
        


def save(save_data:list, save_width=None, save_name=None):
    #sg.theme("DarkPurple6")
    layout = [
        [sg.T("")],
        [sg.Text('Filename: '), sg.Input(key='-NAME-')],
        [sg.Text("Folder: "), sg.Input(os.getcwd(), key='-FOLDER-'), sg.FolderBrowse()],
        [sg.Text('Select save mode: ')],
        [sg.Radio('RAW (UNFORMATTED)', 'MODE', default=True, key='-NONE-')],
        [sg.Radio('RAW (FORMATTED)', 'MODE', default=False, key='-RAW-')],
        [sg.Radio('C HEADER', 'MODE', default=False, key='-C-')],
        [sg.Radio('PYTHON LIST', 'MODE', default=False, key='-P-')],
        [sg.Button('Submit')],
    ]

    ###Building Window
    window = sg.Window('SAVE UR BMP', layout, size=(450,200))

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            return False
        elif event == "Submit":
            raw_name = values['-NAME-']
            if raw_name.strip() == '':
                sg.popup_no_wait('ERROR: Must specify filename...',title='ERROR')
            else:
                if values['-NONE-']:
                    file_out = save_data
                    file_ext = '.txt'
                elif values['-RAW-']:
                    file_out = format_raw(save_data, save_width)
                    file_ext = '.txt'
                elif values['-C-']:
                    if save_name == '':
                        save_name = raw_name
                    file_out = format_c(save_data, save_width, save_name)
                    file_ext = '.h'
                elif values['-P-']:
                    if save_name == '':
                        save_name = raw_name
                    file_out = format_py(save_data, save_width, save_name)
                    file_ext = '.py'

                if not raw_name.lower().endswith(file_ext):
                    raw_name += file_ext

                file_name = os.path.join(values['-FOLDER-'], raw_name)
                if sg.popup_yes_no(f'Save to: {file_name} ?') == 'Yes':
                    with open(file_name, 'w') as the_file:
                        the_file.write(file_out)
                    sg.popup_no_wait('Saved!')
                    break
    return True