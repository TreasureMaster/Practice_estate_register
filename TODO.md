# FIXME Переработано частично

## Модели приложения

| Сущность        | Модель          |
| --------------- | --------------- |
| Здание          | Building        |
| Ответственный   | Chief           |
| Деканат         | Deanery         |
| Кафедра         | Department      |
| Помещение       | Hall            |
| Материал здания | Material        |
| Тип помещения   | Target          |
| Имущество       | Unit            |
| Пользователь    | User            |

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

[x] Создать проект
[x] Построить модели
[ ] Добавить обработчики с json-ответом
[ ] Протестировать работоспособность с Postman
[ ] Нормализация БД, если необходимо
[ ] Переделать обработчики для html-ответа

### Улучшения

- [ ] Переработать текстовое поле Address в Building. Возможно, выделить
    в отдельную таблицу или найти в pypi поле для адреса.
- [ ] Может быть переработать Year, Wear, Flow в поле Decimal. Или
    поискать на pypi соответствующие поля. Для Building.

### Проблемы реализации

- [x] Необходимо было создание поля, нечувствительного к регистру. Для этого нужно применить `CICharField` из модуля
      `django.contrib.postgres.fields`. Но во время миграции можно получить ошибку существования типа `citext`.
      Для этого нужно добавить в текущем файле миграций создание этого типа `CITextExtension()` из модуля
      `django.contrib.postgres.operations` **до** создания этого типа поля.
- [x] Поле модели, адаптированное под телефонный номер. Используем сторонний модуль `django-phonenumber-field`.
- [x] В админке создать фильтрацию поля (`list_filter`) как выпадающий список. Это можно реализовать с помощью
      стороннего модуля `django-admin-list-filter-dropdown`.
- [x] Выпадающий список в админке не отображается. Он будет отображаться только при количестве элементов поиска
      больше 4.
- [x] Фильтрация по полю пусто/не пусто (`NULL`/`NOT NULL`). Начиная с Django 3.1 есть фильтр `EmptyFieldListFilter`.
- [x] Фильтрация по полю пусто/значения. Все работает "из коробки". Описание проблемы смотри в первом пункте раздела
      *Ошибки кода и TODO* ниже.
- [x] Отображение внешнего вида поля `NULL` регулируется параметром `empty_value_display` в `ModelAdmin`.
- [x] Проблема десериализации JSON-запроса в модель Django, если модель содержит `ForeignKey`.
- [ ] Значения типа `Decimal` сериализуются в `string`.
- [x] Как объединить в hybrid property разные типы данных ? Можно использовать `Concate`. Но в данном случае
      нужна была еще и конструкиця `Case ... When`, поэтому было принято решение разделить данные и ввести
      еще одно дополнительное hybrid property для названия здания.

### Ошибки кода и TODO

- [x] Django возвращает ошибку `__str__ returned non-string (type NoneType)` в шаблоне. Достаточно простая ошибка:
      в одном из модулей написал `self.name` вместо `return self.name`. Ищется вертикально ориентированным поиском,
      т.е. отключаются методы `__str__()` в моделях, пока не будет найден тот, который генерирует ошибку.
- [x] Заполнение необязательных полей. На самом деле `blank=True` - это фактически `required=False` для формы.
      Первоначально думал, что оно допускает передачу пустого поля, н-р, `""`. Это не так.
- [x] Валидация полей `cost_year` и `cost_after` - не более `cost` и `start_year`. Сделано с помощью `clean_fields()`.
      Однако для `cost_after` не надо так валидировать, т.к. цена может и повыситься после переоценки.
- [x] Валидация поля `experience` - не более жизни человека. Просто стандартный `MaxValueValidator`.
- [x] Валидация `DecimalField` - не менее 0. Просто стандартный `MinValueValidator`.
- [x] Нужен возврат значения, подобного **hybrid_property** в SQLAlchemy.
- [ ] Уточнение текста ошибки при отсутствии `ForeignKey` в данных JSON.
- [ ] Оптимизация **hybrid_property** с помощью **functools.wraps**.
- [x] Объект типа ImageFieldFile не сериализуется JSON. Выполнено с помощью унификации - сериализации только `QuerySet`.
      Это создает лишний запрос к БД для POST и PATCH (простой запрос, по id), но устраняет избыточную логику в сериализаторе.
- [x] Были непроверенные ошибки в `patch()`. Решены унификацией запроса, перевод с `get()` на `filter()`.
- [x] Можно ли реализовать `hybrid_property` через `ExpressionWrapper` и объекты `F` ? Вполне реально просто через `F`.
- [x] Замена инициализации модели на `create()` ? Нет разницы с существующим вариантом, причем `create` не валидирует переданные данные.