# yt-dlp_GUI
## Description
A simple, unsophisticated Graphical User Interface implementing some yt-dlp functional.
Currently supports downloading, merging video with audio files from supported sites, extracting metadata and downloading subtitles as well as extracting and downloading audio-only and selecting audio codecs for audio-only downloads the same way as resolutions for video downloads. A directory, where the file will be saved can be chosen. Features a progressbar indicating progression of a download.
Built program is currently only provided for Windows.
## Considering antivirus detections
yt-dlp_GUI doesn't feature any malicious files. The detections are false positives caused by the popularity of using Python for different malicious files and then converting them to .exe's (for ex. with PyInstaller which is used to build the .exe in releases) and due to the program being unsigned.
If you are still concerned, [you can build the program from source.]()

## Usage
### Running the prebuilt version (for Windows)
To run yt-dlp_GUI downloaded from releases, simply unzip and launch the .exe file
### Building for yourself (for any platform)
To build yt-dlp_GUI from source:
Download the source code, install pyinstaller and run pyinstaller.exe --onefile (download ytdlp icon with .ico extension and point at it) with something like --icon=C:\example.ico (copy the path from the file manager and then add the file name there), then the name of the script and add --noconsole , so console doesn't show up when booting. It should look like that: Pyinstaller.exe --onefile --noconsole --icon=C:\example.ico yt-dlp_GUI.py
Wait for it to build. Then you'll have build and dist folders in the directory from where you ran the command. Open dist folder and create misc directory there, put ffmpeg(should be named exactly that) folder and logo.ico(should be named exactly that) there. Now the executable in the dist folder is fully functional! You can delete the build folder if you want

## Screenshots
![image](https://github.com/user-attachments/assets/740f6cdf-28f4-4c4f-b451-6e135b40adeb)

### If you have any problems or would like to have any fetures added
If you would like to have any features added or are experiencing trouble, feel free to create a pull request or an issue. I will try to help you out

