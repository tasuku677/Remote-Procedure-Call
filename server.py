import socket
import os
import json
import struct
import server.functions as func

function_hash = {
    'floor': func.floor,
    'nroot': func.nroot,
    'validAnagram': func.validAnagram,
    'reverse': func.reverse,
    'sort': func.sort
}

server_address = './tmp/socket_file'
os.makedirs(os.path.dirname(server_address), exist_ok=True)
sock  = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

try:
    os.unlink(server_address)
except FileNotFoundError:
    pass

print('Starting up on {}'.format(server_address))

sock.bind(server_address)
sock.listen(10)
while True:
    connection, client_address = sock.accept()
    try: 
        print('Connection from', client_address)
        while True:
            data = connection.recv(1024)
            if data:
                data_str = data.decode('utf-8')
                print('Recieved' + data_str)
                data = json.loads(data_str)
                if func.check_params(data["method"], data["params_types"]):
                    response = {
                        "id": data["id"],
                        **function_hash[data["method"]](data["params"])
                    }
                else:
                    response = {
                        "id": data["id"],
                        "type": "error",
                        "value": "Invalid function"
                    }
                connection.sendall(json.dumps(response).encode('utf-8'))
            else:
                print('No data from', client_address)
                break
    except Exception as e:
        print(e)
    finally:
        connection.close()
        print('Connection closed\n')