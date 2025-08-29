import json
from handlers import requestshandler as rqhand

class Playlist:
    def __init__(self, song_count):
        self.count = song_count
    
    def get_album_streams(self, limit=25, offset=0):
        params = {
            "operationName": "fetchPlaylist",
            "variables": json.dumps(
                {
                    "enableWatchFeedEntrypoint": False,
                    "uri": f"spotify:playlist:2maAht4eTfraySTDScSgwi",
                    "offset": offset,
                    "limit": limit,
                }
            ),
            "extensions": json.dumps(
                {
                    "persistedQuery": {
                        "version": 1,
                        "sha256Hash": "837211ef46f604a73cd3d051f12ee63c81aca4ec6eb18e227b0629a7b36adad3",
                    }
                }
            ),
        }

        result = rqhand.get_web_request(params)
        return result

    def get_streams(self):
        return self.get_album_streams(self.count)
