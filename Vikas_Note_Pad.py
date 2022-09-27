# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 21:22:44 2022

@author: Vikas Reddy karkala
"""
email='''Subject: Vacation request for September, 10-15

Dear Mr./Ms. [Last name],

I would like to request a vacation from Monday, September 9th till Friday, September 13th.

I will make sure to complete all my current projects and pending tasks in advance before the vacation. My colleagues [Name] and [Name] will cover my responsibilities during my absence.

Looking forward to your approval.

Sincerely,
[Your name]
[Job title]'''


letter='''Mr. XYZ
(Address)
(Date)

Mr. ABC

(Address)

Dear Sir/Madam,

Subject: Application for the leave of 1 day.

I am writing this letter to inform you that I need one day leave. From last night I am not feeling well. And hence I will not able to come to the office tomorrow.

I will join the office from the day after tomorrow. Please consider my leave application.

Thanking you.
Yours sincerely
(Sign)

(your name)'''
from pathlib import Path
import PySimpleGUI as sg
sg.theme('GrayGrayGray')
smileys=[ 'happy',[':)','xD',':D','<3'],
    'sad',[':(','T_T'],
    'other',[':3']
    ]
smiley_events=smileys[1]+smileys[3]+smileys[5]
menu_layout=[
    # ['File',['Open','Save','---','Exit']],
    #           ['Tools',['Word Count']],
    #           ['Add',smileys]
    
    
     ['File',['Open','Save','---','Exit']],
    ['Tools',['Word Count']],
    ['Add',smileys],
    ['Templates',['E-mail','Letter']]
             ]

layout=[
        
        [sg.Menu(menu_layout)],
        [sg.Text('Untitled',key='-DOCNAME-')],
        [sg.Multiline(no_scrollbar=True,size=(60,50),key='-TEXTBOX-')]
        
        ]
window=sg.Window('Vikas NotePad',layout)
while(True):
    events,values=window.read()
    if events in(sg.WINDOW_CLOSED,'Exit'):
        break
    if events=='Open':
        filepath=sg.popup_get_file('open',no_window=True)
        if filepath:
            file=Path(filepath)
            window['-TEXTBOX-'].update(file.read_text())
            window['-DOCNAME-'].update(filepath.split('/')[-1])
                                                      
    
    if events=='Save':
        filepath=sg.popup_get_file('Save as',no_window=True,save_as=True)+'.txt'
        file=Path(filepath)
        file.write_text(values['-TEXTBOX-'])
        window['-DOCNAME-'].update(filepath.split('/')[-1])
    
    if events=='Word Count':
        text=values['-TEXTBOX-']
        clean_text=text.replace('\n',' ').split(' ')
        word_count=len(clean_text)
        char_count=len(''.join(clean_text))
        sg.popup(f'No. of Words are {word_count} and No. of Characters are {char_count}')
    if events in smiley_events:
       text=values['-TEXTBOX-']+events
       window['-TEXTBOX-'].update(text)
       
    if events =='E-mail':
        
        window['-TEXTBOX-'].update(email)
    
    if events=='Letter':
        
        window['-TEXTBOX-'].update(letter)
        
        
        
        
        
        
window.close()    