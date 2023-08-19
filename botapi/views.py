from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import QuestionSerializer
from .models import ListofQuestions
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .aimodel import chatbot




def sendresponce(request):
    if request.method == "POST":
        question=request.POST.get('question')
        print()
    return render(request,'front.html')

@api_view(['GET'])
def testapi(request):
    question=ListofQuestions.objects.all()
    serial=QuestionSerializer(question,many=True)
    return Response(serial.data)


@csrf_exempt
@api_view(['POST'])
def testapipost(request):
    ans=chatbot.get_response(request.data["question"])
    serial=QuestionSerializer(data=request.data)
    if serial.is_valid():
        serial.save(ans=ans)
        
        
    return Response(serial.data)