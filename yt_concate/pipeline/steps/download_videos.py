import time
from pytube import YouTube

from .step import Step
from yt_concate.settings import VIDEOS_DIR
from yt_concate.multi_handler.yt_multi_processing import YTMultiprocessing
from yt_concate.multi_handler.yt_multi_threading import YTMultithreading


class DownloadVideos(Step):
    def process(self, utils, inputs, data):
        start_time = time.time()
        # self.download_videos(data)
        # multi_thread = YTMultithreading()
        # multi_thread.run_threading(target=self.multi_handler_download_videos, iterable_data=data,
        #                            dictionary_data=inputs)
        multi_process = YTMultiprocessing()
        multi_process.run_processing(target=self.multi_handler_download_videos, iterable_data=data,
                                     dictionary_data=inputs)
        end_time = time.time()
        print('Download videos cost time:', end_time - start_time)
        return data

    def download_videos(self, data):
        yt_set = set([found.yt for found in data])
        print('before:', len(data), 'after:', len(yt_set))
        for yt in yt_set:
            if yt.check_video_file_exists():
                # print(yt.caption_id + '.mp4 file exists!')
                continue
            print('Downloading...', yt.url)
            YouTube(yt.url).streams.first().download(output_path=VIDEOS_DIR, filename=yt.caption_id + '.mp4')
        return data

    def multi_handler_download_videos(self, *args, **kwargs):
        yt_set = set([found.yt for found in args])
        print('before:', len(args), 'after:', len(yt_set))
        for yt in yt_set:
            if yt.check_video_file_exists():
                # print(yt.caption_id + '.mp4 file exists!')
                continue
            print('Downloading...', yt.url)
            YouTube(yt.url).streams.first().download(output_path=VIDEOS_DIR, filename=yt.caption_id + '.mp4')

    def __str__(self):
        return '<class DownloadVideo: This class is use for download all video form Found data structure>' + '\n'
