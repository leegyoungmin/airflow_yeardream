import requests

client_id = 'ee73495505d25ff4a8a8cc3c88af239f'
redirect_uri = 'https://gyoungmin.com/oauth'
authorize_code = 'vyCl26aQ7h6NsC4la2tcfowmv3689FO_0xlfCwcEDj8ZW4LNKOR-0QAAAAQKKcleAAABkC34SHYh5oEAb4_jFQ'

token_url = 'https://kauth.kakao.com/oauth/token'
data = {
    'grant_type': 'authorization_code',
    'client_id': client_id,
    'redirect_uri': redirect_uri,
    'code': authorize_code,
}

response = requests.post(url=token_url, data=data)
tokens = response.json()
print(tokens)