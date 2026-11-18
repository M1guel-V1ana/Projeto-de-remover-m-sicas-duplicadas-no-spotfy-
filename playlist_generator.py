"""Track collection and balanced playlist selection."""
import random
import config


def search_artist_tracks(spotify, artist, limit=None):
    limit = limit or config.TRACKS_PER_ARTIST_SEARCH
    response = spotify.search(
        q=f'artist:"{artist["name"]}"',
        type="track",
        limit=min(limit, 50),
        market=config.MARKET,
    )
    tracks = response.get("tracks", {}).get("items", [])
    artist_id = artist.get("id")
    return [
        track for track in tracks
        if track.get("uri")
        and any(credited.get("id") == artist_id for credited in track.get("artists", []))
    ]


def generate_balanced_playlist(artist_track_lists, total_tracks):
    pools = []
    seen = set()
    for artist, tracks in artist_track_lists:
        pool = []
        for track in tracks:
            uri = track.get("uri")
            if uri and uri not in seen:
                seen.add(uri)
                pool.append(track)
        random.shuffle(pool)
        pools.append({"artist": artist, "tracks": pool, "index": 0})

    selected = []
    # Round-robin keeps the selected artists reasonably balanced.
    while len(selected) < total_tracks:
        added = False
        for pool in pools:
            index = pool["index"]
            if index < len(pool["tracks"]) and len(selected) < total_tracks:
                selected.append(pool["tracks"][index])
                pool["index"] += 1
                added = True
        if not added:
            break
    return selected
