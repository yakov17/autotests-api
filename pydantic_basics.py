"""
{
  "courses": [
    {
      "id": "string",
      "title": "string",
      "maxScore": 0,
      "minScore": 0,
      "description": "string",
      "previewFile": {
        "id": "string",
        "filename": "string",
        "directory": "string",
        "url": "https://example.com/"
      },
      "estimatedTime": "string",
      "createdByUser": {
        "id": "string",
        "email": "user@example.com",
        "lastName": "string",
        "firstName": "string",
        "middleName": "string"
      }
    }
  ]
}
"""


from pydantic import BaseModel, Field, ConfigDict
from pydantic.alias_generators import to_camel
import uuid

class FileSchema(BaseModel):
    id : str
    filename : str
    directory : str
    url : str

class UserSchema(BaseModel):
    id : str
    email : str
    last_name : str = Field(alias = 'lastName')
    first_name : str = Field(alias = 'firstName')
    middle_name : str = Field(alias = 'middleName')

    def get_username(self)-> str:
        return f'{self.last_name} {self.first_name} {self.middle_name}'

class CourseSchema(BaseModel):
    model_config = ConfigDict(alias_generator= to_camel, populate_by_name= True)
    id: str = Field(default_factory = lambda: str(uuid.uuid4()))
    title : str = 'Default Title'
    max_score : int = Field(alias = 'maxScore', default = 100)
    min_score : int = Field(alias = 'minScore',default = 10)
    description : str = 'Default Description'
    preview_file : FileSchema = Field(alias = 'previewFile')
    estimated_time : str = Field(alias = 'estimatedTime', default = '1 week')
    created_by_user : UserSchema = Field(alias = 'createdByUser')


course_default_model = CourseSchema(
    id = 'course-id',
    title = 'Default Title',
    maxScore = 100,
    minScore = 10,
    description = 'Default Description',
    estimatedTime = '1 week',
    previewFile = FileSchema(
        id = 'file-id',
        filename = 'file-name.jpg',
        directory = 'directory',
        url = 'http://localhost:8000'
    ),
    createdByUser = UserSchema(
        id = 'create-by-user-id',
        email = 'example@mail.com',
        lastName = 'Yakov',
        firstName = 'Kuznetsov',
        middleName = 'Alekseevich'
    )
)

print('Default model:', course_default_model)

course_dict = {
    "id": "course-id",
    "title": "Default Title",
    "maxScore": 100,
    "minScore": 10,
    "description": "Default Description",
    "previewFile": {
        "id": "file-id",
        "filename": "file-name.jpg",
        "directory": "directory",
        "url": "http://localhost:8000"
    },
    "estimatedTime": "1 week",
    "createdByUser": {
        "id": "create-by-user-id",
        "email": "yak@mail.ru",
        "lastName": "Lala",
        "firstName": "Lala",
        "middleName": "Lalal"
    }
}

course_dict_model = CourseSchema(**course_dict)
print('Course dict:', course_dict_model)

course_json = """
{
    "id": "course-id",
    "title": "Default Title",
    "maxScore": 100,
    "minScore": 10,
    "description": "Default Description",
    "previewFile": {
        "id": "file-id",
        "filename": "file-name.jpg",
        "directory": "directory",
        "url": "http://localhost:8000"
    },
    "estimatedTime": "1 week",
    "createdByUser": {
        "id": "create-by-user-id",
        "email": "yak@mail.ru",
        "lastName": "Lala",
        "firstName": "Lala",
        "middleName": "Lalal"
    }
}
"""

course_json_model = CourseSchema.model_validate_json(course_json)
print('Course JSON:', course_json_model)
print(course_json_model.model_dump(by_alias=True))
print(course_json_model.model_dump_json(by_alias=True))

user = UserSchema(
    id = 'user-id',
    email = '',
    lastName = 'Kak',
    firstName = 'Tak',
    middleName = 'To',
)

print(user.get_username())
