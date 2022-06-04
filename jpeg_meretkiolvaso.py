# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 15:54:38 2022

@author: murvaiervinszabolcs
"""

import PySimpleGUI as sg
import pandas as pd
import glob
from PIL import Image


df = pd.DataFrame(columns = ["file", "magassag","hossz"])

###################
# FELÜLET
###################
#sg.change_look_and_feel('DarkAmber')	# Add a touch of color


#sg.theme_previewer()
sg.change_look_and_feel('DarkTeal6')

def TextLabel(text): return sg.Text(text+':', justification='r', size=(15,1))

layout = [[TextLabel('Képek fájlok helye'),sg.Input(key='INPUT_FOLDER'), sg.FolderBrowse(target='INPUT_FOLDER')],
          [TextLabel('xlsx neve'),sg.Input(key='XLS_FILE'), sg.FileSaveAs(target='XLS_FILE')],
          [sg.Button('Kiolvas', key='read')],[sg.Button('Ment', key='save')],[sg.Button('Kilép')]]    

window = sg.Window('Kép tulajdonságok kigyűjtése').Layout(layout)

while True:             # Event Loop
    event, values = window.Read()
    print(event, values)
    if event is None or event == 'Kilép':
        break      

    if event == 'read':      
       kepeklistaja = glob.glob(values['INPUT_FOLDER']+'\*.jpg')
        
       for i in range(len(kepeklistaja)):
            filepath = kepeklistaja[i]
            img = Image.open(filepath)
            width = img.width
            height = img.height
            to_append = [filepath, height, width]
            df_length = len(df)
            df.loc[df_length] = to_append
        
    
    if event == 'save':      
        excelhelye = values['XLS_FILE'] + '.xlsx'
        df.to_excel(excelhelye)         
            
window.Close()




