import os

from settings import OUTPUTS_DIR
from settings import DOWNLOADS_DIR
from settings import VIDEOS_DIR
from settings import CAPTIONS_DIR


class Utils:
    def __str__(self):
        return '<class Utils: This class is the set of all helper function>' + '\n'

    def create_dir(self):
        os.makedirs(OUTPUTS_DIR, exist_ok=True)
        os.makedirs(DOWNLOADS_DIR, exist_ok=True)
        os.makedirs(VIDEOS_DIR, exist_ok=True)
        os.makedirs(CAPTIONS_DIR, exist_ok=True)
        return 'Create dir done'

    def get_video_list_filepath(self, channel_id):
        return os.path.join(DOWNLOADS_DIR, channel_id + '.txt')

    def check_video_list_exists(self, filepath):
        return os.path.exists(filepath) and os.path.getsize(filepath) > 0

    def get_output_filepath(self, filename):
        return os.path.join(OUTPUTS_DIR, filename + '.mp4')
