## Задание

Необходимо для имеющейся базы данных PostgreSql (в архиве имеется сама база данных, а также файл с описанием БД
и с готовой схемой данных, по которой создана БД) создать приложение с формами. В приложении должно быть две роли,
администратор (он может добавлять, редактировать и изменять пользователей) и сам пользователь, которому доступен
весь остальной функционал. Основной функционал программы – просмотр, редактирование, добавление/удаление данных +
печать отчета.

## ТЗ варианта

Разработать прикладное программное обеспечение для ведения реестра имущества университетского городка. В состав
имущества входит несколько зданий. В зданиях располагаются аудитории, кафедры, лаборатории, вычислительные центры,
деканаты и т. д. Любое помещение университета относится к какому-либо подразделению. Все движимое имущество, находящееся
в помещении, состоит на балансе материально ответственного лица. Каждая аудитория закреплена за определенной кафедрой
университета, так же в ведении кафедр находятся и лаборатории. По истечении определенного времени имущество, находящееся
в помещениях, списывается. Архив списанного имущества не ведется.

## Разработка

Разработка будет вестить согласно TODO. Каждая git-ветка соответствует варианту исполнения.

* [master] Главная ветка, где будет размещена финальная версия
* [dev] Ветка разработки
* [django] Перевод Flask-RESTful на Django (модели, JSON-ответ)
* [normalize] Нормализация таблиц БД, если необходимо
* [html] Заменить JSON-ответ на построение HTML-страниц
* Построение таблиц (django-tables2 ???)
* Нормализация таблиц
* Поисковые запросы
