from tkinter import *
from yt_dlp import YoutubeDL
from tkinter import filedialog
import os

root = Tk()
root.configure(bg="red")
root.title('yt-dlp')
root.iconbitmap('C:/PythonProjects/logo/logo.ico')

audio_codecs = ['mp3', 'aac', 'opus', 'wav', 'flac']
video_codecs = ['h264', 'h265', 'av01', 'h263']

e2 = Entry(root, fg='grey70', width=50, borderwidth=0, insertwidth=1 )
e2.grid(row = 0, column = 0, columnspan=3, padx=18, pady=20)
e2.insert(0, "Video's URL")

e2.bind("<FocusIn>", lambda e: [e2.delete(0, END),e2.config(fg='black')] if e2.get() == "Video's URL" else None)
e2.bind("<FocusOut>", lambda e: [e2.insert(0, "Video's URL"),  e2.config(fg='grey70')] if not e2.get() else None)

clicked = StringVar()
clicked.set('h264')

fmtdrop = OptionMenu(root, clicked, *video_codecs)
fmtdrop.config(indicatoron=0, borderwidth=0, pady=2, bg='white')
fmtdrop.grid(row=0, column=3, padx=3)
def update_dropdown():
    menu = fmtdrop["menu"]
    menu.delete(0,END)
    if var.get() == 1:
        for codec in audio_codecs:
            menu.add_command(label=codec, command=lambda v=codec: clicked.set(v))
            clicked.set(audio_codecs[0])
    else:
        for codec in video_codecs:
            menu.add_command(label=codec, command=lambda v=codec: clicked.set(v))
            clicked.set(video_codecs[0])

var = IntVar()
audio_only = Checkbutton(root, text = 'Audio only', variable=var, command=update_dropdown, pady=0)
audio_only.grid(row=1, column=1)

def download():
    ffmpeg_dir = os.getcwd() + '/ffmpeg/bin'
    save_directory = filedialog.askdirectory()
    if not save_directory:
        return
    if not save_directory.endswith("/"):
        save_directory += "/"
    ydl_opts = {
    'format': "bv*+ba/b",
    'ffmpeg_location': ffmpeg_dir.replace('\\', '/'),
    'outtmpl': save_directory.replace('\\', '/') + '%(uploader)s/%(title)s.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': clicked.get()
    },{
        'key': 'FFmpegMetadata',
        'add_metadata': 'True'
    }]
}
    URL = e2.get()
    YoutubeDL(ydl_opts).download(URL)
dl = Button(root, text='Download', command=download, borderwidth=0, bg='white')
dl.grid(row= 0, column=4, padx=1)
space = Label(root, fg='red', bg='red', text='   ', padx=0, pady=0)
space.grid(row=0, column=5)
space2 = Label(root, fg='red', bg='red', text='   ', padx=0, pady=0)
space2.grid(row=2, column=3)
root.mainloop()