from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from .models import aeye_train_models
from .serializers import aeye_train_serializers
from .forms import aeye_image_form
from colorama import Fore, Back, Style
from datetime import datetime
import requests
import os

def print_log(status, whoami, mw, message) :
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")

    if status == "active" :
        print("\n-----------------------------------------\n"   + 
              current_time + " " + whoami + Fore.BLUE + "[ " + mw + " ]\n" +  Fore.RESET +
              Fore.GREEN + "[AI NetOper - active] " + Fore.RESET + "message: [ " + Fore.GREEN + message +" ]" + Fore.RESET +
              "\n-----------------------------------------")
    elif status == "error" :
        print("\n-----------------------------------------\n"   + 
              current_time + " " + whoami + Fore.BLUE + "[ " + mw + " ]\n" +  Fore.RESET +
              Fore.RED + "[AI NetOper - error] " + Fore.RESET + "message: [ " + Fore.RED + message +" ]" + Fore.RESET +
              "\n-----------------------------------------")

i_am_mw_test = 'MW - Test'

url = 'http://127.0.0.1:2000/api/ai-toolkit/'
class aeye_test_Viewswets(viewsets.ModelViewSet):
    queryset=aeye_train_models.objects.all().order_by('id')
    serializer_class=aeye_train_serializers

    def create(self, request) :
        serializer = aeye_train_serializers(data = request.data)

        if serializer.is_valid() :
            whoami    = serializer.validated_data.get('whoami')
            message   = serializer.validated_data.get('message')
            print_log('active', whoami, i_am_mw_test, "Succeed to Received Data : {}".format(message))

            response = aeye_ai_test_request()

            if response.status_code==200:
                return response
            else:
                return response
        else:
            print_log('error', 'MW - Test', i_am_mw_test, "Failed to Received Data : {}".format(request.data))

            message = "Client Sent Invalid Data"
            data = aeye_create_json_data(message)
            return Response(data, status=status.HTTP_400_BAD_REQUEST)



def aeye_ai_test_request():
    whoami = 'AEYE NetOper MW Inference'
    data = {
        'whoami' : 'AEYE NetOper MW Test',
        'operation' : 'Test',
        'message' : 'Request AI Test',
    }

    print_log('active', whoami, i_am_mw_test, "Send Data to : {}".format(url))
    response = requests.post(url, data=data)

    if response.status_code==200:
        response_data = response.json()
        print_log('active', whoami, i_am_mw_test, "Received Data from the Server : {}".format(response_data))
        
        whoami  = response_data.get('whoami')
        message = response_data.get('message')
            
        print_log('active', whoami, i_am_mw_test, "Succedd to Receive Data : {}".format(message) )
        data = aeye_create_json_data(message)

        return  Response(data, status=status.HTTP_200_OK)
    else:
        print_log('error', whoami, i_am_mw_test, "Failed to Receive Data : {}".format(message) )

        message = "Failed to Get Response For the Server"
        data = aeye_create_json_data(message)
        return Response(data, status=status.HTTP_400_BAD_REQUEST)


def aeye_get_data_from_response(reponse):
    response_data = reponse.json()
    whoami = response_data.get('whoami', '')
    message = response_data.get('message', '')

    if whoami:
        if message:
            return whoami, message
        else:
            print_log('error', 'AEYE NetOper MW Test', i_am_mw_test, "Failed to Receive message from the server : {}"
                                                                                            .format(message))
            return 400
    else:
        print_log('error', 'AEYE NetOper MW Test', i_am_mw_test, "Failed to Receive whoami from the server : {}"
                                                                                            .format(whoami))
        return 400
    
def aeye_create_json_data(message):
    data = {
        'whoami' : "AEYE NetOper MW Test",
        'message' : message
    }

    return data