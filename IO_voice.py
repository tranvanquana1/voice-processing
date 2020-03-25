import soundfile as sf
import sounddevice as sd
import time



def sync_record(filename, duration, sr, channels):
    print('recording')
    my_rec = sd.rec(samplerate=sr, channels=channels, frames=int(duration*sr))
    sd.wait()
    sf.write(filename + '.wav', data=my_rec, samplerate=sr)
    print('done recording')

sync_record("test.wav", 5, 22050, 1)