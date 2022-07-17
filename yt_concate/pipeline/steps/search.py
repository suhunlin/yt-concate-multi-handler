import time

from yt_concate.models.found import Found
from yt_concate.multi_handler.yt_multi_threading import YTMultithreading
from yt_concate.multi_handler.yt_multi_processing import YTMultiprocessing
from .step import Step


class Search(Step):
    def __init__(self):
        self.found = []

    def process(self, utils, inputs, data):
        start_time = time.time()
        # found = self.search_word(data, inputs)
        multi_thread = YTMultithreading()
        multi_thread.run_threading(target=self.multi_handler_search_word, iterable_data=data,
                                   dictionary_data=inputs)
        # can't use multi_process, self.found data will be reset
        # multi_process = YTMultiprocessing()
        # multi_process.run_processing(target=self.multi_handler_search_word, iterable_data=data,
        #                                    dictionary_data=inputs)

        end_time = time.time()
        print('Search captions cost time:', end_time - start_time)
        # for obj in found:
        #     print(obj.yt, obj.caption, obj.time)
        print('fount:', len(self.found))
        return self.found

    def search_word(self, data, inputs):
        search_word = inputs['search_word']
        for yt in data:
            if not yt.check_caption_file_exists():
                # print(yt.caption_id + '.txt file is not exists!')
                continue
            captions = yt.captions
            for caption in captions:
                if search_word in caption:
                    time = captions[caption]
                    f = Found(yt, caption, time)
                    self.found.append(f)
        return self.found

    def multi_handler_search_word(self, *args, **kwargs):
        search_word = kwargs['search_word']
        for yt in args:
            if not yt.check_caption_file_exists():
                # print(yt.caption_id + '.txt file is not exists!')
                continue
            captions = yt.captions
            for caption in captions:
                if search_word in caption:
                    time = captions[caption]
                    f = Found(yt, caption, time)
                    self.found.append(f)
