import os
from dotenv import load_dotenv
import json
from googleapiclient.discovery import build
load_dotenv()

class Channel:

    def __init__(self, ID):
        self.ID = ID

    def print_info(self):
        api_key: str = os.getenv('YT_API_KEY')
        youtube = build('youtube', 'v3', developerKey=api_key)
        channel = youtube.channels().list(id=self.ID, part='snippet,statistics').execute()
        channel_info = json.dumps(channel, indent=2, ensure_ascii=False)
        print(channel_info)
