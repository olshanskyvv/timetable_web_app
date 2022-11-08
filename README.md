# RUT Timetable

## Техническое задание

На сайте можно будет посмотреть в удобном формате рассписание своей группы, с возможностью оставлять заметки (ДЗ) к каждой паре

### Стек технологий и формат

Формат: WEB Application

**Основной язык разработки:** 
- HTML5
- CSS
- Django Python

**Вспомогательные технолигии:**
- Git (репозиторий на GitHub)
- База данных SQLite3 (интегрированная в Django)

**Источники данных:** [Сайт с расписанием РУТ(МИИТ)](https://rut-miit.ru/timetable/)

### Функционал

Изначально пользователь будет попадать на страницу с кратким описанием проекта: его возможностями, целями, авторами.
С этой страницы он сможет перейти на страницы регистрации и входа для регистрации и входа соответственно.
После аутентификации пользователя будет перенаправлять на главную страницу сайта, 
где и будет располагаться расписание в удобном для восприятия формате.

### Дизайн
В разработке

### Установка репозитория

*Рекомендуемая среда разработки:* PyCharm

Подразумевается, что Python и пакетный менеджер pip уже установлены на Вашем ПК

Установка и первичная настройка:

1. Скачиваем, устанавливаем и запускаем PyCharm
2. Выбираем для открытия Get from VCS, вставляем `https://github.com/olshanskyvv/timetable_web_app.git` и клонируем репозиторий
3. Создаем виртуальное окружение командой: `python3 -m venv venv`. Для Windows будет достаточно написать `python`
4. Устанавливаем необходимые для работы библиотеки: `pip3 install django beautifulsoup4 lxml requests`. Аналогично пункту 3, на Windows будет достаточно использовать `pip`
5. В консоли (терминале) вводим: `cd timetable`
6. Устанавливаем миграции: `python3 manage.py migrate`

Теперь терминал готов к работе!

Для запуска сервера достаточно выполнить команду:
`python3 manage.py runserver`

*Сервер готов к использованию!*

Для удобного администрирования сайта необходим администратор. Для создания такого пользователя выполним команду
`python3 manage.py createsuperuser`. Далее достаточно заполнить поле имя пользователя и пароль.

Всё, админ готов. Можно выполнить вход через эту учетную запись, только сайт будет работать не корректно, 
так как не заполнены поля имени или фамилии и номера группы. 
Для этого в адресной строке на странице расписания вместо timetable вписываем profile и запоняем данные.

Теперь у нас есть администратор, на котором сайт работает корректно.

#### Администрирование

Для перехода в админпанель Django достаточно перейти на страницу с адресом admin
