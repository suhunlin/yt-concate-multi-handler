import urllib.request
import json

from yt_concate.settings import API_KEY
from .step import Step


class GetVideoList(Step):
    def __str__(self):
        return '<class GetVideoList: This class is use for get all video list form api>' + '/n'

    def process(self, utils, inputs, data):
        return self.get_all_video_in_channel(utils, inputs)

    def get_all_video_in_channel(self, utils, inputs):
        api_key = API_KEY
        channel_id = inputs['channel_id']
        video_list_limit = inputs['video_list_limit']
        fileptah = utils.get_video_list_filepath(channel_id)
        if utils.check_video_list_exists(fileptah):
            exists_video_links = self.read_video_links(fileptah)
            if len(exists_video_links) >= video_list_limit:
                print(channel_id + '.txt file exists!')
                print('video links:', len(exists_video_links), 'set:', len(set(exists_video_links)))
                return exists_video_links

        base_video_url = 'https://www.youtube.com/watch?v='
        base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

        first_url = base_search_url + 'key={}&channelId={}&part=snippet,id&order=date&maxResults=25'.format(api_key,
                                                                                                            channel_id)

        video_links = []
        url = first_url
        while True:
            inp = urllib.request.urlopen(url)
            resp = json.load(inp)

            for i in resp['items']:
                if i['id']['kind'] == "youtube#video":
                    video_links.append(base_video_url + i['id']['videoId'])
            if len(video_links) >= video_list_limit:
                break

            try:
                next_page_token = resp['nextPageToken']
                url = first_url + '&pageToken={}'.format(next_page_token)
            except:
                break
        self.wirte_video_links(fileptah, video_links)
        return video_links

    def wirte_video_links(self, filepath, video_links):
        with open(filepath, 'w') as f:
            for url in video_links:
                f.write(url + '\n')

    def read_video_links(self, filepath):
        video_links = []
        with open(filepath, 'r') as f:
            for line in f:
                video_links.append(line.strip())
        return video_links
