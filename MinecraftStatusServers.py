import requests
import asyncio
from mcstatus import JavaServer

def info(serverip):
    try:
        URL = "https://api.mcstatus.io/v2/status/java/"
        respuesta = requests.get(URL + serverip)
        datos = respuesta.json()

        ip = datos["ip_address"]
        port = datos["port"]
        onlinepleyers = datos["players"] ["online"]
        maxcapacity = datos["players"] ["max"]
        version = datos["version"] ["name_clean"]

        jugadores = '\n'.join(f"{j['name_raw']} " for j in datos["players"]["list"])
        uids = '\n'.join(f"{j['uuid']}" for j in datos["players"]["list"])
        
        try:
            server = JavaServer.lookup(serverip)
            status = asyncio.run(server.async_status())
            ping = round(status.latency)
        except Exception as e:
            ping = f"Error al medir el ping: {e}"

        return(
            f"IP and Port: {ip}:{port}\n"
            f"Players Online {onlinepleyers} and maximum capacity players {maxcapacity}\n"
            f"Ping: {ping} ms\n"
            f"Server Version {version}\n"
            f"Players Online list name and uuid \n {jugadores}\n {uids}"
        )
    
    except Exception as e:
        return f"Error al obtener informacion: {e}"
