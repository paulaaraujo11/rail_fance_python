def encrypt_rail_fence(message, rails):
    fence = [[] for _ in range(rails)]
    rail = 0
    direction = 1
    
    for char in message:
        fence[rail].append(char)
        
        if rail == 0:
            direction = 1
        elif rail == rails - 1:
            direction = -1
        
        rail += direction
    
    encrypted_message = ''.join([''.join(rail) for rail in fence])
    return encrypted_message


def decrypt_rail_fence(ciphertext, rails):
    fence = [[] for _ in range(rails)]
    rail = 0
    direction = 1
    
    for char in ciphertext:
        fence[rail].append(None)
        
        if rail == 0:
            direction = 1
        elif rail == rails - 1:
            direction = -1
        
        rail += direction
    
    index = 0
    for rail in fence:
        for i in range(len(rail)):
            rail[i] = ciphertext[index]
            index += 1
    
    rail = 0
    direction = 1
    plaintext = ''
    
    for _ in range(len(ciphertext)):
        plaintext += fence[rail].pop(0)
        
        if rail == 0:
            direction = 1
        elif rail == rails - 1:
            direction = -1
        
        rail += direction
    
    return plaintext


message = "HELLO WORLD"
rails = 3

encrypted_message = encrypt_rail_fence(message, rails)
print("Encrypted message:", encrypted_message)

decrypted_message = decrypt_rail_fence(encrypted_message, rails)
print("Decrypted message:", decrypted_message)
