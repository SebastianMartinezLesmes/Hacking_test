import hashlib
import time

# Hash objetivo (SHA-256 de "123456")
target_hash = "8d969eef6ecad3c29a3a629280e686cff8fabef6e6b3a5a8a1d4e3a7ecbd7aabe"

found = False
attempts = 0
start_time = time.time()

with open("passwords.txt", "r", encoding="utf-8") as file:
    for password in file:
        attempts += 1
        password = password.strip()
        hashed_pwd = hashlib.sha256(password.encode()).hexdigest()

        if hashed_pwd == target_hash:
            print(f"[✔] Contraseña encontrada: {password}")
            found = True
            break

end_time = time.time()
elapsed_time = end_time - start_time

if not found:
    print("[✘] Contraseña no encontrada en el diccionario.")

print(f"Intentos: {attempts}")
print(f"Tiempo transcurrido: {elapsed_time:.4f} segundos")
