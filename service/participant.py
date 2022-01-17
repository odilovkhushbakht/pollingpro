from django.contrib.auth.models import User

from backend_polling.models import Participant, UserCustom
from backend_polling.serializer import UserCustomSeria, ParticipantSeria, UserCustomRelationSeria, \
    UserCustomValidateSeria


def check_user(request):
    user_id = request.headers.get("user-id")
    user_seria = UserCustomValidateSeria(data={'id': user_id})
    if user_seria.is_valid():
        return UserCustom.objects.filter(id=user_id).exists()
    return False


def save_result(request):
    status = 400
    serializer = ParticipantSeria(data=request.data)
    if serializer.is_valid() and check_user(request=request):
        Participant(
            user_data=UserCustom.objects.get(id=request.headers.get("user-id")),
            polling=serializer.validated_data.get("polling"),
            text=serializer.validated_data.get("text"),
            answer_multi_1=serializer.validated_data.get("answer_multi_1"),
            answer_multi_2=serializer.validated_data.get("answer_multi_2"),
            answer_multi_3=serializer.validated_data.get("answer_multi_3"),
            answer_multi_4=serializer.validated_data.get("answer_multi_4"),
            answer_text=serializer.validated_data.get("answer_text"),
            date=serializer.validated_data.get("date")
        ).save()
        status = 200
    return status


def order(request):
    res = {}
    if check_user(request=request):
        user = UserCustom.objects.filter(id=request.headers.get("user-id")).values()
        # print(user[0])
        serializer = UserCustomRelationSeria(data=user[0])
        if serializer.is_valid():
            res = serializer.data
            print(serializer.data)
            print(serializer.validated_data)
    return res


def create_user(request):
    id = 0
    serializer = UserCustomSeria(data=request.data)
    if serializer.is_valid():
        user = UserCustom(
            first_name=serializer.validated_data.get('first_name', "anonim"),
            last_name=serializer.validated_data.get('last_name', "anonim")
        )
        user.save()
        id = user.id
    return id
