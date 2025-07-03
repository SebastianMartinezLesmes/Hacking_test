# 🧪 Proyectos

## ⏱️ Timing Attack (Ataque de temporización)

### 🧠 ¿Qué es?
Un **Timing Attack** es un tipo de **ataque de canal lateral** en el que el atacante mide el tiempo de respuesta de un sistema a diferentes entradas para deducir información confidencial, como contraseñas o claves criptográficas.

Por ejemplo, si una comparación de contraseñas se realiza carácter por carácter, y el sistema tarda ligeramente más cuando algunos caracteres son correctos, un atacante puede deducir la contraseña **letra por letra** simplemente midiendo el tiempo de respuesta.

---

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
## 🦾 Brute Force Attack (ataque de fuerza bruta)

### 🧠 ¿Qué es?
Un **Brute Force Attack** (o **ataque de fuerza bruta**) es una técnica en la que un atacante intenta adivinar una contraseña o clave probando **todas las combinaciones posibles** hasta encontrar la correcta.

Este tipo de ataque no depende de vulnerabilidades específicas, sino de la **debilidad de la contraseña** y la **fuerza bruta computacional**. Es un enfoque simple pero efectivo cuando las contraseñas son cortas o predecibles.

---

### 🧠 ¿Como funciona?
El atacante no tiene pistas reales sobre la contraseña o clave, así que:
- Empieza probando "a", "b", "c", ..., "aa", "ab", "ac", etc.
- Continúa hasta encontrar la combinación correcta que permite el acceso.
- Funciona con cualquier tipo de sistema donde haya una verificación de datos de acceso.

---

### ⚙️ Cómo ejecutar el sistema

1. Abre **dos ventanas de terminal (CMD, PowerShell o terminal Bash)** y se dirige a la carpeta 'Brute Force Attack'.
2. En la primera ventana, ejecuta:
    ```
    python index.py
    ```
