import numpy as np

def encrypt_message(message, key_matrix):
    message_vector = np.array([ord(char) for char in message])
    eigenvalues, eigenvectors = np.linalg.eig(key_matrix)
    diagonalized_key_matrix = np.dot(np.dot(eigenvectors, np.diag(eigenvalues)), np.linalg.inv(eigenvectors))
    encrypted_vector = np.dot(diagonalized_key_matrix, message_vector)
    return encrypted_vector


def decrypt_message_(encrypted_vector, key_matrix):
    eigenvalues, eigenvectors = np.linalg.eig(key_matrix)
    diagonalized_key_matrix = np.dot(np.dot(eigenvectors, np.diag(eigenvalues)), np.linalg.inv(eigenvectors))
    decrypted_vector = np.dot(np.linalg.inv(diagonalized_key_matrix), encrypted_vector)
    return decrypted_vector




message = "Hello, world!"
key_matrix = np.random.randint(0, 256, (len(message), len(message)))

encrypted = encrypt_message(message, key_matrix)
print("Encrypted message:", encrypted)

decrypted = decrypt_message_(encrypted, key_matrix)
print("Decrypted message:", decrypted)

decrypted_message = ''.join(chr(int(round(num.real))) for num in decrypted)
print("Decrypted message:", decrypted_message)