# api_final
api final

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
установить и зарегистрировать в файле settings.py библиотеку djoser.
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

Получение
```
