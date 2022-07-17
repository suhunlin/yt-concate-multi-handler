import time
from pytube import YouTube

from yt_concate.multi_handler.yt_multi_threading import YTMultithreading
from yt_concate.multi_handler.yt_multi_processing import YTMultiprocessing
from .step import Step


class DownloadCaptions(Step):
    def process(self, utils, inputs, data):
        start_time = time.time()
        # self.download_captions(data)
        # download 為I/O bound ，所以用multi-threading的方式來下載captions
        multi_thread = YTMultithreading()
        multi_thread.run_threading(target=self.multi_handler_download_captionos, iterable_data=data,
                                   dictionary_data=inputs)
        # multi_process = YTMultiprocessing()
        # multi_process.run_processing(target=self.multi_handler_download_captionos, iterable_data=data,
        #                              dictionary_data=inputs)
        end_time = time.time()
        print('Download captions cost time:', end_time - start_time)
        return data

    def download_captions(self, data):
        for yt in data:
            if yt.check_caption_file_exists():
                print(yt.caption_id + '.txt file exists')
                continue
            try:
                source = YouTube(yt.url)
                en_caption = source.captions.get_by_language_code('a.en')
                en_caption_convert_to_srt = (en_caption.generate_srt_captions())
            except (AttributeError, KeyError) as e:
                continue
            text_file = open(yt.caption_filepath, "w")
            text_file.write(en_caption_convert_to_srt)
            text_file.close()

    def multi_handler_download_captionos(self, *args, **kwargs):
        for yt in args:
            if yt.check_caption_file_exists():
                print(yt.caption_id + '.txt file exists')
                continue
            try:
                source = YouTube(yt.url)
                en_caption = source.captions.get_by_language_code('a.en')
                en_caption_convert_to_srt = (en_caption.generate_srt_captions())
            except (AttributeError, KeyError) as e:
                continue
            text_file = open(yt.caption_filepath, "w")
            text_file.write(en_caption_convert_to_srt)
            text_file.close()
