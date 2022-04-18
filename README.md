![](https://img.shields.io/badge/Python-3.8-blue) 
![](https://img.shields.io/badge/Django-2.2.16-green)
![](https://img.shields.io/badge/DjangoRestFramework-3.12.4-red)
<br><br>

# API YATUBE
API для проекта социальной сети YATUBE
## Описание
API зволяет отправлять и получать запросы в соответствии с ролями пользователей.
В API реализованы следующие классы:
- User - пользователь;
- Post - запись;
- Group - сообщество;
- Comment - комментарий;
- Follow - подписчик

Авторизация осуществляется на базе JWT-аутентификации на основе библиотек Djoser и SimpleJWT.
Подробная документация располагается по адресу http://127.0.0.1:8000/redoc/



### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/zerg959/api_yatube_final.git
```

```
cd api_yatube_final
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

```
source venv/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```
установить и зарегистрировать в файле settings.py библиотеку djoser.</br>
настроить urls.py
при регистрации необходимо обратить внимание на то, что пакет djoser располагается после
django.contrib.auth и rest_framework

```
в разделе REST_FRAMEWORK добавить:
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
```
Выполнить миграции в директории /yatube_api проекта:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```
Примеры выполнения запросов к api:

1. Получение отдельной записи:
```
GET http://127.0.0.1:8000/api/v1/posts/

```
```
{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
  ]
}
```
2. Получение комментария:

```
GET http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/
```
```
[
  {
    "id": 0,
    "author": "string",
    "text": "string",
    "created": "2019-08-24T14:15:22Z",
    "post": 0
  }
]
```
3. Получение списка сообществ:
```
GET http://127.0.0.1:8000/api/v1/groups/
```
```
[
  {
    "id": 0,
    "title": "string",
    "slug": "string",
    "description": "string"
  }
]
```
