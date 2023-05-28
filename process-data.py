import PySimpleGUI as psg

layout = [
    [psg.Text(text='Audio player')],
    [psg.Multiline(default_text='Paragraph')]
]
window = psg.Window('Gap Fill', layout, size=(715,250))
while True:
   event, values = window.read()
   print(event, values)
   if event in (None, 'Exit'):
      break
window.close()