from django.http import HttpResponseRedirect
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from backend_polling.models import Polling, UserCustom
from backend_polling.serializer import PollingSeria, PollingRelationSeria, UserCustomRelationSeria
from service.custom import SmallResultsSetPagination
from service.participant import save_result, order, check_user, create_user


class PollingView(ListAPIView):
    queryset = Polling.objects.filter(status=True)
    serializer_class = PollingSeria


class GetPollingView(ListAPIView):
    queryset = Polling.objects.filter(status=True).order_by('id')
    pagination_class = SmallResultsSetPagination
    serializer_class = PollingRelationSeria

    def get(self, request, *args, **kwargs):
        if check_user(request=request):
            return super().get(request, *args, **kwargs)
        return Response(status=403, data={"message": "вы не зарегистрированы"})


@api_view(['POST'])
def save_result_view(request):
    status = save_result(request=request)
    return Response(status=status)


@api_view(['GET'])
def order_view(request):
    data = order(request=request)
    return Response(data=data)


class OrderView(ListAPIView):
    queryset = UserCustom.objects.all().order_by('id')
    serializer_class = UserCustomRelationSeria

    def get_queryset(self):
        return super().get_queryset()

    def get(self, request, *args, **kwargs):
        if check_user(request=request):
            self.queryset = UserCustom.objects.filter(id=request.headers.get("user-id")).order_by('id')
            return super().get(request, *args, **kwargs)
        return Response(status=403, data={"message": "вы не зарегистрированы"})


@api_view(['POST'])
def registration_view(request):
    id = create_user(request=request)
    return Response(data={"id": id})
