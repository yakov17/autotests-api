from clients.api_client import APIClient
from typing import TypedDict
from httpx import Response

"""
    Описание структуры запроса на аутентификацию.
    """

class LoginResponse(TypedDict):
    email: str
    password: str
 """
    Описание структуры запроса для обновления токена.
    """
class RefreshRequestDict(TypedDict):
    refreshToken: str

"""
   Клиент для работы с /api/v1/authentication
   """
class AuthenticationClient(APIClient):

    def login_api(self, request: LoginResponse) -> Response:
        return self.post("/api/v1/authentication/login", json=request)

    """
            Метод обновляет токен авторизации.

            :param request: Словарь с refreshToken.
            :return: Ответ от сервера в виде объекта httpx.Response
            """

    def refresh_api(self, request: RefreshRequestDict) -> Response:
        return self.post("/api/v1/authentication/refresh", json=request)

    """
            Метод обновляет токен авторизации.

            :param request: Словарь с refreshToken.
            :return: Ответ от сервера в виде объекта httpx.Response
            """