По распоковочкам
в api_service/settings.py настройки подключения к БД DATABASES

python manage.py makemigrations
python manage.py migrate 
для генерации бдшечки

pip install requirements.txt
для подключения зависимостей

-------------------------------------------------
api:

-------------------
    api/ivents/
	(GET, POST) создание / вывод мероприятий (региональные партнёры добавляются отдельно)
{
        "name": "sdaf",
        "description": "f",
        "datebegin": "2002-01-02T03:24:00",
        "dateend": "2003-04-04T03:24:00",
        "place": "sddf",
        "img": null,
        "organizationId": 2
}

--------------------

    api/ivents/team/
	(POST) добавление команд в мероприятие
{
    "id_system_team": 1, (id команды)
    "ivent": 2 (id мероприятия)
}

-------------------

    api/ivents/teams/<int:pk>/
	(GET) вывод всех команд pk-id мероприятия

    api/ivents/ team/cat_ivents/<int:pk>/
	(GET) вывод всех мероприятий, в которых участвует команда

------------------

    api/ivents/regionalpartner/
	(POST) добавление региональных партнёров в мероприятие

{
    "id_system_partner": 1, (id партнёра)
    "ivent": 1 (id мероприятия)
}

-------------------

    api/ivents/regionalpartners/<int:pk>/
	(GET) вывод региональных партнёров мероприятия

