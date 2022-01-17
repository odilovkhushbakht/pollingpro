from django.urls import path

from backend_polling.views import PollingView, GetPollingView, order_view, save_result_view, registration_view, \
    OrderView

urlpatterns = [
    path('', PollingView.as_view()),
    path('polling/', GetPollingView.as_view()),
    path('order/', OrderView.as_view()),
    path('save-result/', save_result_view),
    path('regis/', registration_view),
    # path('delete/', delete_view),
]
