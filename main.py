"""Mixify MVP - generate a balanced playlist preview from selected artists."""
from artist_search import choose_artist
from playlist_generator import search_artist_tracks, generate_balanced_playlist
from playlist_manager import export_playlist_preview
from spotify_client import create_spotify_client


def collect_artists(spotify):
    selected = []
    print("Enter artist names. Leave blank when you are done.")
    while True:
        name = input("\\nArtist name: ").strip()
        if not name:
            break
        artist = choose_artist(spotify, name)
        if artist and all(existing.get("id") != artist.get("id") for existing in selected):
            selected.append(artist)
            print(f"Added: {artist['name']}")
        elif artist:
            print("Artist already selected.")
    return selected


def main():
    print("=== Mixify ===")
    print("Your artists. Your mix. Your vibe.\\n")
    spotify = create_spotify_client()
    artists = collect_artists(spotify)
    if not artists:
        print("No artists selected. Exiting.")
        return

    while True:
        raw = input("\\nHow many tracks do you want in the playlist? ").strip()
        if raw.isdigit() and int(raw) > 0:
            total_tracks = int(raw)
            break
        print("Enter a positive whole number.")

    artist_track_lists = []
    for artist in artists:
        print(f"\\nSearching tracks for {artist['name']}...")
        tracks = search_artist_tracks(spotify, artist, limit=50)
        print(f"Found {len(tracks)} usable tracks.")
        artist_track_lists.append((artist, tracks))

    playlist = generate_balanced_playlist(artist_track_lists, total_tracks)
    if not playlist:
        print("No tracks could be selected. Try different artists.")
        return

    filename = export_playlist_preview(playlist)
    print("\\n=== MIXIFY PREVIEW ===")
    print(f"Selected artists: {', '.join(a['name'] for a in artists)}")
    print(f"Tracks requested: {total_tracks}")
    print(f"Tracks selected: {len(playlist)}")
    print(f"Preview saved to: {filename}")
    print("\\nThis MVP does not create or modify Spotify playlists yet.")
    for number, track in enumerate(playlist, start=1):
        artist_names = ", ".join(a.get("name", "") for a in track.get("artists", []))
        print(f"{number:02d}. {track.get('name')} — {artist_names}")


if __name__ == "__main__":
    main()
