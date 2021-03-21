from django.urls import path
from . import views


urlpatterns = [
    path(
       "get_user_details/",
       views.GetUserDetailsView.as_view(),
       name="get_user_details_view"
    ),
    path(
        "get_questions",
        views.MultiChoiceQuestionsView.as_view(),
        name="get_questions"
    ),
    path(
        "user_answer",
        views.UserAnswerView.as_view(),
        name="user_answer"
    ),
]
