import time

from yt_concate.multi_handler.yt_multi_processing import YTMultiprocessing
from yt_concate.multi_handler.yt_multi_threading import YTMultithreading
from .step import Step


class ReadCaptions(Step):
    def __str__(self):
        return '<class ReadCaption: This class is use for read all captions(dictionary data structure) to YT structure>' + '\n'

    def process(self, utils, inputs, data):
        start_time = time.time()
        # self.read_caption(data)
        # multi_process = YTMultiprocessing()
        # multi_process.run_processing(target=self.read_caption_by_multi_thread, iterable_data=data, dictionary_data=inputs)
        multi_thread = YTMultithreading()
        multi_thread.run_threading(target=self.read_caption_by_multi_thread, iterable_data=data, dictionary_data=inputs)
        end_time = time.time()
        print('read captions cost time:', end_time - start_time)
        # for yt in data:
        #     print(yt.captions)
        #     print('\n')
        return data

    def read_caption(self, data):
        for yt in data:
            if not yt.check_caption_file_exists():
                # print(yt.caption_id + '.txt is not exists!')
                continue
            captions = {}
            time_line = False
            with open(yt.caption_filepath, 'r') as f:
                for line in f:
                    if '-->' in line:
                        time_line = True
                        time = line.strip()
                        continue
                    if time_line:
                        time_line = False
                        caption = line.strip()
                        captions[caption] = time
            yt.captions = captions

    def read_caption_by_multi_thread(self, *args, **kwargs):
        for yt in args:
            if not yt.check_caption_file_exists():
                # print(yt.caption_id + '.txt is not exists!')
                continue
            captions = {}
            time_line = False
            with open(yt.caption_filepath, 'r') as f:
                for line in f:
                    if '-->' in line:
                        time_line = True
                        time = line.strip()
                        continue
                    if time_line:
                        time_line = False
                        caption = line.strip()
                        captions[caption] = time
            yt.captions = captions
