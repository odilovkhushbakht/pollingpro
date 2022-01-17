from django.urls import path

from admin_polling.views import (
    PollingView, create_polling_view, update_polling_view, delete_polling_view,
    QuestionView, create_question_view, update_question_view, delete_question_view
)

urlpatterns = [
    path('', PollingView.as_view()),
    # path('polling/', PollingView.as_view()),
    path('polling-post/', create_polling_view),
    path('polling-update/', update_polling_view),
    path('polling-delete/', delete_polling_view),

    path('question/', QuestionView.as_view()),
    path('question-post/', create_question_view),
    path('question-update/', update_question_view),
    path('question-delete/', delete_question_view),
]
