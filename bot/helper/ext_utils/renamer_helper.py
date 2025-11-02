from anitopy import parse

def get_rename_anime(file_name):
    renamed_file = None
    parsed_file = parse(file_name)
    if parsed_file:
        anime_title = parsed_file.get("anime_title", None)
        anime_season = parsed_file.get("anime_season", None)
        episode_number = parsed_file.get("episode_number", None)
        if anime_title and anime_season and episode_number:
            season_number = f"0{anime_season}" if int(anime_season) < 10 else anime_season
            episode_number = f"0{episode_number}" if int(episode_number) < 10 else episode_number
            renamed_file = f"{anime_title} S{season_number}E{episode_number}"
    return renamed_file
