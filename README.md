# 🧪 Proyectos

## ⏱️ Timing Attack (Ataque de temporización)

### 🧠 ¿Qué es?
Un **Timing Attack** es un tipo de **ataque de canal lateral** en el que el atacante mide el tiempo de respuesta de un sistema a diferentes entradas para deducir información confidencial, como contraseñas o claves criptográficas.

Por ejemplo, si una comparación de contraseñas se realiza carácter por carácter, y el sistema tarda ligeramente más cuando algunos caracteres son correctos, un atacante puede deducir la contraseña **letra por letra** simplemente midiendo el tiempo de respuesta.

---

### ⚙️ Cómo ejecutar el sistema

#### 🔓 Para probar el servidor **vulnerable**:
1. Abre **dos ventanas de terminal (CMD, PowerShell o terminal Bash)**.
2. En la primera ventana, ejecuta:
    ```
    python vulnerable_server.py
    ```
3. En la segunda ventana, ejecuta:
    ```
    python attacker.py
    ```
#### 🔐 Para probar el servidor **seguro**:
1. Abre **dos ventanas de terminal (CMD, PowerShell o terminal Bash)**.
2. En la primera ventana, ejecuta:
    ```
    python secure_server.py.py
    ```
3. En la segunda ventana, ejecuta:
    ```
    python attacker.py
    ```