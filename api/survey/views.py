from django.shortcuts import render
from rest_framework.views import APIView
from .models import Question, Answer, AnsweredQuestion
from .serializers import QuestionSerializer, AnswerSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q

class QuestionView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = self.request.user

        try:
            current_ques = self.request.data['current_ques']
            answer = self.request.data['answer']
        except:
            question = Question.objects.all().first()
            serialized = QuestionSerializer(question)
            return Response(serialized.data, status=status.HTTP_200_OK)

        user = self.request.user
        current_ques = Question.objects.get(id=current_ques)
        answer = Answer.objects.get(question=current_ques, id=answer)
        AnsweredQuestion.objects.create(question=current_ques, user=user)
        user.score = user.score + answer.score
        print(user.score)
        user.save()

        answered_questions = AnsweredQuestion.objects.filter(user=user)
        a = [a.question.id for a in answered_questions]
        print(a)

        if current_ques.next_question:
            question = Question.objects.filter(prev_ques = current_ques)    
        else:
            question = Question.objects.filter(lower__lte = user.score, upper__gte = user.score).exclude(id__in = a).first()
            print(question)


        if not question:
            user.has_completed = True
            user.score = 15
            AnsweredQuestion.objects.filter(user=user).delete()
            user.save()
            if user.score < 12.5:
                final = 'Low Risk'
            elif user.score >12.5 and user.score < 17.5:
                final = 'Moderate Risk'
            else:
                final = 'High Risk'
            return Response({'final': final}, status=status.HTTP_200_OK)

        serialized = QuestionSerializer(question)
        return Response(serialized.data, status=status.HTTP_200_OK)