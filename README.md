# Video Downloader

A simple Python-based GUI application for downloading online media. Supports downloading video and audio from a wide variety of websites supported by yt-dlp, including common formats such as MP4 and WebM.

## Features

- **Simple GUI:** Easy-to-use graphical interface built with Tkinter.
- **Multiple URLs:** Queue multiple media URLs and download them in one session.
- **Custom Download Location:** Choose where downloaded files are saved.
- **Default Download Location:** Automatically uses your Windows Downloads folder when no custom location is specified.
- **Remembered Save Location:** Saves your preferred download directory between sessions.
- **Format Selection:** Automatically selects available video and audio formats.
- **Automatic Merging:** Uses FFmpeg to combine separate video and audio streams when necessary.
- **Wide Compatibility:** Powered by yt-dlp, supporting many websites and media formats.

## Requirements

- Windows
- Python 3.13 or compatible version
- FFmpeg
- Deno (JavaScript runtime)

## Installation

### 1. Install Python

Download and install Python from:

https://www.python.org/downloads/

Make sure Python is added to PATH during installation.

### 2. Install Deno

Deno is used by yt-dlp for JavaScript-based media extraction.

Install through Windows Package Manager:

```cmd
winget install DenoLand.Deno
```

Verify installation:

```cmd
deno --version
```

### 3. Install Python Dependencies

Open Command Prompt in the project directory and run:

```cmd
python -m pip install -U "yt-dlp[default]" Pillow
```

### 4. Install FFmpeg

Download an FFmpeg Windows build from:

https://ffmpeg.org/download.html

After downloading:

1. Extract the downloaded archive.
2. Open the extracted folder.
3. Find the folder containing `bin`, `doc`, and `presets`.
4. Drag that folder directly into the Video Downloader project directory.
5. Rename the folder to **`ffmpeg`**, removing any version numbers or additional text from its original name.

Your project directory should look like this:

```text
Video Downloader/
│
├── GUI.py
├── downloader.py
├── deafault_location.txt
├── icon.png
│
└── ffmpeg/
    ├── bin/
    │   ├── ffmpeg.exe
    │   └── ffprobe.exe
    ├── doc/
    └── presets/
```

**Important:** The folder must be named exactly `ffmpeg`. Both `ffmpeg.exe` and `ffprobe.exe` must be inside its `bin` directory.

### 5. Run the Application

Open Command Prompt in the project directory and execute:

```cmd
python GUI.py
```

## Configuration

### Download Location

The application uses `deafault_location.txt` to remember your preferred download directory.

You can enter a custom directory in the GUI or edit the text file manually.

Examples:

```text
D:\Videos
```

```text
E:\Media\Downloads
```

If the file is empty or contains no path, downloads automatically go to your Windows Downloads folder.

Relative paths are also supported and are resolved relative to the project directory.

## Usage

1. Launch the application using `python GUI.py`.
2. Paste a media URL into the URL input field.
3. Click **Add URL** to add it to the download queue.
4. Repeat to add additional URLs.
5. Optionally enter a custom download directory.
6. Click **Download** to begin downloading.
7. Review the results when the downloads finish.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Tkinter | Graphical user interface |
| yt-dlp | Media extraction and downloading |
| FFmpeg | Audio/video merging and processing |
| Pillow | Application icon handling |
| Deno | JavaScript runtime for media extraction |

## Notes

- Supported websites and available formats depend on yt-dlp and the source website.
- Not every website or media URL is supported.
- Some websites may require authentication or restrict access.
- FFmpeg is required when separate video and audio streams need to be merged.
- An internet connection is required.

## License

This project is provided for personal and educational use. Users are responsible for ensuring that their downloads comply with applicable copyright laws, website terms of service, and permissions.