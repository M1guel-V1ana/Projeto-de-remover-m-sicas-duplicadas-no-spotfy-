# Mixify

**Your artists. Your mix. Your vibe.**

Mixify is a Python project that combines artists chosen by the user and generates a personalized playlist from Spotify catalog search results.

## MVP

- Authenticate with Spotify using OAuth.
- Search for artists and let the user confirm the correct result.
- Search tracks for selected artists.
- Avoid duplicate tracks by Spotify URI.
- Balance tracks across artists (round-robin selection).
- Export the generated selection to JSON for review.

> Playlist creation inside Spotify is planned for a later step. This MVP does not modify any Spotify playlist.

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

Create a `.env` file in the project root:

```env
SPOTIFY_CLIENT_ID=your_client_id
SPOTIFY_CLIENT_SECRET=your_client_secret
```

In Spotify Developer Dashboard, configure this Redirect URI:

```
http://127.0.0.1:8888/callback
```

## Run

```bash
python main.py
```

Enter artist names one by one. Select the matching artist from Spotify search results, choose the desired number of tracks, and Mixify will create a balanced selection and export it to `playlist_preview.json`.

## Project structure

```
main.py
spotify_client.py
artist_search.py
playlist_generator.py
playlist_manager.py
config.py
```

## Roadmap

- [x] Spotify OAuth connection
- [x] Artist search and confirmation
- [x] Track search for selected artists
- [x] URI-based duplicate prevention
- [x] Balanced track selection
- [x] JSON preview export
- [ ] Create a playlist in Spotify
- [ ] Playlist name and description customization
- [ ] Streamlit interface
- [ ] More playlist selection controls

## Security

Never commit your `.env` file or share your Spotify Client Secret. Spotify catalog metadata is used only to help users select music; the project does not download Spotify audio.

## License

MIT
