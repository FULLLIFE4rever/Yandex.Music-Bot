from yandex_music import Client

client = Client().init()

type_to_name = {
    "track": "трек",
    "artist": "исполнитель",
    "album": "альбом",
    "playlist": "плейлист",
    "video": "видео",
    "user": "пользователь",
    "podcast": "подкаст",
    "podcast_episode": "эпизод подкаста",
}


def send_search_request_and_print_result(query, printin=0):  # noqa: C901
    search_result = client.search(query, type_="playlist")
    if printin:
        search_result = client.search(query, page=1, type_="playlist")

    for result in search_result.playlists.results:
        print(result.tracks)


if __name__ == "__main__":
    while True:
        input_query = input("Введите поисковой запрос: ")
        send_search_request_and_print_result(input_query)
        send_search_request_and_print_result(input_query, 1)
