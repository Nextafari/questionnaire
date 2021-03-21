from django.contrib import admin
from .models import (
    MultiChoiceQuestions, MultiChoiceUser, User,
    MultiChoiceAnswer
)


class UserDb(admin.ModelAdmin):
    list_display = [
        "email", "full_name", "is_admin", "is_active",
        "is_staff", "is_superuser"
    ]


admin.site.register(User, UserDb)


class MultiChoiceUserDB(admin.ModelAdmin):
    list_display = [
        "first_name", "last_name", "occupation", "highest_education",
        "phone_number", "address", "postal_code", "marital_status"
    ]


admin.site.register(MultiChoiceUser, MultiChoiceUserDB)


class MultiChoiceQuestionsDB(admin.ModelAdmin):
    list_display = [
        "question"
    ]


admin.site.register(MultiChoiceQuestions, MultiChoiceQuestionsDB)


class MultiChoiceAnswerDB(admin.ModelAdmin):
    list_display = [
        "answers"
    ]


admin.site.register(MultiChoiceAnswer, MultiChoiceAnswerDB)
