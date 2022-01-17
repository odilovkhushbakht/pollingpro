from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from backend_polling.models import Polling, Question
from backend_polling.serializer import PollingSeria, PollingUpdateSeria, QuestionSeria
from service.actions import create, update, delete, create_question, update_question


class PollingView(ListAPIView):
    queryset = Polling.objects.all()
    serializer_class = PollingSeria


@api_view(['POST'])
def create_polling_view(request):
    status = create(Polling, PollingSeria, request=request)
    return Response(status=status)


@api_view(['POST'])
def update_polling_view(request):
    status = update(Polling, PollingUpdateSeria, request=request)
    return Response(status=status)


@api_view(['DElETE'])
def delete_polling_view(request):
    status = delete(Polling, request=request)
    return Response(status=status)


# Questions section

class QuestionView(ListAPIView):
    queryset = Question.objects.select_related().all()
    serializer_class = QuestionSeria


@api_view(['POST'])
def create_question_view(request):
    status = create_question(Question, request=request)
    return Response(status=status)


@api_view(['POST'])
def update_question_view(request):
    status = update_question(Question, request=request)
    return Response(status=status)


@api_view(['DElETE'])
def delete_question_view(request):
    status = delete(Question, request=request)
    return Response(status=status)
