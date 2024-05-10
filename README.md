# api_final
## Описание проекта.
Проект предназначен исключительно для обращения на эндпоинты API.
Можно добавлять посты, комментарии и подписываться на пользователей.
Создание пользователей осуществляется через обращение на эндпоинт API.

По API можно запросить такие данные, как:
- посты пользователей;
- подписки пользователя;
- группы постов;
- комментарии пользователей.

Действия:
- удаление, постов и комментариев;
- создание постов и комментариев;
- редактирование постов и комментариев;
- создание групп - только через админку;
- создание новых пользователей.

## Инструкция по запуску.
### Перед запуском проекта необходимо развернуть виртуальное окружение, например Venv:
1. Откройте терминал в нужной директории.
2. Введите команду:
    - `python -m venv venv` - для Windows.
    - `python3 -m venv venv` - для Mac и Linux.

_Второе 'venv' можно замнить на любое другое имя директории, для удобства лучше, если будет называться именем проекта._

3. Активируйте виртуальное окружение:
    - `source venv/Scripts/activate` - для Windows.
    - `source venv/bin/activate` - для Mac и Linux.

_Имя директории после 'source' - это название вашей директории с виртуальным окружением._

### Установите менеджер пакетов pip:
- `python -m pip install --upgrade pip` - для Windows.
- `python3 -m pip install --upgrade pip` - Mac и Linux.
### Установите все зависимости из файла requirments.txt:
- `pip install -r requirements.txt` - для Windows, Mac и Linux.
### Для того чтобы запустить проект локально, воспользуйтесь командой в терминале:
- `python manage.py runserver` - для Windows, Mac и Linux.

## Информация об авторе.
Блок API написан студентом [Берашевич Анной александровной](https://github.com/litanchick).
Постановка ТЗ и наполнение проекта: [Yandex-praktikum](https://github.com/yandex-praktikum).

## Примеры запросов и ответов.
### Создание поста.
![Static Badge](https://img.shields.io/badge/POST_запрос-blue)

`http://127.0.0.1:8000/api/v1/posts/`
```
{
    "text": "string",
    "image": "string",
    "group": 0
}
```
Ответ JSON:
```
{
    "id": 0,
    "author": "string",
    "text": "string",
    "pub_date": "2019-08-24T14:15:22Z",
    "image": "string",
    "group": 0
}
```
### Получение комментария.
![Static Badge](https://img.shields.io/badge/GET_запрос-green)

`http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/`

Ответ JSON:
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
### Примеры остальных запросов можно посмотреть [здесь](http://127.0.0.1:8000/redoc/).
