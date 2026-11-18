"""Track collection and balanced playlist selection."""
import random
import config



def search_artist_tracks(spotify, artist, limit=None):
    limit = limit or config.TRACKS_PER_ARTIST_SEARCH
    query = f'artist:"{artist["name"]}"'
    response = spotify.search(
        q=query, type="track", limit=min(limit, 10), market=config.MARKET
    )
    tracks = response.get("tracks", {}).get("items", [])
    artist_id = artist.get("id")

    # Keep only tracks where the selected artist is actually credited.
    filtered = [
        track for track in tracks
        if any(credited.get("id") == artist_id for credited in track.get("artists", []))
        and track.get("uri")
    ]
    return filtered



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
    # Round-robin selection keeps artists reasonably balanced.
    while len(selected) < total_tracks:
        added_this_round = False
        for pool in pools:
            index = pool["index"]
            if index < len(pool["tracks"]) and len(selected) < total_tracks:
                selected.append(pool["tracks"][index])
                pool["index"] += 1
                added_this_round = True
        if not added_this_round:
            break
    return selected
