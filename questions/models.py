from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from .random_id import random_id


class UserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, full_name, password=None, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(email),
            full_name=full_name,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, full_name, password=None, **extra_fields):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email=self.normalize_email(email),
            full_name=full_name,
            password=password
        )
        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "User"
    username = None
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=50)
    investor = models.BooleanField(
        default=False, blank=True
    )
    account_linked = models.BooleanField(default=False)
    date_joined = models.DateTimeField(
        verbose_name='date joined', auto_now_add=True
    )
    last_login = models.DateTimeField(
        verbose_name='last login', auto_now=True
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    # This overwrites django's default user model's username to a
    # username of choice
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["full_name"]

    def __str__(self):
        return self.full_name

    def has_perm(self, perm, obj=None):
        """ Does the user have specific perimission?"""
        return self.is_admin

    def has_module_perms(self, app_label):
        """
        Does the user have specific permission to view the app'app_label'?
        """
        return True


class MultiChoiceUser(models.Model):
    class Meta:
        verbose_name = "Multi Choice User"
        verbose_name_plural = "Multi choice User"

    first_name = models.CharField(max_length=100)
    uuid = models.CharField(
        max_length=150,
        default=random_id,
        blank=True,
        null=True
    )
    last_name = models.CharField(max_length=100)
    occupation = models.CharField(max_length=150)
    highest_education = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=12)
    address = models.CharField(max_length=150)
    postal_code = models.CharField(max_length=10)
    marital_status = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.uuid}"


class MultiChoiceQuestions(models.Model):
    class Meta:
        verbose_name = "Multi Choice Questions"
        verbose_name_plural = "Multi Choice Questions"

    question = models.TextField()


class MultiChoiceAnswer(models.Model):
    class Meta:
        verbose_name = "Multi Choice Answer"
        verbose_name_plural = "Multi Choice Answer"

    answers = models.TextField()
    score = models.IntegerField(default=0, blank=True)
    user = models.OneToOneField(
        to=MultiChoiceUser,
        null=True,
        on_delete=models.SET_NULL
    )
