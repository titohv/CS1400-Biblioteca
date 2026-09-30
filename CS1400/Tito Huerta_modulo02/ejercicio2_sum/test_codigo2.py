# #!/usr/bin/env python3 (para Linux/Mac) - python (para Windows)

import subprocess
import sys

def test_sum():
    """
    Evalúa si codigo2.py solicita dos números (3 y 8) y produce la suma 11.
    """
    # Selecciona el comando de Python adecuado según la plataforma
    python_cmd = 'python3' if sys.platform != 'win32' else 'python'

    process = subprocess.Popen(
        [python_cmd, '-u', 'codigo2.py'],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    
    # Simula la entrada del usuario presionado Enter ('3\n8\n')
    output, error = process.communicate(input='3\n8\n')

    # Une las salidas de texto por si los prompts de input van por stderr
    combined_output = (output + error).strip()

    # Aserción de la prueba
    assert "La suma de 3 y 8 es: 11" in combined_output, (
        f"❌ Esperado 'La suma de 3 y 8 es: 11', pero se recibió:\n[{combined_output}]"
    )

test_sum()
print("✅ Prueba pasada con éxito para la suma de dos números.")