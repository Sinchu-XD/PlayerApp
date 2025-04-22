from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.slider import Slider
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import AsyncImage
from kivy.clock import Clock
from kivy.storage.jsonstore import JsonStore
from player import play_song, update_seekbar
from playlist import add_to_playlist, play_next_song_in_playlist, play_previous_song_in_playlist
from share import share_song_or_thumbnail
from utils.youtube_search import search_youtube

class MusicPlayerApp(App):
    def build(self):
        self.song_title = "Search a song"
        self.song_url = ""
        self.song_thumbnail = ""
        self.sound = None
        self.history = []

        layout = BoxLayout(orientation='vertical')

        # Search Bar
        self.search_input = TextInput(hint_text='Search for a song...', size_hint=(1, 0.1))
        layout.add_widget(self.search_input)

        # Search Button
        search_button = Button(text="Search", size_hint=(1, 0.1))
        search_button.bind(on_press=self.search_song)
        layout.add_widget(search_button)

        # Song Title Label
        self.title_label = Label(text=self.song_title, size_hint=(1, 0.1))
        layout.add_widget(self.title_label)

        # Song Thumbnail
        self.thumbnail_image = AsyncImage(size_hint=(1, 0.5))
        layout.add_widget(self.thumbnail_image)

        # Play Button
        self.play_button = Button(text="Play", size_hint=(1, 0.1))
        self.play_button.bind(on_press=self.toggle_play_pause)
        layout.add_widget(self.play_button)

        # Next/Previous Buttons
        self.next_button = Button(text="Next", size_hint=(1, 0.1))
        self.next_button.bind(on_press=self.play_next_song)
        layout.add_widget(self.next_button)

        self.prev_button = Button(text="Previous", size_hint=(1, 0.1))
        self.prev_button.bind(on_press=self.play_previous_song)
        layout.add_widget(self.prev_button)

        # Seekbar
        self.seekbar = Slider(min=0, max=100, value=0, size_hint=(1, 0.1))
        layout.add_widget(self.seekbar)

        # Volume Control
        self.volume_slider = Slider(min=0, max=1, value=0.5, size_hint=(1, 0.1))
        layout.add_widget(self.volume_slider)

        # Share Button
        self.share_button = Button(text="Share", size_hint=(1, 0.1))
        self.share_button.bind(on_press=self.share_song)
        layout.add_widget(self.share_button)

        return layout

    def search_song(self, instance):
        query = self.search_input.text
        if query:
            song_title, video_url, song_thumbnail = search_youtube(query)
            self.song_title = song_title
            self.song_url = video_url
            self.song_thumbnail = song_thumbnail
            self.title_label.text = self.song_title
            self.thumbnail_image.source = self.song_thumbnail

            add_to_playlist(self.song_title, self.song_url)

    def toggle_play_pause(self, instance):
        if self.sound and self.sound.state == 'play':
            self.sound.stop()
            self.play_button.text = "Play"
        else:
            self.sound = play_song(self.song_url)
            self.play_button.text = "Pause"

    def play_next_song(self, instance):
        play_next_song_in_playlist()

    def play_previous_song(self, instance):
        play_previous_song_in_playlist()

    def share_song(self, instance):
        share_song_or_thumbnail()

if __name__ == "__main__":
    MusicPlayerApp().run()
  
