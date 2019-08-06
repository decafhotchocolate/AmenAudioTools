import youtube_dl

# https://github.com/ytdl-org/youtube-dl/blob/master/README.md#embedding-youtube-dl

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'outtmpl': './tmp/vid.%(ext)s'
}

def convert(link):
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])