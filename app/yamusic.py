"""Yandex music client"""

from yandex_music import ClientAsync

# from yandex_music.utils.request_async import Request


class YandexMusic:
    """Yandex music client"""

    def __init__(self):
        # request = Request(proxy_url='http://proxy.server:3128')
        # self.client = ClientAsync(request=request)
        self.client = ClientAsync()

    async def _search(self, query: str):
        """Method to find track with artist"""
        search_result = await self.client.search(query)
        # Если треков не найдено
        if search_result.tracks is None:
            return [
                {
                    "cover_url": "https://music.yandex.ru/favicon32.png",
                    "id": "0",
                    "url": "https://music.yandex.ru/",
                    "title": "Yandex.music",
                    "artist": "Yandex music official site",
                }
            ]
        #
        tracks = []
        for track in search_result.tracks.results:
            tracks_dict = {
                "cover_url": (
                    track.get_cover_url()
                    if track.cover_uri
                    else "https://music.yandex.ru/favicon32.png"
                ),
                "id": str(track.id),
                "url": "https://music.yandex.ru/album/"
                f"{track.albums[0].id}/track/{track.id}",
                "title": track.title,
                "artist": " ".join(artist.name for artist in track.artists),
            }
            tracks.append(tracks_dict)
        return tracks

    async def track_results(self, query: str):
        """Method to take part of the find music"""
        return await self._search(query)


yandex_music = YandexMusic()
