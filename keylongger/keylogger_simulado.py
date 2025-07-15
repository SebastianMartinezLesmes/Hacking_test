import datetime

print("Simulación de keylogger (offline). Escribe algo y presiona Enter para finalizar.\n")
entrada = input("Entrada del usuario: ")

# Guardamos las teclas registradas en un archivo
with open("registro_teclas.txt", "a", encoding="utf-8") as f:
    f.write(f"[{datetime.datetime.now()}] {entrada}\n")

print("Teclas registradas en 'registro_teclas.txt'.")
