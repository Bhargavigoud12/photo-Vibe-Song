<<<<<<< HEAD
import base64
import json
import requests

# Load credentials
def load_spotify_credentials(config_path: str = 'config/secrets.json') -> tuple:
    with open(config_path, 'r') as f:
        creds = json.load(f)
    return creds['client_id'], creds['client_secret']

# Get an access token using Client Credentials flow
def get_spotify_token(client_id: str, client_secret: str) -> str:
    auth_str = f"{client_id}:{client_secret}"
    b64_auth = base64.b64encode(auth_str.encode()).decode()
    headers = {
        'Authorization': f'Basic {b64_auth}',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = {'grant_type': 'client_credentials'}
    res = requests.post('https://accounts.spotify.com/api/token', headers=headers, data=data)
    res.raise_for_status()
    return res.json().get('access_token')

# Search tracks by mood and language
def search_spotify_song(mood: str, language: str, token: str, limit: int = 5) -> list:
    query = f"{mood} vibe {language}"
    headers = {'Authorization': f'Bearer {token}'}
    params = {'q': query, 'type': 'track', 'limit': limit}
    res = requests.get('https://api.spotify.com/v1/search', headers=headers, params=params)
    res.raise_for_status()
    items = res.json().get('tracks', {}).get('items', [])
    suggestions = []
    for track in items:
        name = track['name']
        artist = track['artists'][0]['name']
        preview = track.get('preview_url')  # 30s preview
        suggestions.append({'name': name, 'artist': artist, 'preview': preview})
=======
import base64
import json
import requests

# Load credentials
def load_spotify_credentials(config_path: str = 'config/secrets.json') -> tuple:
    with open(config_path, 'r') as f:
        creds = json.load(f)
    return creds['client_id'], creds['client_secret']

# Get an access token using Client Credentials flow
def get_spotify_token(client_id: str, client_secret: str) -> str:
    auth_str = f"{client_id}:{client_secret}"
    b64_auth = base64.b64encode(auth_str.encode()).decode()
    headers = {
        'Authorization': f'Basic {b64_auth}',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = {'grant_type': 'client_credentials'}
    res = requests.post('https://accounts.spotify.com/api/token', headers=headers, data=data)
    res.raise_for_status()
    return res.json().get('access_token')

# Search tracks by mood and language
def search_spotify_song(mood: str, language: str, token: str, limit: int = 5) -> list:
    query = f"{mood} vibe {language}"
    headers = {'Authorization': f'Bearer {token}'}
    params = {'q': query, 'type': 'track', 'limit': limit}
    res = requests.get('https://api.spotify.com/v1/search', headers=headers, params=params)
    res.raise_for_status()
    items = res.json().get('tracks', {}).get('items', [])
    suggestions = []
    for track in items:
        name = track['name']
        artist = track['artists'][0]['name']
        preview = track.get('preview_url')  # 30s preview
        suggestions.append({'name': name, 'artist': artist, 'preview': preview})
>>>>>>> 85c14a2a8ec9826ddfaf297010631cb5c821f1ca
    return suggestions