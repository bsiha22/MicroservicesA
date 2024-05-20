import zmq

def req_password(length, uppercase, lowercase, numbers, special):

    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")

    req_message = {
        'length': length,
        'uppercase': uppercase,
        'lowercase': lowercase,
        'numbers': numbers,
        'special': special
    }

    socket.send_json(req_message)

    response = socket.recv_json()

    if response['status'] == 'success':
        return response['password']
    else:
        raise Exception(f'Error generating a password: {response['message']}')
    
if __name__ == '__main__':
    try:
        password = req_password(12, 2, 4, 3, 3)
        print(f'Received base64 Encoded Password: {password}')
    except Exception as ex:
        print(ex)