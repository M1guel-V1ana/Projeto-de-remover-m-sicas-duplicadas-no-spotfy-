import os
from collections import defaultdict

import spotipy
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
REDIRECT_URI = "http://127.0.0.1:8888/callback"

SCOPE = (
    "playlist-read-private "
    "playlist-read-collaborative "
    "playlist-modify-private "
    "playlist-modify-public"
)


def criar_cliente_spotify():
    if not CLIENT_ID or not CLIENT_SECRET:
        raise RuntimeError(
            "Credenciais ausentes. Configure SPOTIFY_CLIENT_ID e "
            "SPOTIFY_CLIENT_SECRET no arquivo .env."
        )

    return spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            redirect_uri=REDIRECT_URI,
            scope=SCOPE,
        )
    )


def obter_id_playlist(link):
    return link.split("/")[-1].split("?")[0]


def obter_musicas(spotify, playlist_id):
    musicas = []
    resultado = spotify.playlist_items(playlist_id, limit=100)

    while resultado:
        musicas.extend(resultado.get("items", []))

        if resultado.get("next"):
            resultado = spotify.next(resultado)
        else:
            break

    return musicas


def identificar_duplicatas(musicas):
    ocorrencias = defaultdict(list)

    for indice, item in enumerate(musicas):
        faixa = item.get("track")

        # Ignora itens removidos, indisponíveis ou sem URI.
        if not faixa or not faixa.get("uri"):
            continue

        uri = faixa["uri"]
        ocorrencias[uri].append(
            {
                "indice": indice,
                "nome": faixa.get("name", "Nome desconhecido"),
                "artistas": ", ".join(
                    artista.get("name", "")
                    for artista in faixa.get("artists", [])
                ),
            }
        )

    return {
        uri: itens
        for uri, itens in ocorrencias.items()
        if len(itens) > 1
    }


def main():
    spotify = criar_cliente_spotify()

    link = input("Cole o link da playlist: ").strip()
    playlist_id = obter_id_playlist(link)

    print("\nBuscando músicas na playlist...")
    musicas = obter_musicas(spotify, playlist_id)
    print(f"Total de itens encontrados: {len(musicas)}")

    duplicatas = identificar_duplicatas(musicas)

    if not duplicatas:
        print("\nNenhuma duplicata encontrada.")
        return

    print("\n=== DUPLICATAS ENCONTRADAS ===")
    total_repeticoes_extras = 0

    for ocorrencias in duplicatas.values():
        primeira = ocorrencias[0]
        repeticoes_extras = len(ocorrencias) - 1
        total_repeticoes_extras += repeticoes_extras

        print(f"\nMúsica: {primeira['nome']}")
        print(f"Artista(s): {primeira['artistas']}")
        print(f"Ocorrências na playlist: {len(ocorrencias)}")
        print(f"Cópias extras: {repeticoes_extras}")

    print("\n==============================")
    print(f"Faixas com duplicatas: {len(duplicatas)}")
    print(f"Total de cópias extras: {total_repeticoes_extras}")
    print("==============================")
    print("Modo de análise: nenhuma faixa foi removida.")


if __name__ == "__main__":
    main()
