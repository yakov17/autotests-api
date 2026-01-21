import httpx
from facker import fake_info

payload = fake_info()

response_user = httpx.post('http://localhost:8000/api/v1/users', json=payload)
response_user_data= response_user.json()

print('Status code', response_user.status_code)
print('Response user', response_user_data)

payload_login = {
  "email": payload['email'],
  "password": payload['password']
}


response_token = httpx.post('http://localhost:8000/api/v1/authentication/login', json=payload_login)
response_token_data = response_token.json()
print(f'Status code', response_token.status_code)
print(f'Response token', response_token_data)

payload_update = fake_info()
headers = {
    'Authorization' :f'Bearer {response_token_data['token']["accessToken"]}'}

update_user = httpx.patch(f'http://localhost:8000/api/v1/users/{response_user_data['user']["id"]}', json=payload_update, headers = headers)
update_user_data = update_user.json()
print(f'Status code', update_user.status_code)
print(f'Response user', update_user_data)








