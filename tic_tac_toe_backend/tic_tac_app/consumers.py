from channels.generic.websocket import AsyncWebsocketConsumer
import json

class TicTacToeConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.game_id = self.scope['url_route']['kwargs']['game_id']
        self.game_group_name = f'game_{self.game_id}'
        print("connect")
        await self.channel_layer.group_add(
            self.game_group_name,
            self.channel_name
        )

    async def disconnect(self, code):
        print("disconnect")
        await self.channel_layer.group_discard(
            self.game_group_name,
            self.channel_name
        )