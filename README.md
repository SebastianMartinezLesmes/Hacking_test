# 🧪 Proyectos

## ⏱️ Timing Attack (Ataque de temporización)

### 🧠 ¿Qué es?
Un **Timing Attack** es un tipo de **ataque de canal lateral** en el que el atacante mide el tiempo de respuesta de un sistema a diferentes entradas para deducir información confidencial, como contraseñas o claves criptográficas.
Por ejemplo, si una comparación de contraseñas se realiza carácter por carácter, y el sistema tarda ligeramente más cuando algunos caracteres son correctos, un atacante puede deducir la contraseña **letra por letra** simplemente midiendo el tiempo de respuesta.

### ⚙️ Cómo ejecutar el sistema
#### 🔓 Para probar el servidor **vulnerable**:
1. Abre **dos ventanas de terminal (CMD, PowerShell o terminal Bash)** y se dirige a la carpeta 'Timing Attack'.
2. En la primera ventana, ejecuta:
    ```
    python vulnerable_server.py
    ```
3. En la segunda ventana, ejecuta:
    ```
    python attacker.py
    ```
#### 🔐 Para probar el servidor **seguro**:
1. Abre **dos ventanas de terminal (CMD, PowerShell o terminal Bash)** y se dirige a la carpeta 'Timing Attack'.
2. En la primera ventana, ejecuta:
    ```
    python secure_server.py.py
    ```
3. En la segunda ventana, ejecuta:
    ```
    python attacker.py
    ```

---

## 🦾 Brute Force Attack (ataque de fuerza bruta)

### 🧠 ¿Qué es?
Un **Brute Force Attack** (o **ataque de fuerza bruta**) es una técnica en la que un atacante intenta adivinar una contraseña o clave probando **todas las combinaciones posibles** hasta encontrar la correcta.
Este tipo de ataque no depende de vulnerabilidades específicas, sino de la **debilidad de la contraseña** y la **fuerza bruta computacional**. Es un enfoque simple pero efectivo cuando las contraseñas son cortas o predecibles.

### 🧠 ¿Como funciona?
El atacante no tiene pistas reales sobre la contraseña o clave, así que:
- Empieza probando "a", "b", "c", ..., "aa", "ab", "ac", etc.
- Continúa hasta encontrar la combinación correcta que permite el acceso.
- Funciona con cualquier tipo de sistema donde haya una verificación de datos de acceso.

### ⚙️ Cómo ejecutar el sistema
1. Abre **dos ventanas de terminal (CMD, PowerShell o terminal Bash)** y se dirige a la carpeta 'Brute Force Attack'.
2. En la primera ventana, ejecuta:
    ```
    python index.py
    ```
---

## 🧬 Hash Cracking (crackeo de hash)

### 🧠 ¿Qué es?
El **## 🧬 Hash Cracking** (o **crackeo de hash**)  es una técnica utilizada para descubrir contraseñas que han sido cifradas mediante funciones hash (como SHA-256). Los hashes son funciones unidireccionales: no se pueden revertir, pero sí se pueden comparar.

Este ataque consiste en generar hashes desde una lista de posibles contraseñas (diccionario) y compararlos con un hash objetivo hasta encontrar una coincidencia.

### 🧠 ¿Como funciona?
Esto es útil para mostrar cómo las contraseñas débiles pueden romperse incluso sin saber nada del sistema original.
- Se parte de un hash conocido (por ejemplo, almacenado en una base de datos).
- El atacante usa un diccionario con contraseñas comunes.
- Por cada entrada en el diccionario, genera su hash con la misma función (ej. SHA-256).
- Compara ese hash con el objetivo. Si coinciden, ha descubierto la contraseña original.

### ⚙️ Cómo ejecutar el sistema
1. Abre **dos ventanas de terminal (CMD, PowerShell o terminal Bash)** y se dirige a la carpeta 'Hash Cracking'.
2. En la ventana, ejecuta:
    ```
    python hash_cracker.py
    ```

---

## Keylogger Simulado (offline)

### 🧠 ¿Qué es?
Un **Keylogger** (**registrador de teclas**) es un programa que registra cada tecla que escribe el usuario. Puede ser utilizado maliciosamente para robar contraseñas, correos o datos personales, pero también se utiliza con fines educativos o de monitoreo autorizado.

Este proyecto muestra una simulación segura y offline de cómo funciona un keylogger básico en Python, sin capturar en segundo plano ni ejecutar nada malicioso.

### 🧠 ¿Como funciona?
- El usuario escribe algo en consola.
- El sistema guarda esa entrada en un archivo de texto con una marca de tiempo.
- De este modo, simula cómo un keylogger real puede almacenar entradas del usuario de forma silenciosa.

### ⚙️ Cómo ejecutar el sistema
1. Abre **dos ventanas de terminal (CMD, PowerShell o terminal Bash)** y se dirige a la carpeta 'Keylogger'.
2. En la ventana, ejecuta:
    ```
    python keylogger_simulado.py
    ```
