import socketio
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from .seriallizer import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from socketio import AsyncServer


sio = AsyncServer(async_mode='asgi')
@sio.on('message')
async def handle_message(sid, data):
    response = {'message': f'Received: {data}'}
    await sio.emit('response', response, room=sid)

class SocketView(APIView):
    async def get(self, request):
        sio_app = socketio.ASGIApp(sio)
        response = await sio_app.handle_request(request.environ)
        return Response(response)
    

class UserView(viewsets.ModelViewSet):

    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()





from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def fn_stream(request):
    print(request.POST)
    return Response({"message": "Hello, world!"})



import base64
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def camera_stream(request):
    if request.method == 'POST':
        image_data = request.POST.get('image_data')
        image_data = image_data.split(',')[1]
        image_data = base64.b64decode(image_data)
        # Process the image data as needed
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=405)


class StreamApiView(APIView):
    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        print(request.POST)

        return Response({"data recived"}, status=HTTP_200_OK)