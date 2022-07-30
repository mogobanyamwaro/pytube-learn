from pytube import YouTube
from pytube import Playlist
import threading
import multiprocessing as mp

urls = 'https://www.youtube.com/watch?v=coqQwbDezUA&list=PLC3y8-rFHvwiRYB4-HHKHblh3_bQNJTMa'

p = Playlist(urls)

def download_videos(p):
    for video in p.videos:
        def download_video(video):
            # video.download()
            print(video.title)
    t = threading.Thread(target=download_video, args=(video,))
    t.start()
    t.join()


# t= threading.Thread(target=download_video, args=(p,))
# t.start()
# t.join()



