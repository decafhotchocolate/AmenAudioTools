def run(file, output):
        from amen.audio import Audio
        # from amen.utils import example_audio_file
        from amen.synthesize import synthesize
        audio_file = file # INPUT FILE HERE
        audio = Audio(audio_file)

        beats = audio.timings['beats']
        beats.reverse()

        # output
        out = synthesize(beats)
        out.output(output)
