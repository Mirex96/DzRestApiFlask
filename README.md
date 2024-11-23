# Инструкция по запуску

1. Активируйте виртуальное окружение:

```bash
source venv/bin/activate


2. Запустите сервер:
python app.py


# Примеры запросов

## Создание пользователя
- Метод: POST
- URL: /users
- Тело запроса:
  ```json
  {
    "username": "example_user",
    "email": "user@example.com"
  }

Создание поста
Метод: POST
URL: /posts
Тело запроса:
{
  "user_id": 1,
  "title": "My First Post",
  "content": "This is the content of the post."
}
Получение всех постов
Метод: GET
URL: /posts
Обновление поста
Метод: PUT
URL: /posts/{post_id}
Тело запроса:
{
  "title": "Updated Title",
  "content": "Updated content of the post."
}
Удаление поста
Метод: DELETE
URL: /posts/{post_id}
