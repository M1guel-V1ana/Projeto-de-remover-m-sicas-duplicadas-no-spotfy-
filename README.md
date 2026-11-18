# Spotify Duplicate Cleaner

Script desenvolvido em Python para identificar músicas duplicadas em playlists do Spotify, utilizando a API oficial do Spotify.

O projeto busca facilitar a organização de playlists, identificando faixas repetidas e apresentando informações sobre as duplicatas encontradas.

## Objetivo

Desenvolver uma ferramenta capaz de analisar playlists do Spotify, identificar músicas duplicadas e, futuramente, automatizar sua remoção, mantendo apenas uma ocorrência de cada faixa.

## Funcionalidades

- Autenticação com a conta Spotify.
- Leitura de playlists.
- Identificação de músicas duplicadas por URI.
- Contagem de ocorrências repetidas.
- Exibição do nome da música e dos artistas.
- Análise sem alteração da playlist.

## Tecnologias utilizadas

- Python
- Spotipy
- Spotify Web API
- python-dotenv

## Como funciona

1. O usuário fornece o link da playlist.
2. O script extrai o ID da playlist.
3. A API do Spotify retorna as músicas presentes nela.
4. O script percorre as faixas e agrupa músicas com URIs iguais.
5. As duplicatas são identificadas e exibidas no terminal.

## Instalação

Clone o repositório:

```bash
git clone https://github.com/M1guel-V1ana/Projeto-de-remover-m-sicas-duplicadas-no-spotfy-.git
```

Entre na pasta:

```bash
cd Projeto-de-remover-m-sicas-duplicadas-no-spotfy-
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

## Configuração

Crie uma aplicação no [Spotify Developer Dashboard](https://developer.spotify.com/dashboard).

Configure as credenciais de acesso e o Redirect URI:

```text
http://127.0.0.1:8888/callback
```

Crie um arquivo `.env` na raiz do projeto:

```env
SPOTIFY_CLIENT_ID=seu_client_id
SPOTIFY_CLIENT_SECRET=seu_client_secret
```

## Execução

Execute o script:

```bash
python spotify_cleaner.py
```

Cole o link da playlist que deseja analisar quando solicitado.

## Segurança

- Armazene as credenciais em variáveis de ambiente.
- Não compartilhe seu Client Secret ou arquivo `.env`.
- O arquivo `.env` está listado no `.gitignore`.

## Próximas melhorias

- Remoção automatizada de músicas duplicadas.
- Confirmação antes de excluir faixas.
- Relatório detalhado das duplicatas.
- Exportação dos resultados para CSV.
- Interface gráfica para facilitar o uso.

## Licença

Este projeto está sob a licença MIT.
