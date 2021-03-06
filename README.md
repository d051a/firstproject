# Описание
Первый проект [@PythonNoobs](https://t.me/python_noobs)
help_desk &amp; service_desk system

# Requirements / Требования
Django==1.11

# Installation / Установка
- Open the command line, navigate to the django app folder and execute:
- virtualenv *virtualenvname*
- Clone this repository to virtualenv folder
- Linux: source *virtualenvname*/bin/activate, Windows: call *virtualenvname*/Scripts/activate.bat
- pip install -r requirements.txt
- move to cloned repository folder
- python manage.py makemigrations
- python manage.py migrate
- python manage.py createsuperuser
- python manage.py runserver
# load Dump-data / Установка
- python manage.py loaddata dump_groups.json
- python manage.py loaddata dump_groups_perms.json
- python manage.py loaddata dump_holidays.json
- python manage.py loaddata dump_maindata.json
# runserver / запуск серевера
- Open http://127.0.0.1:8000/ in web browser.

# Основные подсистемы и фичи:
## Система заявок(ticketsapp)
- страница создания новой заявки. На странице указываются общая проблема, ее категория, описание, статус. При выборе проблем связанных с компьютером, сервером, или КМТ, должна осуществляться привязка к соответствующей модели.
- страница изменения заявки
- страница всех зарегистрированных в системе заявок. Вывод информации осуществляется в табличном виде всех зарегистрированных заявок с указанием параметров определенных в модели

## Реестр серверов(serverapp)
- страница с выводом всех позиций техники. Вывод информации осуществляется в табличном виде всех серверов с указанием параметров определенных в модели
- страница добавления нового сервера с формой для добавления основных параметров
- страница(карточка) сервера с формой ввода основных параметров и перечнем заявок для этого сервера

## Реестр копировально-множительной техники(КМТ)(cmtapp)
- страница с выводом всех позиций техники. Вывод информации осуществляется в табличном виде всей КМТ с указанием параметров определенных в модели
- страница добавления новой КМТ с формой для добавления параметров определенных в модели
- страница(карточка) КМТ с формой для редактирования параметров определенных в модели и перечнем заявок для этой КМТ

## Реестр компьютеров(workstationsapp)
- страница с выводом всех позиций техники. Вывод информации осуществляется в табличном виде всех компьютеров с указанием параметров определенных в модели
- страница добавления нового компьютера с формой для добавления параметров определенных в модели
- страница(карточка) компьютера с формой для редактирования параметров определенных в модели и перечнем заявок для этого комьпютера

## Реестр пользователей(employeesapp)
- страница с выводом всех позиций сотрудников. Вывод информации осуществляется в табличном виде всех пользователей с указанием параметров определенных в модели
- страница добавления нового пользователя с формой для добавления параметров определенных в модели
- страница(карточка) пользователя с формой для редактирования параметров определенных в модели и перечнем заявок для этого комьпютера

## Подсистема администрирования(adminapp)
...
## Подсистема авторизации(authapp)
- страница личного кабинета сотрудника
...

# Схема моделей:
