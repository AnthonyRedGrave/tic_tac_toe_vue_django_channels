import channels
from channels.generic.websocket import AsyncWebsocketConsumer
import json


class TicTacToeConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.game_id = self.scope['url_route']['kwargs']['game_id']
        self.game_group_name = f'game_{self.game_id}'
        # print(dir(self.channel_layer))
        
        # print("connect")
        await self.channel_layer.group_add(
            self.game_group_name,
            self.channel_name
        )
        
        await self.accept()
        if len(self.channel_layer.groups[self.game_group_name]) == 2:
            print("можно отправлять")
            await self.channel_layer.group_send(
            self.game_group_name,
            {
                "type": "user2IsReady_send",
                "user2IsReady": True

            }
        )

    async def user2IsReady_send(self, event):
        user2IsReady = event['user2IsReady']
        await self.send(text_data=json.dumps({
            'user2IsReady_send': user2IsReady
        }))


    async def disconnect(self, code):
        print("disconnect")
        await self.channel_layer.group_discard(
            self.game_group_name,
            self.channel_name
        )