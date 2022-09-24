# Описание встреченных особенностей (документация)

## Функции БД

### Функции сравнения и преобразования

**Cast** - заставляет тип результата *expression* быть типом результата из *output_field*.

```python
Author.objects.annotate(age_as_float=Cast('age', output_field=FloatField()))
```

## Условные выражения

__When(condition=None, then=None, **lookups)__ - используется для инкапсуляции условия и его результата
в условном выражении. Использование `When()` аналогично использованию `filter()`. Условие может быть
задано с помощью объектов `field lookup`, `Q` или `Expression`, у которых `output_field` является `BooleanField`.
Результат выдается с помощью ключевого слова `then`.

```python
>>> from django.db.models import F, Q, When
>>> # Строковые аргументы относятся к полям; следующие два примера эквивалентны:
>>> When(account_type=Client.GOLD, then='name')
>>> When(account_type=Client.GOLD, then=F('name'))
>>> # Вы можете использовать поиск полей в условии
>>> from datetime import date
>>> When(registered_on__gt=date(2014, 1, 1),
...      registered_on__lt=date(2015, 1, 1),
...      then='account_type')
>>> # Сложные условия могут быть созданы с использованием объектов Q
>>> When(Q(name__startswith="John") | Q(name__startswith="Paul"),
...      then='name')
>>> # Условие может быть создано с использованием логических выражений.
>>> from django.db.models import Exists, OuterRef
>>> non_unique_account_type = Client.objects.filter(
...     account_type=OuterRef('account_type'),
... ).exclude(pk=OuterRef('pk')).values('pk')
>>> When(Exists(non_unique_account_type), then=Value('non unique'))
>>> # Условие может быть создано с помощью выражений поиска.
>>> from django.db.models.lookups import GreaterThan, LessThan
>>> When(
...     GreaterThan(F('registered_on'), date(2014, 1, 1)) &
...     LessThan(F('registered_on'), date(2015, 1, 1)),
...     then='account_type',
... )
```

> **_Примечание:_** Поскольку аргумент ключевого слова `then` зарезервирован для результата `When()`, существует потенциальный конвликт, если модель имеет поле с именем `then`. Это можно решить 2 способами:

```python
When(then__exact=0, then=1)
When(Q(then=0), then=1)
```

__Case(*cases, **extra)__ - подобно выражению `if ... elif ... else` в Python. Условие каждого объекта `When()`
оценивается по порядку, пока один из них не будет оценен как истинное значение.
Возвращается результат из соответствующего объекта `When()`.

```python
>>> # Получите скидку для каждого Клиента в зависимости от типа счета
>>> Client.objects.annotate(
...     discount=Case(
...         When(account_type=Client.GOLD, then=Value('5%')),
...         When(account_type=Client.PLATINUM, then=Value('10%')),
...         default=Value('0%'),
...     ),
... ).values_list('name', 'discount')
```

`Case()` принимает любое количество `When()` в качестве отдельных аргументов. Другие опции предоставляются
с помощью аргументов с ключевыми словами. Если ни одно из условий не соответствует `True`, то возвращается
выражение, заданное аргументом `default`. Если аргумент `default` не указан, используется `None`.

`Case()` также работает в предложении `filter()`.

```python
>>> a_month_ago = date.today() - timedelta(days=30)
>>> a_year_ago = date.today() - timedelta(days=365)
>>> Client.objects.filter(
...     registered_on__lte=Case(
...         When(account_type=Client.GOLD, then=a_month_ago),
...         When(account_type=Client.PLATINUM, then=a_year_ago),
...     ),
... ).values_list('name', 'account_type')
```

Ссылка на [примеры использования](https://django.fun/ru/docs/django/4.0/ref/models/conditional-expressions/).
