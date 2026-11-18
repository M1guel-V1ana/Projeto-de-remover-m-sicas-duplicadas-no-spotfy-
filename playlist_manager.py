"""Playlist preview export. Spotify playlist writing is not enabled yet."""
import json
from pathlib import Path



def export_playlist_preview(tracks, filename="playlist_preview.json"):
    preview = [
        {
            "name": track.get("name"),
            "artists": [artist.get("name") for artist in track.get("artists", [])],
            "uri": track.get("uri"),
            "spotify_url": track.get("external_urls", {}).get("spotify"),
        }
        for track in tracks
    ]
    Path(filename).write_text(
        json.dumps(preview, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    return filename
