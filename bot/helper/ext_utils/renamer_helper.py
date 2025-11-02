from anitopy import parse
from ... import LOGGER, VIDEO_SUFFIXES

def get_rename_anime(file_name):
    renamed_file = None
    if file_name.split(".")[-1] not in VIDEO_SUFFIXES:
        LOGGER.info(f"File {file_name} is not a video file, skipping rename.")
        return renamed_file
    parsed_file = parse(file_name)
    LOGGER.info(f"Parsed file name {file_name}: {parsed_file}")
    if not parsed_file or not parsed_file.get("anime_title"):
        return None

    new_name_parts = []

    anime_title = parsed_file.get("anime_title")
    new_name_parts.append(anime_title)

    anime_season = parsed_file.get("anime_season")
    episode_number = parsed_file.get("episode_number")

    if anime_season and episode_number:
        season_number = f"0{anime_season}" if int(anime_season) < 10 else anime_season
        ep_number = f"0{episode_number}" if int(episode_number) < 10 else episode_number
        new_name_parts.append(f"S{season_number}E{ep_number}")
    elif anime_season:
        season_number = f"0{anime_season}" if int(anime_season) < 10 else anime_season
        new_name_parts.append(f"S{season_number}")
    elif episode_number:
        ep_number = f"0{episode_number}" if int(episode_number) < 10 else episode_number
        new_name_parts.append(f"E{ep_number}")

    episode_title = parsed_file.get("episode_title")
    if episode_title:
        new_name_parts.append(f"- {episode_title}")

    renamed_file = " ".join(new_name_parts)
    LOGGER.info(f"Renamed file to {renamed_file}")
    return renamed_file
