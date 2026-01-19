import httpx

payload = {
  "email": "yashak.2001@mail.ru",
  "password": "qwertyyasha1"
}

login_request = httpx.post('http://localhost:8000/api/v1/authentication/login', json=payload)
login_response = login_request.json()
print(f'Ответ по запросу accessToken:{login_response}')

headers = {'Authorization': f'Bearer {login_response['token']["accessToken"]}'}
user_info_request = httpx.get('http://localhost:8000/api/v1/users/me', headers = headers)
user_info_response = user_info_request.json()
print(f'Статус код запроса: {user_info_request.status_code}')
print(f'Ответ по запросу информации о пользователе: {user_info_response}')

