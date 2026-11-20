# Mixify

**Your artists. Your mix. Your vibe.**

Mixify is a Python project for building personalized playlists from artists and music selected by the user, using Spotify's catalog.

## Product rules

- The user can add multiple artists.
- Every selected artist must contribute at least **one track**.
- The user chooses the desired number of tracks separately for each artist.
- Mixify imposes no arbitrary total-playlist-size limit.
- Duplicate tracks are identified by Spotify track URI and included only once.
- Tracks are interleaved between artists.
- If an artist has no available unique tracks, generation stops with a clear message.
- If fewer unique tracks are available than requested, Mixify uses the available tracks and reports the difference.

## Current MVP

- Spotify authentication.
- Artist search and confirmation.
- Paginated track search for each selected artist.
- Custom track quantity per artist.
- Minimum of one unique track per selected artist.
- URI-based duplicate prevention.
- Interleaved playlist generation.
- JSON preview export.

> The current MVP only creates a local JSON preview. It does not create, edit, or delete Spotify playlists.

## Planned features

- Search and select complete albums and EPs.
- Pick individual tracks.
- Combine artist, album, and track selections in one playlist.
- Create a new playlist in the user's Spotify account.
- Add tracks to Spotify playlists in API-compliant batches.
- Interface for reviewing and editing the playlist before saving.

## Technical notes and API limits

Mixify does not impose an arbitrary total playlist-size limit. Actual results depend on tracks available in Spotify's catalog and Spotify Web API restrictions. Search requests are paginated (up to 50 results per request); Spotify's Search API has an offset ceiling, so very large artist catalogs may require album-based catalog retrieval in a future iteration.

When playlist creation is implemented, tracks will be sent in batches that respect the API's per-request item limit. Large playlists will be processed in multiple requests.

## Requirements

- Python 3.10+
- Spotify Developer application
- Spotify account

## Setup

Clone the repository and enter its folder:

```bash
git clone https://github.com/M1guel-V1ana/Projeto-de-remover-m-sicas-duplicadas-no-spotfy-.git
cd Projeto-de-remover-m-sicas-duplicadas-no-spotfy-
```

Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a .env file in the project root:

```env
SPOTIFY_CLIENT_ID=your_client_id
SPOTIFY_CLIENT_SECRET=your_client_secret
```

The Spotify Developer Dashboard must contain this Redirect URI:

```
http://127.0.0.1:8888/callback
```

## Run

```bash
python main.py
```

Add artists, confirm each search result, and enter the number of tracks desired from each artist. Mixify generates an interleaved preview and saves it as playlist_preview.json.

## Project structure

```
main.py
spotify_client.py
artist_search.py
playlist_generator.py
playlist_manager.py
config.py
```

## Security

Never commit your .env file or share your Spotify Client Secret. Mixify uses Spotify catalog metadata and does not download audio.

## License

MIT
