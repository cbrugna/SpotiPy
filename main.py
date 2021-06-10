import requests
import time

from pprint import pprint

SPOTIFY_GET_CURRENT_TRACK_URL = 'https://api.spotify.com/v1/me/player'
SPOTIFY_ACCESS_TOKEN = 'BQAF-6EduekHsdvevOOetRhWCtVdIRqVU4D5XZ7QtvtV0rbGK9JQ1ZQOk-Pr4S35uSuJ11NEyZMWjtuZS3bgb9' \
                       '-23ZgwXFJWp2F8HuP516C_ZcEsolwkxqj5RVhUqx3WtuiRYVFXaCiZFM1IzDaRMDWUt7Fg89ORy8puNyXCqVrjsmTCV' \
                        '2K4L3d5u0pWPkm51ImAS93Ii1osns1-RSbFh_SQ '


def get_current_track(access_token):
    response = requests.get(
        SPOTIFY_GET_CURRENT_TRACK_URL,
        headers={
            "Authorization": f"Bearer {access_token}"
        }
    )
    json_resp = response.json()

    track_id = json_resp['item']['id']
    track_name = json_resp['item']['name']
    artists = json_resp['item']['artists']
    artists_names = ', '.join(
        [artist['name'] for artist in artists]
    )
    link = json_resp['item']['external_urls']['spotify']

    current_track_info = {
        "id": track_id,
        "name": track_name,
        "artists": artists_names,
        "link": link
    }

    return current_track_info


def main():
    current_track_id = None
    while True:
        current_track_info = get_current_track(SPOTIFY_ACCESS_TOKEN)

        if current_track_info['id'] != current_track_id:
            pprint(
                current_track_info,
                indent=4,
            )
            current_track_id = current_track_info['id']

        time.sleep(1)


if __name__ == "__main__":
    main()