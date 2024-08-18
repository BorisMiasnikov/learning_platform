from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from django.db import models

from courses.models import Course


class CustomUser(AbstractUser):
    """Кастомная модель пользователя - студента."""

    email = models.EmailField(
        verbose_name='Адрес электронной почты',
        max_length=250,
        unique=True
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = (
        'username',
        'first_name',
        'last_name',
        'password'
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('-id',)

    def __str__(self):
        return self.get_full_name()


class Balance(models.Model):
    """Модель баланса пользователя."""

    balance = models.IntegerField(
        default=1000,
        validators=[MinValueValidator(0)]
    )
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE
    )

    def change_balance(self, value:int)->int:
        user = AbstractUser.objects.filter(id=self.user)
        if user.is_stuff:
            self.balance = value
            return self.balance

    class Meta:
        verbose_name = 'Баланс'
        verbose_name_plural = 'Балансы'
        ordering = ('-id',)


class Subscription(models.Model):
    """Модель подписки пользователя на курс."""
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE
    )

    # TODO

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
        ordering = ('-id',)

