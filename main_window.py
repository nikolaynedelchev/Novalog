import PySimpleGUI as sg
import tools
import settings
import data_tests



settings.load()


main_layout = [   
    [sg.Button(             'New delivery',                     key='-new-delivery-')],
    [sg.Button(             'Delete delivery',                  key='-delete-delivery-')],
    [sg.Button(             'New contract',                     key='-new-contract-')],
    [sg.Button(             'Delete contract',                  key='-delete-contract-')],
    [sg.Button(             'New buyer',                        key='-new-buyer-')],
    [sg.Button(             'Delete buyer',                     key='-delete-buyer-')],
    [sg.Button(             'Autocorrect manual changes',       key='-autocorrect-')],
    [sg.FolderBrowse(       'Select workspace',                 key='-select-workspace-',       enable_events=True)],
    [sg.Text(               '',                                 key='-workspace-folder-')],

#########################################################    
    [sg.Button(             'Do data test',       key='-do-data-test-')],
]

win = sg.Window(title="Novalog Deliveries", layout=main_layout, finalize=True)

for col in main_layout:
    for w in col:
        win[w.key].expand(True)


win['-workspace-folder-'].update(settings.workspace.getName())

win.move(settings.workspace.mainWindowX,settings.workspace.mainWindowY)

while True:
    settings.workspace.mainWindowX,settings.workspace.mainWindowY = win.CurrentLocation()
    event, values = win.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == '-select-workspace-':
        settings.workspace.rootFolder = values['-select-workspace-']
        win['-workspace-folder-'].update(settings.workspace.getName())
    elif event == '-do-data-test-':
        data_tests.doTest()

    settings.save()

win.close()