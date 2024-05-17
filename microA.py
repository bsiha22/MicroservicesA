import random
import string
import base64

def generate_password(specs):
    length, use_uppercase, use_lowercase, use_numbers, use_special = specs
    
    # Create separate pools for each type of character
    uppercase_chars = string.ascii_uppercase if use_uppercase else ''
    lowercase_chars = string.ascii_lowercase if use_lowercase else ''
    number_chars = string.digits if use_numbers else ''
    special_chars = string.punctuation if use_special else ''
    
    # Combine all pools
    char_pool = uppercase_chars + lowercase_chars + number_chars + special_chars
    
    if not char_pool:
        raise ValueError("At least one character type must be selected")
    
    # Start the password with at least one character from each required type
    password_chars = []
    if use_uppercase:
        password_chars.append(random.choice(uppercase_chars))
    if use_lowercase:
        password_chars.append(random.choice(lowercase_chars))
    if use_numbers:
        password_chars.append(random.choice(number_chars))
    if use_special:
        password_chars.append(random.choice(special_chars))
    
    # Fill the rest of the password length with random choices from the combined pool
    while len(password_chars) < length:
        password_chars.append(random.choice(char_pool))
    
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
    encode = password_encode(password)
    return encode



for i in range(1,6):
    passw = (10, True, True, True, True)
    passwords = gen_encode_pass(passw)
    print(f"Generated encoded password {i}: {passwords}")