import alsaaudio

def get_volume():
    mixer = alsaaudio.Mixer()
    pcm = alsaaudio.PCM()
    print(pcm)
    vol = mixer.getvolume()
    #return vol

while True:
    print(get_volume())
