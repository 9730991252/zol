from channels.consumer import SyncConsumer, AsyncConsumer
from channels.exceptions import StopConsumer



class MySyncConsumer(SyncConsumer):
    def websocket_connect(self, event):
        print('websocket connected...', event)
        self.send({
            'type' : 'websocket.accept'
        })
    def websocket_receive(self, event):
        print('message Recived from Client..', event)

    def websocket_disconnect(self, event):
        print('websocket Disconnected...', event)