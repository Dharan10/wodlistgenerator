# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#       CODED: bY Team alpha
#       DaTe: in progress
#       Dev: Python (TKinter)
#
# ~~~~~~~~~~~ INFO ~~~~~~~~~~~~~~~~~~~
#
#    Simple wordlist generator
#    GUI (Graphical User Interface)
#
# ************************************

# Module tkinter
from tkinter import *
from  messagebox import *
import itertools
import sys
import string
import subprocess
import os
import time
import webbrowser

# Main «root»
root = Tk()
root.title('wrdlist.py')

# Title
l = LabelFrame(root, text="Wrd.py", padx=20, pady=20)
l.pack(fill="both", expand="yes")

# Label info
Label(l, text="Simple WordList geneator\nCoded By Team Aplha").pack()


# Build wordlist
def GET():
    ch = chars.get()
    mn = value1.get()
    mx = value2.get()
    N_file =str(input("Enter the file name:"))
    ln = len(ch)
    TXT = []

    file = open(N_file, 'a')
    for x in range(mn, mx + 1):
        meta = ln ** x
        TXT.append(meta)
        TXT_line = sum(TXT)

        for xs in itertools.product(ch, repeat=x):
            file.write(''.join(xs) + '\n')
    file.close()
    Finish()


# Finish & Exit
def Finish():
    print("[*] Finish!")
    showinfo('INFO', 'File Finish!')
    showinfo('Exit', 'Thanks for using me!')
    sys.exit()


# Var
value = StringVar()
value.set("Chars")
chars = Entry(root, textvariable=value, width=20)
chars.pack(padx=5, pady=5)

value1 = IntVar()
value1.set("Min")
MIN = Entry(root, textvariable=value1, width=20)
MIN.pack(padx=5, pady=5)

value2 = IntVar()
value2.set("Max")
MAX = Entry(root, textvariable=value2, width=20)
MAX.pack(padx=5, pady=5)


def callinfo():
    showinfo('INFO', '(WordList Generator)')




def EXIT():
    showinfo('Closing', 'Thanks for using me!')
    root.quit()


# frame 1
Frame1 = Frame(root, borderwidth=1, relief=GROOVE)

# button «OK "build wordlist"»
qb = Button(root, text='Ok', command=GET)
qb.pack(side=LEFT, padx=5, ipadx=15, pady=5)
# button «INFO "call INFO»
qb = Button(root, text='Info', command=callinfo)
qb.pack(side=LEFT, padx=5, ipadx=10, pady=5)
# button «EXIT "call EXIT"»
qb = Button(root, text='Exit', command=EXIT)
qb.pack(side=LEFT, padx=5, ipadx=10, pady=5)

Frame1.pack(side=LEFT, padx=0, pady=20)
# Run main «MAIN»
root.mainloop()
