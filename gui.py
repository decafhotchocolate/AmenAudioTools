# import libraries
from appJar import gui
import sys

# import functions
from funcs import beatsReversed
from funcs.grouped import everyEvenBeat
from funcs.grouped import everyOddBeat
from funcs.separated import everyFirstBeat
from funcs.separated import everySecondBeat
from funcs.separated import everyThirdBeat
from funcs.separated import everyFourthBeat

def function(file):
    data = app.getAllInputs(includeEmptyInputs=False)
    importedFile = data['f1']
    selection = data['option'] # arbitrary but clean
    output = data['output'] + '/output.wav'
    
    if selection == "Reverse beats of the audio file.":
        beatsReversed.run(importedFile, output)
    if selection == "Get every 1st and 3rd beat of the audio file.":
        everyOddBeat.run(importedFile, output)
    if selection == "Get every 2nd and 4th beat of the audio file.":
        everyEvenBeat.run(importedFile, output)
    if selection == "Get every 1st beat of the audio file.":
        everyFirstBeat.run(importedFile, output)
    if selection == "Get every 2nd beat of the audio file.":
        everySecondBeat.run(importedFile, output)
    if selection == "Get every 3rd beat of the audio file.":
        everyThirdBeat.run(importedFile, output)
    if selection == "Get every 4th beat of the audio file.":
        everyFourthBeat.run(importedFile, output)
    app.infoBox("Success!", "Proccess complete! Check your output directory.", parent=None)


# create a GUI variable called app
app = gui("Amen Audio Tools", "400x300")

app.setFont(size=12)
app.setBg("pink")

# add & configure widgets - widgets get a name, to help referencing them later
app.addLabel("heading", "Amen Audio Tools")
app.addRadioButton("option", "Reverse beats of the audio file.")
app.addRadioButton("option", "Get every 1st and 3rd beat of the audio file.")
app.addRadioButton("option", "Get every 2nd and 4th beat of the audio file.")
app.addRadioButton("option", "Get every 1st beat of the audio file.")
app.addRadioButton("option", "Get every 2nd beat of the audio file.")
app.addRadioButton("option", "Get every 3rd beat of the audio file.")
app.addRadioButton("option", "Get every 4th beat of the audio file.")

app.addLabel("inputLabel", "What audio file?")
app.addFileEntry("f1")

app.addLabel("outputLabel", "Where to save the output?")
app.addDirectoryEntry("output")

app.addButton("Perform Magic", function)

# start the GUI
app.go()
