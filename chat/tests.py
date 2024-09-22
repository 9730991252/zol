from django.test import TestCase
from channels.generic.websocket import WebsocketConsumer
import json
from asgiref.sync import async_to_sync


# Create your tests here.




class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_code']
        self.group_name = f'room_{self.room_name}'
        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name
        )

        self.accept()

        #async_to_sync(self.channel_layer.group_send)(
        #    f'room_{self.room_name}', {
        #        'value' : json.dumps({'status' : 'online'})
        #    }
        #)

        data = {'type': 'connected'}

        self.send(text_data = json.dumps({
            'payloade' : 'connected'
        }))

    def receive(self, text_data):
        data = json.loads(text_data)

        payload = {'message' : data.get('message') , 'sender' : data.get('sender')}

        async_to_sync(self.channel_layer.group_send)(
            f'room_{self.room_name}', {
                'type' : 'send_message',
                'value' : json.dumps(payload)
            }
        )


    def disconnect(self , close_code):
        pass

    def send_message(self, text_data):
        data = json.loads(text_data.get('value'))

        self.send(text_data = json.dumps({
            'payload' : data
        }))