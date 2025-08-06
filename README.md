# ch58-Number-Trivia
Este proyecto fue creado en Python con el objetivo de practicar el consumo de APIs públicas y la automatización de pruebas. Utiliza la API gratuita NumbersAPI para obtener datos curiosos en formato JSON sobre cualquier número ingresado por el usuario.

Consta de dos scripts principales:

Uno que permite al usuario ingresar cualquier número para consultar un dato curioso.

Otro que consulta directamente el número 42, usado comúnmente en ejemplos de programación.

Además, se incluirá un archivo de pruebas (test.py) para verificar el correcto funcionamiento de las funciones mediante el uso de la librería pytest.

El proyecto fue desarrollado como parte de una práctica formativa en el área de desarrollo backend, enfocándose en la interacción con APIs, manejo de respuestas JSON y buenas prácticas de pruebas unitarias.

## 📁 Archivos incluidos

- `trivia_fetch.py`: El usuario ingresa un número, el programa consulta la API y devuelve una respuesta JSON con información interesante.
- `consulta_fija_42.py`: Script que consulta directamente el número 42 en la API y muestra detalles específicos del resultado.
- `test.py`: (Próximamente) Archivo de pruebas automatizadas que verificará el correcto funcionamiento de las funciones de los scripts principales usando `pytest`.

---

## ⚙️ Requisitos

- Python 3.7 o superior
- Librería `requests`

Para instalar la librería necesaria:

```bash
pip install requests

🌐 API utilizada
NumbersAPI: Provee datos curiosos en múltiples formatos (texto plano, JSON) sobre números.

📄 Licencia
Este proyecto se distribuye bajo la licencia MIT.

✨ Autoría
Proyecto desarrollado como parte de una práctica de programación en Python para aprender sobre APIs y automatización de pruebas.
