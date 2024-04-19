import PySimpleGUI as sg

label1 = sg.Text("Enter feet:")
input_text1 = sg.InputText()
label2 = sg.Text("Enter inches:")
input_text2 = sg.InputText()
convert = sg.Button("convert")

window = sg.Window("Convertor",
                   layout= [[label1, input_text1],
                   [label2, input_text2], [convert]])
window.read()
window.close()