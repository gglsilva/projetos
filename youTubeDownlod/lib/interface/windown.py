# -*- coding: utf-8 -*-
from tkinter import Event
import PySimpleGUI as sg
#from PySimpleGUI.PySimpleGUI import Window

# Define o conteúdo da janela
layout = [
    [sg.Text('Video URL:'), sg.Input(key='-URL-')],
    [sg.Checkbox('Video', default=True, k='-VD-'),
    sg.Checkbox('Audio', default=False, k='-AD-')],
    [sg.Button('Download'), sg.Button('Cancel')],
   
    '''
    [sg.Radio('Video', "VideoDemo", default=True, size=(10,1), k='-R1-') \
    , sg.Radio('Video Playlist', "VideoPlDemo", default=False, size=(10,1), k='-R2-') \
    , sg.Radio('Audio', "AudioDemo", default=False, size=(10,1), k='-R3-') \
    , sg.Radio('Audio Playlist', "AudioPlDemo", default=False, size=(10,1), k='-R4-') ],
'''
]

# Cria a janela
window = sg.Window('YouTube Downloader', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    
    window['-OUTPUT-'].update('Hello ' + values['-INPUT-'] + "! Thanks for trying PySimpleGUI")

# Finish up by removing from the screen
window.close()