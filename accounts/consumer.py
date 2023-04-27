import asyncio
from channels.generic.websocket import AsyncWebsocketConsumer

class CameraStreamConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        # Process the camera stream data received from the Electron app
        # You can access the image data in `text_data` variable
        # Example: image_data = text_data

        # Send a response back to the client (Electron app)
        await self.send(text_data='{"status": "success"}')