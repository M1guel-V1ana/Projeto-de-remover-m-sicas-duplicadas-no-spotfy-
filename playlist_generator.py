"Search artist catalogs and assemble personalized, duplicate-free playlists."
import random
import config


def search_artist_tracks(spotify, artist, limit):
    """Fetch up to limit tracks credited to the selected artist using pagination."""
    if limit < 1:
        return []

    artist_id = artist.get("id")
    found = []
    seen = set()
    offset = 0

    while len(found) < limit and offset <= config.SPOTIFY_SEARCH_MAX_OFFSET:
        page_limit = min(config.SEARCH_PAGE_SIZE, limit - len(found))
        response = spotify.search(
            q=f'artist:"{artist["name"]}"',
            type="track",
            limit=page_limit,
            offset=offset,
            market=config.MARKET,
        )
        page = response.get("tracks", {}).get("items", [])
        if not page:
            break

        for track in page:
            uri = track.get("uri")
            credited_ids = {item.get("id") for item in track.get("artists", [])}
            if uri and uri not in seen and artist_id in credited_ids:
                found.append(track)
                seen.add(uri)
                if len(found) >= limit:
                    break

        if len(page) < page_limit:
            break
        offset += len(page)

    return found


def generate_custom_playlist(artist_track_lists):
    """Select each artist's requested count, then interleave their tracks.

    Each item is (artist, tracks, requested_count). Every artist must
    contribute at least one unique track.
    """
    pools = []
    seen_uris = set()
    counts = {}

    for artist, tracks, requested_count in artist_track_lists:
        if requested_count < 1:
            raise ValueError(f"{artist.get('name', 'An artist')} must have at least one track.")

        unique_tracks = []
        for track in tracks:
            uri = track.get("uri")
            if uri and uri not in seen_uris:
                seen_uris.add(uri)
                unique_tracks.append(track)

        if not unique_tracks:
            raise ValueError(
                f"No unique tracks were found for {artist.get('name', 'an artist')}. "
                "Choose another artist or review the selected artists."
            )

        random.shuffle(unique_tracks)
        chosen = unique_tracks[:requested_count]
        counts[artist["id"]] = len(chosen)
        pools.append({"tracks": chosen, "index": 0})

    playlist = []
    while True:
        added = False
        for pool in pools:
            index = pool["index"]
            if index < len(pool["tracks"]):
                playlist.append(pool["tracks"][index])
                pool["index"] += 1
                added = True
        if not added:
            break

    return playlist, counts
