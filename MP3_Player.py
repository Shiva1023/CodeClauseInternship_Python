import os
import pygame
from tkinter import filedialog, Tk, Button, Label, Frame


class MusicPlayer:
    def __init__(self):
        pygame.init()
        self.root = Tk()
        self.root.title("Music Player")
        self.root.geometry("300x150")

        self.current_folder = None
        self.current_index = 0
        self.music_files = []

        self.label_status = Label(self.root, text="", width=40)
        self.label_status.pack()

        self.btn_select_folder = Button(self.root, text="Select Folder", command=self.select_folder)
        self.btn_select_folder.pack(pady=10)

        self.btn_play = Button(self.root, text="Play", command=self.play_music)
        self.btn_play.pack(pady=5)

        self.btn_pause = Button(self.root, text="Pause", command=self.pause_music)
        self.btn_pause.pack(pady=5)

        self.btn_stop = Button(self.root, text="Stop", command=self.stop_music)
        self.btn_stop.pack(pady=5)

        self.root.mainloop()

    def select_folder(self):
        self.current_folder = filedialog.askdirectory()
        if self.current_folder:
            self.music_files = [file for file in os.listdir(self.current_folder) if file.endswith(".mp3")]
            self.label_status.config(text=f"Selected Folder: {self.current_folder}")

    def play_music(self):
        if not self.music_files:
            self.label_status.config(text="No music files found.")
            return

        pygame.mixer.music.load(os.path.join(self.current_folder, self.music_files[self.current_index]))
        pygame.mixer.music.play()
        self.label_status.config(text=f"Now Playing: {self.music_files[self.current_index]}")

    def pause_music(self):
        pygame.mixer.music.pause()
        self.label_status.config(text="Music Paused")

    def stop_music(self):
        pygame.mixer.music.stop()
        self.label_status.config(text="Music Stopped")


if __name__ == "__main__":
    MusicPlayer()
