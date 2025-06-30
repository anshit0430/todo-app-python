###################################
########TO-DO APP IN PYTHON########
###################################

import PySimpleGUI as sg

# Initial task list
tasks = []

# Define the layout
layout = [
    [sg.Text("Your Tasks:")],
    [sg.Listbox(values=tasks, size=(40, 10), key='TASKS')],
    [sg.InputText('', key='TASK_INPUT'), sg.Button("Add Task")],
    [sg.Button("Delete Task"), sg.Button("Clear All"), sg.Button("Exit")]
]

# Create the window
window = sg.Window("To-Do App", layout)

# Event loop
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == "Exit":
        break
    elif event == "Add Task":
        task = values['TASK_INPUT'].strip()
        if task:
            tasks.append(task)
            window['TASKS'].update(tasks)
            window['TASK_INPUT'].update('')
    elif event == "Delete Task":
        selected = values['TASKS']
        if selected:
            for item in selected:
                tasks.remove(item)
            window['TASKS'].update(tasks)
    elif event == "Clear All":
        tasks.clear()
        window['TASKS'].update(tasks)

window.close()
