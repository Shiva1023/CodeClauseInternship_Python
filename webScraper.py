import tkinter as tk
from tkinter import scrolledtext
from bs4 import BeautifulSoup
import requests

def set_window_size(root, width_percent, height_percent):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    window_width = int(screen_width * width_percent)
    window_height = int(screen_height * height_percent)

    root.geometry(f"{window_width}x{window_height}")

def fetch_and_display_headlines():
    url = "https://www.sakshi.com/"
    html_text = requests.get(url)
    
    if html_text.status_code == 200:
        soup = BeautifulSoup(html_text.text, "html.parser")
        headlines = soup.find_all("h5", class_="heading")
        headlines_text = '\n'.join([headline.text.strip() for headline in headlines])
        
        text_area.delete('1.0', tk.END)
        text_area.insert(tk.END, headlines_text)

window = tk.Tk()
window.title("Sakshi News Headlines")

set_window_size(window, width_percent=0.7, height_percent=0.8)

fetch_button = tk.Button(window, text="Fetch Headlines", command=fetch_and_display_headlines)
fetch_button.pack(pady=10)

text_area = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=500, height=200)
text_area.pack(padx=10, pady=10)

window.mainloop()
