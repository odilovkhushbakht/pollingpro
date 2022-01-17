from enum import Enum

# from backend_polling.models import Polling
from backend_polling.serializer import QuestionSeria


def create(modelObj, modelSeria, request):
    serializer = modelSeria(data=request.data)
    status = 400
    # message = 'error'
    if serializer.is_valid():
        modelObj(
            name=serializer.validated_data.get("name"),
            start_date=serializer.validated_data.get("start_date"),
            finished_date=serializer.validated_data.get("finished_date"),
            number=serializer.validated_data.get("number"),
            description=serializer.validated_data.get("description"),
            status=serializer.validated_data.get("status")
        ).save()
        status = 201
        # message = 'success'
    return status


def update(modelObj, modelSeria, request):
    serializer = modelSeria(data=request.data, partial=True)
    status = 202
    if serializer.is_valid():
        res = modelObj.objects.filter(
            id=request.data.get("id")).update(
            name=serializer.validated_data.get("name"),
            finished_date=serializer.validated_data.get("finished_date"),
            description=serializer.validated_data.get("description"),
            status=serializer.validated_data.get("status")
        )
        if not res:
            status = 400
    return status


class Style(Enum):
    ANSWER_TEXT = 1
    ANSWER_SELECT_ONE = 2
    ANSWER_MULTISELECT = 3


# def get_serializer(request):
#     style = request.data.get('style', None)
#     if style == Style.ANSWER_SELECT_ONE.value or style == Style.ANSWER_MULTISELECT.value:
#         return QuestionSelectSeria(data=request.data)
#     if style == Style.ANSWER_TEXT.value:
#         return QuestionTextSeria(data=request.data)
#     return None


def create_question(modelObj, request):
    status = 400
    # serializer = get_serializer(request=request)
    serializer = QuestionSeria(data=request.data)
    # message = 'error'
    if serializer and serializer.is_valid():
        if request.data.get('style', None) == Style.ANSWER_TEXT.value:
            modelObj(
                text=serializer.validated_data.get("text"),
                style=serializer.validated_data.get("style"),
                # parent=Polling.objects.get(id=serializer.validated_data.get("parent"))
                parent=serializer.validated_data.get("parent")
            ).save()
        else:
            modelObj(
                text=serializer.validated_data.get("text"),
                style=serializer.validated_data.get("style"),
                answer_multi_1=serializer.validated_data.get("answer_multi_1"),
                answer_multi_2=serializer.validated_data.get("answer_multi_2"),
                answer_multi_3=serializer.validated_data.get("answer_multi_3"),
                answer_multi_4=serializer.validated_data.get("answer_multi_4"),
                # parent=Polling.objects.get(id=serializer.validated_data.get("parent"))
                parent=serializer.validated_data.get("parent")
            ).save()
        status = 201
        # message = 'success'
    return status


def update_question(modelObj, request):
    status = 400
    # serializer = get_serializer(request=request)
    serializer = QuestionSeria(data=request.data)
    if serializer and serializer.is_valid():
        id = request.data.get("id")
        if request.data.get('style', None) == Style.ANSWER_TEXT.value:
            modelObj.objects.filter(id=id).update(
                text=serializer.validated_data.get("text"),
                style=serializer.validated_data.get("style"),
                answer_multi_1="",
                answer_multi_2="",
                answer_multi_3="",
                answer_multi_4="",
                parent=serializer.validated_data.get("parent", None)
            )
        else:
            modelObj.objects.filter(id=id).update(
                text=serializer.validated_data.get("text"),
                style=serializer.validated_data.get("style"),
                answer_multi_1=serializer.validated_data.get("answer_multi_1"),
                answer_multi_2=serializer.validated_data.get("answer_multi_2"),
                answer_multi_3=serializer.validated_data.get("answer_multi_3"),
                answer_multi_4=serializer.validated_data.get("answer_multi_4"),
                # parent=Polling.objects.get(id=serializer.validated_data.get("parent", None))
                parent=serializer.validated_data.get("parent", None)
            )
        status = 202
    return status


def delete(modelObj, request):
    status = 200
    # message = 'success'
    try:
        res = modelObj.objects.get(pk=request.data.get('id', None))
        res.delete()
    except modelObj.DoesNotExist:
        status = 400
        # message = 'not exist'
    return status
