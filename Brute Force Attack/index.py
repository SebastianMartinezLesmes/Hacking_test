import itertools
import string
import time

# Contraseña que se intentará adivinar (puedes cambiarla)
PASSWORD_REAL = "jav"

# Conjunto completo de caracteres
caracteres = string.ascii_letters + string.digits + string.punctuation

def verificar(password_intento):
    """Simula la verificación de una contraseña"""
    return password_intento == PASSWORD_REAL

def ataque_fuerza_bruta(longitud_maxima=15):
    """Intenta adivinar la contraseña probando todas las combinaciones posibles"""
    intentos = 0
    inicio = time.perf_counter()

    for longitud in range(1, longitud_maxima + 1):
        for combinacion in itertools.product(caracteres, repeat=longitud):
            intento = ''.join(combinacion)
            intentos += 1

            # Mostrar intento actual en una sola línea
            print(f"\rIntentos: {intentos:,} | Probando: {intento}", end="")

            if verificar(intento):
                duracion = time.perf_counter() - inicio
                print(f"\n\n[✔] Contraseña encontrada: {intento}")
                print(f"[🔁] Intentos realizados: {intentos}")
                print(f"[⏱️] Tiempo total: {duracion:.2f} segundos")
                return intento

    duracion = time.perf_counter() - inicio
    print("\n\n[✘] Contraseña no encontrada.")
    print(f"[⏱️] Tiempo total: {duracion:.2f} segundos")
    return None

# Ejecutar el ataque
if __name__ == "__main__":
    print(f"[🎯] Iniciando ataque por fuerza bruta para encontrar: '{PASSWORD_REAL}'")
    ataque_fuerza_bruta()
