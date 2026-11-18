"""Artist search and confirmation helpers."""

def search_artists(spotify, name, limit=5):
    response = spotify.search(q=name, type="artist", limit=limit, market="BR")
    return response.get("artists", {}).get("items", [])


def choose_artist(spotify, name):
    results = search_artists(spotify, name)
    if not results:
        print(f"No artists found for: {name}")
        return None

    print(f"\nArtist results for '{name}':")
    for index, artist in enumerate(results, start=1):
        genres = ", ".join(artist.get("genres", [])[:3]) or "Genre unavailable"
        print(f"{index}. {artist['name']} — {genres}")

    while True:
        choice = input("Choose an artist number (0 to cancel): ").strip()
        if choice == "0":
            return None
        if choice.isdigit() and 1 <= int(choice) <= len(results):
            return results[int(choice) - 1]
        print("Invalid selection. Try again.")
