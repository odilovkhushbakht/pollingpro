
Функционал для администратора системы:

http://127.0.0.1:8000/admin/ метод GET получить список опросов

http://127.0.0.1:8000/admin/polling-post/ метод POST создание опроса
Пример:
{
    "start_date": "2022-01-16",
    "name": "Polling 1",
    "finished_date": "2022-01-30",
    "description": "description Polling 1",
    "status": true,
    "number": 1
}
Все поля обязательны для заполнения.
"number" должен быть уникальным.


http://127.0.0.1:8000/admin/polling-update/ метод POST обновления опроса
Пример:
{
    "id": 9,
    "name": "Polling 4",
    "finished_date": "2022-01-30",
    "description": "description Polling 4",
    "status": true
}
Выборка опроса через поле id.
Все поля кроме id обновляется.

http://127.0.0.1:8000/admin/polling-delete/ метод DELETE удалить опрос
Пример:
{
    "id": 10
}


http://127.0.0.1:8000/admin/question/ метод GET получить список вопросов

http://127.0.0.1:8000/admin/question-post/ метод POST создать вопрос
Пример 1:
{
    "text": "Вопрос",
    "style": 1,
    "parent": 1
}
Поля "text" и "style" обязательны для заполнения.
Поле "style" тип вопроса ответ текстом.

Пример 2:
{
    "text": "Вопрос",
    "style": 2,
    "answer_multi_1": "вариант 1",
    "answer_multi_2": "вариант 2",
    "answer_multi_3": "вариант 3",
    "answer_multi_4": "вариант 4",
    "parent": 1
}
Поля "text","style","answer_multi_1","answer_multi_2","answer_multi_3","answer_multi_4"  обязательны для заполнения.
Поле "style" тип вопроса ответ выбор один из вариантов.

Пример 3:
{
    "text": "Вопрос",
    "style": 3,
    "answer_multi_1": "вариант 1",
    "answer_multi_2": "вариант 2",
    "answer_multi_3": "вариант 3",
    "answer_multi_4": "вариант 4",
    "parent": 1
}
Поля "text","style","answer_multi_1","answer_multi_2","answer_multi_3","answer_multi_4"  обязательны для заполнения.
Поле "style" тип вопроса ответ выбор несколько вариантов.


http://127.0.0.1:8000/admin/question-update/ метод POST обновления вопроса
Пример:
{
    "id": 1,
    "text": "Вопрос",
    "style": 2,
    "answer_multi_1": "вариант 1",
    "answer_multi_2": "вариант 2",
    "answer_multi_3": "вариант 3",
    "answer_multi_4": "вариант 4",
    "parent": 2
}
Выборка вопроса через id.

Пример 2:
{
    "id": 2,
    "text": "Вопрос",
    "style": 1,
    "parent": 2
}
Выборка вопроса через id.


http://127.0.0.1:8000/admin/question-delete/ метод DELETE удалить вопрос.
Пример:
{
    "id": 2
}
Выборка вопроса через id.


Функционал для пользователей системы:

http://127.0.0.1:8000/back/ метод GET. Получить список активных опросов.

http://127.0.0.1:8000/back/regis/ метод POST. Получить id.
Пример:
{
    "first_name": "first_name",
    "last_name": "last_name"
}
В ответ получите id. Можно анонимно получить id просто отправить запрос по этой ссылке http://127.0.0.1:8000/back/regis/.

http://127.0.0.1:8000/back/polling/ метод GET. Ответить на вопросы для этого нужно в заголовок запроса добавить "user-id", значением должен ваш id.

http://127.0.0.1:8000/back/order/ метод GET. Получение пройденных пользователем опросов с детализацией по ответам в заголовок запроса добавить "user-id", значением должен ваш id.