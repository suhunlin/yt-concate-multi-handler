from yt_concate.utils import Utils
from yt_concate.pipeline.pipeline import Pipeline
from yt_concate.pipeline.steps.preflight import Preflight
from yt_concate.pipeline.steps.get_video_list import GetVideoList
from yt_concate.pipeline.steps.initialize_yt import InitializeYT
from yt_concate.pipeline.steps.download_captions import DownloadCaptions
from yt_concate.pipeline.steps.read_captions import ReadCaptions
from yt_concate.pipeline.steps.search import Search
from yt_concate.pipeline.steps.download_videos import DownloadVideos
from yt_concate.pipeline.steps.edit_video import EditVideo

def main():
    steps = [
        Preflight(),
        GetVideoList(),
        InitializeYT(),
        DownloadCaptions(),
        ReadCaptions(),
        Search(),
        DownloadVideos(),
        EditVideo(),

    ]
    inputs = {
        'channel_id' : 'UCKSVUHI9rbbkXhvAXK-2uxA',
        'video_list_limit': 250,  # one page 25 item for url
        'search_word': 'incredible',
        'video_clip_limit': 20,

    }
    utils = Utils()
    p1 = Pipeline(steps)
    p1.run(utils, inputs)


if __name__ == '__main__':
    main()