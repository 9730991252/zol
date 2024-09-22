from channels.consumer import SyncConsumer, AsyncConsumer
from channels.exceptions import StopConsumer
from asgiref.sync import AsyncToSync, async_to_sync


class MySyncConsumer(SyncConsumer):
    def websocket_connect(self, event):
        print('websocket connected...', event)
        print("channel layer...", self.channel_layer)

        async_to_sync(self.channel_layer.group_add)(
            'programmers', 
            self.channel_name
            )
        self.send({
            'type' : 'websocket.accept'
        })

    def websocket_receive(self, event):
        print('message Recived from Client..', event)
        async_to_sync(self.channel_layer.group_send)(
            'programmers', 
            {
                'type': 'chat.message',
                'message' :event['text']
            })
        
    def chat_message(self, event):
        print('Event...', event)
        print('Actual Data...', event['message'])
        self.send({
            'type' : 'websocket.send',
            'text' : event['message']
        })

    def websocket_disconnect(self, event):
        print('websocket Disconnected...', event)
        async_to_sync(self.channel_layer.group_discard)(
            'programmers',
            self.channel_name
            )
        raise StopConsumer()