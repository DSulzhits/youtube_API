import os
from dotenv import load_dotenv
import json
from googleapiclient.discovery import build

load_dotenv()


class Channel:
    api_key: str = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, channel_id: str):
        self.__id = channel_id
        yt_channel = self.youtube.channels().list(id=self.__id, part='snippet,statistics').execute()
        self.__channel_info = json.dumps(yt_channel, indent=2, ensure_ascii=False)
        self.__info = json.loads(self.__channel_info)
        self.__title = self.__info['items'][0]['snippet']['title']
        self.__description = self.__info['items'][0]['snippet']['description']
        self.__link = 'https://www.youtube.com/' + self.__info['items'][0]['snippet']['customUrl']
        self.__subscribers = self.__info['items'][0]['statistics']['subscriberCount']
        self.__videoCount = self.__info['items'][0]['statistics']['videoCount']
        self.__viewCount = self.__info['items'][0]['statistics']['viewCount']

    @property
    def channel_id(self) -> str:
        return self.__id

    @property
    def channel_title(self) -> str:
        return self.__title

    @property
    def channel_description(self) -> str:
        return self.__description

    @property
    def channel_link(self) -> str:
        return self.__link

    @property
    def channel_subscribers(self) -> str:
        return self.__subscribers

    @property
    def channel_videoCount(self) -> str:
        return self.__videoCount

    @property
    def channel_viewCount(self) -> str:
        return self.__viewCount

    @property
    def channel_info(self) -> str:
        return self.__channel_info

    @channel_id.setter
    def channel_id(self, name_inp: str) -> None:
        raise AttributeError("property 'channel_id' of 'Channel' object has no setter")

    def make_json(self):
        data = {}
        data['channel_id'] = self.__id
        data['channel_title'] = self.__title
        data['channel_description'] = self.__description
        data['channel_link'] = self.__link
        data['channel_subscribers'] = self.__subscribers
        data['channel_videoCount'] = self.__videoCount
        data['channel_viewCount'] = self.__viewCount
        with open(f'channel_info_{self.__title}.json', 'a', encoding='UTF-8') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)
