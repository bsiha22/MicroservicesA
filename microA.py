import random
import string
import zmq
import base64

def generate_password(specs):
    length, uppercase, lowercase, numbers, special = specs
    
    # Create separate pools for each type of character
    uppercase_chars = string.ascii_uppercase if uppercase else ''
    lowercase_chars = string.ascii_lowercase if lowercase else ''
    number_chars = string.digits if numbers else ''
    special_chars = string.punctuation if special else ''
    
    # Combine all pools
    char_pool = uppercase_chars + lowercase_chars + number_chars + special_chars
    
    totalchar = uppercase + lowercase + numbers + special
    if totalchar > length:
        raise ValueError("The sum of specified characters is more than the requested length.")
    
    # Start the password with at least one character from each required type
    password_chars = []
    password_chars.extend(random.choices(uppercase_chars, k=uppercase))
    password_chars.extend(random.choices(lowercase_chars, k=lowercase))
    password_chars.extend(random.choices(number_chars, k=numbers))
    password_chars.extend(random.choices(special_chars, k=special))
    
    # Fill the rest of the password length with random choices from the combined pool
    if (length - totalchar) > 0:
        password_chars.extend(random.choices(char_pool, k=(length - totalchar)))
    
    # Shuffle the resulting list to ensure random distribution
    random.shuffle(password_chars)
    
    # Join the list into a single string
    password = ''.join(password_chars)
    
    return password

# Example usage
def password_encode(passwd):
    byte = passwd.encode('utf-8')
    b64bytes = base64.b64encode(byte)
    b64pass = b64bytes.decode('utf-8')
    return b64pass

def gen_encode_pass(param):
    password = generate_password(param)
    print(f"Preencoded password: {password}")
    encode = password_encode(password)
    print(f"Sending encoded password: {encode}")
    return encode

def rec_message():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")

    while True:

        message = socket.recv_json()

        try:
            params = (
                message['length'],
                message['uppercase'],
                message['lowercase'],
                message['numbers'],
                message['special']
            )
            encoded = gen_encode_pass(params)
            response = {'status': 'success', 'password': encoded}
        except Exception as ex:
            response = {'status': 'error', 'message': str(ex)}

        socket.send_json(response)

if __name__ == "__main__":
    rec_message()
