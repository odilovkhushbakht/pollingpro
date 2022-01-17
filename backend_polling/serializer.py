from rest_framework import serializers
from .models import Polling, Question, Participant, UserCustom


class PollingSeria(serializers.ModelSerializer):
    class Meta:
        model = Polling
        fields = ('__all__')


class PollingUpdateSeria(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Polling
        # fields = ('id', 'name', 'finished_date', 'description', 'status')
        exclude = ['number', ]


class QuestionSeria(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('__all__')


class PollingRelationSeria(serializers.ModelSerializer):
    pol = QuestionSeria(many=True, read_only=True)

    class Meta:
        model = Polling
        fields = ('__all__')


# class QuestionSelectSeria(serializers.ModelSerializer):
#     class Meta:
#         model = Question
#         exclude = ['answer_text', ]


# class QuestionTextSeria(serializers.ModelSerializer):
#     class Meta:
#         model = Question
#         fields = (
#             'text', 'style', 'answer_multi_1', 'answer_multi_2', 'answer_multi_3', 'answer_multi_4', 'parent'
#         )
# exclude = ['answer_multi_1', 'answer_multi_2', 'answer_multi_3', 'answer_multi_4', 'answer_text']


class ParticipantSeria(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = ("__all__")


class UserCustomValidateSeria(serializers.ModelSerializer):
    class Meta:
        model = UserCustom
        fields = ("id",)


class UserCustomSeria(serializers.ModelSerializer):
    class Meta:
        model = UserCustom
        fields = ("__all__")


class UserCustomRelationSeria(serializers.ModelSerializer):
    # id = serializers.IntegerField()
    # username = serializers.CharField()
    answer = ParticipantSeria(many=True, read_only=True)

    # answer = serializers.SlugRelatedField(
    #     many=True,
    #     read_only=True,
    #     slug_field='text'
    # )

    class Meta:
        model = UserCustom
        fields = ['first_name', 'last_name', 'answer']
        # fields = ('__all__')
