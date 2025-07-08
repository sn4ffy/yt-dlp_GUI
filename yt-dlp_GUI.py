from tkinter import *
from yt_dlp import YoutubeDL
from tkinter import filedialog
from tkinter import ttk
import os
from functools import partial
import threading

root = Tk()
root.configure(bg="red")
root.title('yt-dlp')
icon_location = (os.getcwd() + '/misc/logo.ico')
root.iconbitmap(icon_location.replace('\\', '/'))


download_bar = ttk.Progressbar(root, orient=HORIZONTAL, mode='determinate', length=120)
download_bar.grid(row=3, column=5, columnspan=2, pady=10)


audio_codecs = ['mp3', 'aac', 'opus', 'wav', 'flac']
video_res = ['480', '720', '1080', '1440', '2160']


def validate_length(cc_langs):
    return len(cc_langs) <= 2

def handle_focus_in(event, entry_widget, placeholder_text):
    if entry_widget.get() == placeholder_text:
        entry_widget.delete(0, END)      
        entry_widget.config(fg='black')

def handle_focus_out(event, entry_widget, placeholder_text):
    if not entry_widget.get():
        entry_widget.insert(placeholder_text)
        entry_widget.config(fg='grey70')


validation = (root.register(validate_length), '%P')

cc_langs = Entry(root, width=3, validate='key', validatecommand=validation, fg='grey70', borderwidth=0.5, insertwidth=1)
cc_langs.grid(row=1, column=6, padx=0)
cc_langs.insert(0, 'CC')

cc_langs.bind('<FocusIn>', partial(handle_focus_in, entry_widget = cc_langs, placeholder_text = 'CC'))
cc_langs.bind('<FocusOut>', partial(handle_focus_out, entry_widget = cc_langs, placeholder_text = 'CC'))




e2 = Entry(root, fg='grey70', width=50, borderwidth=0, insertwidth=1)
e2.grid(row = 0, column = 1, columnspan=10, padx=3, pady=20)
e2.insert(0, "Video's URL")

e2.bind("<FocusIn>", partial(handle_focus_in, entry_widget = e2, placeholder_text = "Video's URL"))
e2.bind("<FocusOut>", partial(handle_focus_out, entry_widget = e2, placeholder_text = "Video's URL"))

clicked = StringVar()
clicked.set('720')


fmtdrop = OptionMenu(root, clicked, *video_res)
fmtdrop.config(indicatoron=0, borderwidth=0, pady=2, bg='white')
fmtdrop.grid(row=0, column=11, padx=10)
def update_dropdown():
    menu = fmtdrop["menu"]
    menu.delete(0,END)
    if var.get() == 1:
        for codec in audio_codecs:
            menu.add_command(label=codec, command=lambda v=codec: clicked.set(v))
            clicked.set(audio_codecs[0])
    else:
        for codec in video_res:
            menu.add_command(label=codec, command=lambda v=codec: clicked.set(v))
            clicked.set(video_res[0])

var = IntVar()
audio_only = Checkbutton(root, text = 'Audio only', variable=var, command=update_dropdown, pady=0, padx=0, borderwidth=0.5)
audio_only.grid(row=1, column=5)

def my_hook(d):
    if d['status'] == 'downloading':
        if 'fragment_index' in d and 'fragment_count' in d and d['fragment_count']:
            percent = (d['fragment_index'] / d['fragment_count']) * 100
            download_bar['value'] = percent
        elif 'downloaded_bytes' in d and 'total_bytes' in d and d['total_bytes']:
            percent = (d['downloaded_bytes'] / d['total_bytes']) * 100
            download_bar['value'] = percent
        
def download(): 
    ffmpeg_dir = os.getcwd() + '/misc/ffmpeg/bin'
    save_directory = filedialog.askdirectory()
    if not save_directory:
        return
    if not save_directory.endswith("/"):
        save_directory += "/"
    if var.get() == 1:
        ydl_opts = {
        'format': "bv*+ba/b",
        'progress_hooks': [my_hook],
        'ffmpeg_location': ffmpeg_dir.replace('\\', '/'),
        'outtmpl': save_directory.replace('\\', '/') + '%(uploader)s/%(title)s.%(ext)s',
        'writesubtitles': True,
        'writeautomaticsub': True,
        'subtitleslangs': [cc_langs.get()],
        'subtitlesformat': 'srt',  
        'skip_download': False,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': clicked.get()
        },{
            'key': 'FFmpegMetadata',
            'add_metadata': 'True'
        
    }]
}   
    else:
        ydl_opts = {
        'format': f"bestvideo[height<={clicked.get()}]+bestaudio/best[height<={clicked.get()}]",
        'progress_hooks': [my_hook],
        'ffmpeg_location': ffmpeg_dir.replace('\\', '/'),
        'outtmpl': save_directory.replace('\\', '/') + '%(uploader)s/%(title)s.%(ext)s',
        'writesubtitles': True,
        'writeautomaticsub': True,
        'subtitleslangs': [cc_langs.get()],
        'subtitlesformat': 'srt',  
        'skip_download': False,
        'postprocessors': [{
            'key': 'FFmpegMetadata',
            'add_metadata': 'True'
        
    }]
}   
    download_bar['value'] = 3
    URL = e2.get()
    YoutubeDL(ydl_opts).download(URL)

def start_download():
    download_bar['value'] = 0
    threading.Thread(target=download, daemon=False).start()

dl = Button(root, text='Download', command=start_download, borderwidth=0, bg='white')
dl.grid(row= 0, column=12, padx=1)
space = Label(root, fg='red', bg='red', text='   ', padx=0, pady=0)
space.grid(row=0, column=13)
space3 = Label(root, fg='red', bg='red', text='  ', padx=0, pady=0)
space3.grid(row=0, column=0)
space2 = Label(root, fg='red', bg='red', text='   ', padx=0, pady=0)
space2.grid(row=2, column=3)
root.mainloop()
