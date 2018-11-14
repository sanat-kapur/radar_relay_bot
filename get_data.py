import asyncio
import websockets
import json
import datetime

url = "wss://ws.radarrelay.com/v2"

sub_request_json = json.dumps({
	"type":'SUBSCRIBE',
	"topic":'BOOK',
	"market":'DAI-WETH'
	})

async def collect_data():
	async with websockets.connect(url) as websocket:
		await websocket.send(sub_request_json)
		while True:
			message = await websocket.recv()
			print(message)

def store_data(json_packet):
	with open(date)

asyncio.get_event_loop().run_until_complete(collect_data())
