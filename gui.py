# import libraries
from appJar import gui
import sys
from shutil import rmtree
import os
import ffmpeg

# import functions
from funcs import beatsReversed
from funcs.grouped import everyEvenBeat
from funcs.grouped import everyOddBeat
from funcs.separated import everyFirstBeat
from funcs.separated import everySecondBeat
from funcs.separated import everyThirdBeat
from funcs.separated import everyFourthBeat

from funcs import youtubeConvert

def function(file):
    data = app.getAllInputs(includeEmptyInputs=True)
    
    selection = data['option'] # arbitrary but clean
    upload = data['f1']
    ytLink = data['link']
    output = data['output'] + '/output.wav'
    fileType = data['type']
    
    importedFile = None

    if upload == '' and ytLink == '':
        print('file not present...')
        app.warningBox('No file selected...', 'Please insert either an audio file or a YouTube Link to use.', parent=None)
        return

    if data['output'] == '':
        print('output directory not present...')
        app.warningBox('No output directory selected...', 'Please choose an output directory for your file.', parent=None)
        return

    if ytLink != '' and upload != '':
        print('two files selected...')
        app.warningBox('Two files?', 'You must choose one or the other, you can not use the YouTUbe link and the local file at the same time.', parent=None)
        return

    if ytLink != '':
        youtubeConvert.convert(ytLink)
        importedFile = './tmp/vid.mp3'

    if upload != '':
        importedFile = upload

    if selection == "Reverse beats of the audio file.":
        beatsReversed.run(importedFile, output)
        print('Starting proccess...')
    if selection == "Get every 1st and 3rd beat of the audio file.":
        everyOddBeat.run(importedFile, output)
        print('Starting proccess...')
    if selection == "Get every 2nd and 4th beat of the audio file.":
        everyEvenBeat.run(importedFile, output)
        print('Starting proccess...')
    if selection == "Get every 1st beat of the audio file.":
        everyFirstBeat.run(importedFile, output)
        print('Starting proccess...')
    if selection == "Get every 2nd beat of the audio file.":
        everySecondBeat.run(importedFile, output)
        print('Starting proccess...')
    if selection == "Get every 3rd beat of the audio file.":
        everyThirdBeat.run(importedFile, output)
        print('Starting proccess...')
    if selection == "Get every 4th beat of the audio file.":
        everyFourthBeat.run(importedFile, output)
        print('Starting proccess...')

    if os.path.exists('./tmp') and os.path.isdir('./tmp'):
        print('Deleting temp directory...')
        rmtree('./tmp')
        print('Deleted!')
    
    if fileType == '.mp3 (slower, much smaller file size)':
        print('MP3 conversion starting...')
        {
            ffmpeg
            .input(output)
            .output('output.mp3', acodec='libmp3lame')
            .run()
        }
        print('MP3 conversion complete!')
        if os.path.exists(output):
            os.remove(output)
            print('Deleted .wav file.')


    print('Success!')
    app.infoBox("Success!", "Proccess complete! Check your output directory.", parent=None)


# create a GUI variable called app
app = gui("Amen Audio Tools", "400x400")

app.setIcon('./resources/icon.gif')
app.setResizable(canResize=False)
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

app.addLabel("ytLabel", "OR, insert a YouTube link!")
app.addEntry("link")

app.addLabel("outputLabel", "Where to save the output?")
app.addDirectoryEntry("output")

app.addLabel("whatType", "How about file type?")
app.addRadioButton("type", ".wav (faster, much larger file size)")
app.addRadioButton("type", ".mp3 (slower, much smaller file size)")

app.addButton("Perform Magic", function)

# start the GUI
app.go()
