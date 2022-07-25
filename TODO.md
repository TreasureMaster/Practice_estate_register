# FIXME Пока не переработано

## Модели приложения

| Сущность        | Модель          |
| --------------- | --------------- |
| Пользователь    | User            |
| Материал здания | Material        |
| Тип помещения   | Target          |
| Кафедра         | Department      |
| Здание          | Building        |
| Помещение       | Hall            |
| Ответственный   | Chief           |
| Имущество       | Unit            |

> **_Примечание:_** Модель User и требуемое поведение уже встроено в Django.

## API приложения (исправить)

| HTTP    | Ресурс                  | Класс и метод               | Роль в доступе | Описание                           |
| ------- | ----------------------- | --------------------------- | -------------- | ---------------------------------- |
| GET     | Коллекция зданий        | BuildingListResource.get    | user           | Получает все здания
| POST    | Коллекция зданий        | BuildingListResource.post   | user           | Создает новое здание
| GET     | Здание                  | BuildingResource.get        | user           | Получает одно здание
| PATCH   | Здание                  | BuildingResource.patch      | user           | Обновляет одно здание
| DELETE  | Здание                  | BuildingResource.delete     | user           | Удаляет одно здание
| GET     | Коллекция кафедр        | DepartmentListResource.get  | user           | Получает все кафедры
| POST    | Коллекция кафедр        | DepartmentListResource.post | user           | Создает новую кафедру
| GET     | Кафедра                 | DepartmentResource.get      | user           | Получает одно кафедру
| PATCH   | Кафедра                 | DepartmentResource.patch    | user           | Обновляет одно кафедру
| DELETE  | Кафедра                 | DepartmentResource.delete   | user           | Удаляет одно кафедру
| GET     | Коллекция помещений     | HallListResource.get        | user           | Получает все помещения
| POST    | Коллекция помещений     | HallListResource.post       | user           | Создает новое помещение
| GET     | Помещение               | HallResource.get            | user           | Получает одно помещение
| PATCH   | Помещение               | HallResource.patch          | user           | Обновляет одно помещение
| DELETE  | Помещение               | HallResource.delete         | user           | Удаляет одно помещение
| GET     | Коллекция имущества     | UnitListResource.get        | user           | Получает все имущество
| POST    | Коллекция имущества     | UnitListResource.post       | user           | Создает новое имущество
| GET     | Имущество               | UnitResource.get            | user           | Получает одно имущество
| PATCH   | Имущество               | UnitResource.patch          | user           | Обновляет одно имущество
| DELETE  | Имущество               | UnitResource.delete         | user           | Удаляет одно имущество
| GET     | Коллекция ответственных | ChiefListResource.get       | user           | Получает всех ответственных
| POST    | Коллекция ответственных | ChiefListResource.post      | user           | Создает нового ответственного
| GET     | Ответственный           | ChiefResource.get           | user           | Получает одного ответственного
| PATCH   | Ответственный           | ChiefResource.patch         | user           | Обновляет одного ответственного
| DELETE  | Ответственный           | ChiefResource.delete        | user           | Удаляет одного ответственного
| GET     | Коллекция материалов    | MaterialListResource.get    | user           | Получает все материалы
| POST    | Коллекция материалов    | MaterialListResource.post   | user           | Создает новый материал
| DELETE  | Материал здания         | MaterialResource.delete     | user           | Удаляет материал
| GET     | Коллекция типов помещ.  | TargetListResource.get      | user           | Получает все типы помещений
| POST    | Коллекция типов помещ.  | TargetListResource.post     | user           | Создает новый тип помещения
| DELETE  | Типы помещений          | TargetResource.delete       | user           | Удаляет тип помещения
| GET     | Коллекция пользователей | UserListResource.get        | admin          | Получает всех сохраненных пользователей
| POST    | Коллекция пользователей | UserListResource.post       | admin          | Создает нового пользователя
| GET     | Пользователь            | UserResource.get            | admin          | Получает существующего пользователя
| PATCH   | Пользователь            | UserResource.patch          | admin          | Обновляет одного пользователя
| DELETE  | Пользователь            | UserResource.delete         | admin          | Удаляет одного пользователя


### Задачи практики

[ ] Создать проект
[ ] Построить модели
[ ] Добавить обработчики с json-ответом
[ ] Протестировать работоспособность с Postman
[ ] Нормализация БД, если необходимо
[ ] Переделать обработчики для html-ответа

### Проблемы реализации

- [x] Пока ничего нет

### Ошибки кода и TODO

- [x] Пока ничего нет