#!/bin/python3
import requests

def main():
	print("Validando si la IP pertenece a una botnet mediante INCIBE.")
	data = {}
	headers = {"X_INTECO_WS_Request_Source":"api"}
	get = requests.get("https://antibotnet.osi.es/api/wscheckip/es", data=data, headers=headers)
	print(get.json())
if __name__ == "__main__":
	main()
