from kivy.core.audio import SoundLoader

def play_song(song_url):
    sound = SoundLoader.load(song_url)
    if sound:
        sound.play()
        return sound
    return None

def update_seekbar(dt, sound, seekbar, total_time):
    if sound and sound.state == 'play':
        current_time = sound.get_pos()
        seekbar.value = (current_time / total_time) * 100
      
