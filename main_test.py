import PySimpleGUI as sg
import tools
import settings

#------------------------------------------------------------

def move_center(window):
    screen_width, screen_height = window.get_screen_dimensions()
    win_width, win_height = window.size
    x, y = (screen_width - win_width)//2, (screen_height - win_height)//2
    window.move(100, 100)

#------------------------------------------------------------

def show_test_popup():
    popup_layout =    [   
                [sg.Text('My first popup window')],
                [sg.Button('Close', key='-close-popup-')]
            ]
    popup_win = sg.Window(title="Hello Popup", layout=popup_layout, finalize=True)
    move_center(popup_win)
    
    while True:
        event, values = popup_win.read(5)
        if event == sg.WIN_CLOSED:
            break
        elif event == '-close-popup-':
            break
    popup_win.close()

#------------------------------------------------------------


class Foo:
    def __init__(self, y=10, z=100) -> None:
        self.y = y
        self.z = z
    def calc_me(self, num) -> int:
        return num + self.x + self.y + self.z
    x = 12

#------------------------------------------------------------

settings.load()

print(settings.workspace.rootFolder)

settings.workspace.rootFolder = 'changed by user'

settings.save()



f = Foo(11, 66)
f2 = Foo(z=11, y=66)
print(f.x)
print(f.y)
print(f.z)
f.x = 13
f.y = 11
f.z = 111
print(f.x)
print(f.y)
print(f.z)
print(f.calc_me(10000))

tools.saveObject("test_data.txt", f)

f2 = tools.loadObject("test_data.txt", Foo())

main_layout =    [   
                [sg.Text('My first window')],
                [sg.In('Enter something')],
                [sg.Button('New win', key='-new-window-')]
            ]
win = sg.Window(title="Hello Workd!", layout=main_layout, finalize=True)

#move_center(win)
x,y = 0,0
while True:
    x,y = win.CurrentLocation()
    event, values = win.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == '-new-window-':
        win.DisableClose = True
        show_test_popup()
        win.DisableClose = False


win.close()

