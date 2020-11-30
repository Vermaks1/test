from tkinter import Tk, Frame, Label, Text, Scrollbar, \
    Button, PhotoImage, END, W, E
import translators as ts
from textblob import TextBlob as detect
import pyttsx3
from datetime import datetime, date, time

def window():
    win_text = text1.get(1.0, END)
    if len(win_text) < 4:
        win_text = 'Enter text than 2 characters'
        text1.delete(1.0, END)
        text1.insert(END, win_text)
    translate(win_text)


def clipboard():
    try:
        clip_text = root.clipboard_get()
    except BaseException:
        clip_text = 'Buffer empty'
    text1.delete(1.0, END)
    text1.insert(END, clip_text)
    translate(clip_text)


def translate(get_text):
    language_text = detect(get_text)
    indetect = language_text.detect_language()
    if indetect != 'ru':
        langout = 'ru'
    else:
        langout = 'en'
    lab1['text'] = indetect
    lab0['text'] = f'{indetect}↔{langout}'
    lab2['text'] = langout


    output = ts.google(get_text, to_language=langout, if_use_cn_host=True)
    text2.delete(1.0, END)
    text2.insert(END, output)


root = Tk()
root.title('VermaksTranslate')

lab0 = Label(root, font='arial 11 bold', fg='white', bg='blue')
lab0.grid(row=0, column=0, columnspan=2, sticky=W + E, pady=2)


f1 = Frame(root)
f1.grid(row=1, column=0)
text1 = Text(f1, font='arial 12', wrap='word', width=50, height=12, padx=10, pady=10)
text1.pack(side='left')
scroll1 = Scrollbar(f1, command=text1.yview)
scroll1.pack(side='right', fill='y')
text1['yscroll'] = scroll1.set
# text1.pack_propagate(False)
root.update()
tx, ty = text1.winfo_width(), text1.winfo_height()
lab1 = Label(text1, fg='blue', bg='white')
# lab1.pack(side='right', anchor='s')
lab1.place(x=tx - 35, y=ty - 35)

f2 = Frame(root)
f2.grid(row=1, column=1)
text2 = Text(f2, font='arial 12', wrap='word', width=50, height=12, padx=10, pady=10, bg='gray97')
text2.pack(side='left')
scroll2 = Scrollbar(f2, command=text2.yview)
scroll2.pack(side='right', fill='y')
text2['yscroll'] = scroll2.set
# text2.pack_propagate(False)
lab2 = Label(text2, fg='blue', bg='gray97')
# lab2.pack(side='right', anchor='s')

lab2.place(x=tx - 35, y=ty - 35)

bt1 = Button(root, text='Translate window', font='arial 12', fg='blue', command=window)
bt1.grid(row=2, column=0, sticky=W + E, padx=5, pady = 5)
bt2 = Button(root, text='Translate clipboard', font='arial 12', fg='blue', command=clipboard)
bt2.grid(row=2, column=1, sticky=W + E, padx = 5, pady = 5)

tts = pyttsx3.init()
tts.setProperty('voice', 'ru')
tts.setProperty('voice', 'en')
tts.setProperty('rate', 120)
tts.setProperty('volume', 0.8)

voices = tts.getProperty('voices')
for voice in voices:
    if 'Irina' in voice.name:
        tts.setProperty('voice', voice.id)


def say_time(s):
    tts.say(s)
    tts.runAndWait


time_checker = datetime.now()
say_time(f'text1')


root.mainloop()

