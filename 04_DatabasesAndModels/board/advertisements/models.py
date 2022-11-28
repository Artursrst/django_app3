from django.db import models
'''
Создать главную страницу, вывести хоть что-нибудь по адресу /advertisements
'''

# Доработайте модель объявления: добавьте поля: описание, цена, дата публикации, дата окончания публикации.

# Создайте модель для хранения контактной информации об авторе объявления. (Обязательные поля: имя, электронная почта, телефон).

# Свяжите модели объявления и автора связью один-ко-многим так, чтобы у одного автора могло быть несколько объявлений.

# Добавьте модель для хранения рубрики объявления (Возможные значения: Авто, Недвижимость, Работа), поля: наименование.

# Свяжите рубрику с объявлением с использованием связи вида один-ко-многим.

# Реализуйте вывод списка объявлений по адресу /advertisements в формате:
# Заголовок | Цена | Наименование рубрики

'''
При нажатии на заголовок должен произойти переход на детальную страницу объявления, на которой должны быть представлены следующие данные:

Заголовок
Цена
Описание
Рубрика
Тип объявления
Контактная информация 
Количество просмотров

По умолчанию цена должна отображаться в рублях, рядом можно разместить цену в долларах по курсу ЦБ.'''


class Advertisement(models.Model):
    title = models.CharField(max_length=1000, db_index=True)
    description = models.CharField(max_length=10000)
    created_at = models.DateTimeField(auto_now_add=True)
    ended_at = models.DateTimeField()
    price = models.FloatField(verbose_name='цена', default=0)
    views_count = models.IntegerField(verbose_name='количетсов просмотров', default=0)
    author = models.ForeignKey('AuthorInformation', default=None, null=True, on_delete=models.DO_NOTHING)
    heading = models.ForeignKey('Headings', default=None, null=True, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'advertisements'

class AuthorInformation(models.Model):
    name = models.CharField(max_length=1000, db_index=True)
    email = models.CharField(max_length=1000)
    phone_number = models.CharField(max_length=1000)

class Headings(models.Model):
    title = models.CharField(max_length=1000, db_index=True)