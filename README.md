# BANK-OCR
**Daniel Cruz Arciniega**

## Cómo ejecutar el programa
Para ejecutar el programa se necesita tener python instalado, de preferencia la versión **3.12**, no se necesitan instalar librerías adicionales.

En la carpeta del proyecto ejecuta el comando `python main.py`. 

Los resultados se guardarán en outputs/output.txt.

Los archivos de entrada se encuentran dentro de la carpeta **inputs**. Si se quiere leer otro archivo cambiar la variable `input_file` dentro de **main.py**.

## Enfoque
Para este reto decidí tomar un enfoque de Programación Orientada a Objetos, creando la clase **BankOCR** dentro del archivo **bank_ocr**.
Lo hice de esta manera para poder guardar tanto el contenido de los inputs como los resultado con el objetivo de poder reutilizarlos a voluntad.

Hice un mapeo de los dígitos de los archivos de entrada con su número correspondiente, las llaves son strings de longitud 9, cada 3 caracteres representa una línea del archivo de texto
formando en total una celda de 3x3. 

Después de esto leí los archivos de entrada guardando los resultados en una matríz para luego convertir las celdas de 3x3 en strings y buscar su valor correspondiente en el mapeo, si no encuentra ninguno el valor va a ser **?**.

Por último se validan los números resultantes, en caso de contener **?** es **ILL**, si no contienen este caracter se introduce el número en la función `checksum` que valida que el número sea de longitud 9 y que el resultado de `(1*d1 + 2*d2 + 3*d3 + ... + 9*d9) mod 11` sea 0, si lo es el número es correcto **(OK)** y si no hay un error **(ERR)**.
