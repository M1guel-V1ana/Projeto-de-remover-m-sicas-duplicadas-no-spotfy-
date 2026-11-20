"Mixify MVP: personalized playlist preview from selected artists."
from artist_search import choose_artist
from playlist_generator import search_artist_tracks, generate_custom_playlist
from playlist_manager import export_playlist_preview
from spotify_client import create_spotify_client


def ask_track_count(artist_name):
    while True:
        raw = input(f"How many tracks do you want from {artist_name}? ").strip()
        if raw.isdigit() and int(raw) >= 1:
            return int(raw)
        print("Choose at least 1 track for each artist.")


def collect_artists(spotify):
    selected = []
    print("Add artists one by one. Press Enter on an empty name when finished.")
    while True:
        name = input("Artist name: ").strip()
        if not name:
            break
        artist = choose_artist(spotify, name)
        if not artist:
            continue
        if any(item["id"] == artist["id"] for item in selected):
            print("This artist is already in your selection.")
            continue
        selected.append(artist)
        print(f"Added: {artist['name']}")
    return selected


def main():
    print("=== Mixify ===")
    print("Your artists. Your mix. Your vibe.")
    spotify = create_spotify_client()
    artists = collect_artists(spotify)
    if not artists:
        print("No artists selected. Exiting.")
        return

    preferences = [(artist, ask_track_count(artist["name"])) for artist in artists]
    artist_track_lists = []

    for artist, desired_count in preferences:
        print(f"Searching tracks for {artist['name']}...")
        search_limit = min(1000, desired_count + 50)
        tracks = search_artist_tracks(spotify, artist, limit=search_limit)
        print(f"Found {len(tracks)} tracks credited to {artist['name']}.")
        artist_track_lists.append((artist, tracks, desired_count))

    try:
        playlist, counts = generate_custom_playlist(artist_track_lists)
    except ValueError as error:
        print(f"Could not generate playlist: {error}")
        return

    for artist, desired_count in preferences:
        actual = counts[artist["id"]]
        if actual < desired_count:
            print(f"Notice: {artist['name']} requested {desired_count}, but only {actual} unique tracks were available.")

    filename = export_playlist_preview(playlist)
    print("\n=== MIXIFY PREVIEW ===")
    print(f"Selected artists: {len(artists)}")
    print(f"Total tracks selected: {len(playlist)}")
    print(f"Preview saved to: {filename}")
    print("This MVP exports a preview; it does not create or modify Spotify playlists.")
    for number, track in enumerate(playlist, start=1):
        names = ", ".join(item.get("name", "") for item in track.get("artists", []))
        print(f"{number:04d}. {track.get('name')} — {names}")


if __name__ == "__main__":
    main()
