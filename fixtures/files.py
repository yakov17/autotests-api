import pytest
from pydantic import BaseModel

from clients.files.files_client import get_files_client, FilesClient
from clients.files.files_schema import CreateFileRequestSchema
from clients.users.users_schema import CreateUserResponseSchema
from fixtures.users import UserFixture

@pytest.fixture
def files_client(function_user : UserFixture) -> FilesClient:
    return get_files_client(function_user.authentication_user)

class FileFixture(BaseModel):
    request : CreateFileRequestSchema
    response : CreateUserResponseSchema

@pytest.fixture
def function_file(files_client : FilesClient):
    request = CreateFileRequestSchema(upload_file=r'C:\Users\Яков\Desktop\Stepik\autotests\testdata\courses\test.png')
    response = files_client.create_file(request)
    return FileFixture(request = request, response=response)
