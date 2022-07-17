import os

from yt_concate.settings import CAPTIONS_DIR
from yt_concate.settings import VIDEOS_DIR


class YT:
    def __str__(self):
        return '<class YT: Is the data structure for every youtube video data download from youtube api>' + '\n'

    def __init__(self, url):
        self.url = url
        self.caption_id = self.get_caption_id_by_url()
        self.caption_filepath = self.get_caption_filepath()
        self.captions = None
        self.video_filepath = self.get_video_filepath()

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, url):
        self._url = url

    def get_caption_id_by_url(self):
        return self.url.split('watch?v=')[-1]

    def get_caption_filepath(self):
        return os.path.join(CAPTIONS_DIR, self.caption_id + '.txt')

    def check_caption_file_exists(self):
        return os.path.exists(self.caption_filepath) and os.path.getsize(self.caption_filepath) > 0

    def get_video_filepath(self):
        return os.path.join(VIDEOS_DIR, self.caption_id + '.mp4')

    def check_video_file_exists(self):
        return os.path.exists(self.video_filepath) and os.path.getsize(self.video_filepath) > 0
