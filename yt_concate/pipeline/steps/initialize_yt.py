from yt_concate.models.yt import YT
from .step import Step


class InitializeYT(Step):
    def __str__(self):
        return '<class InitializeYT: Return data of list about initialize data structure YT(url)>'

    def process(self, utils, inputs, data):
        return [YT(url) for url in data]
