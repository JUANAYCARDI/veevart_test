# veevart_test

Test 15 

Para correr este archivo se necesita una versiòn de python 3.12 o superior

Si el programa se ejecuta sin un archivo de texto de entrada se requeriran varios inputs por parte del usuario:
1. Ingresar la cantidad de filas que tendrà la sopa de letras
2. Ingresar linea a linea cada fila de la sopa de letras con las letras separadas por espacio y en mayùsculas
3. Ingresar la opcion 1 en caso de que se desee jugar, o la opcion 0 para que finalice el programa
4. Ingresar la cantidad de palabras que el usuario quiere buscar en la sopa de letras
5. Ingresar linea a linea cada palabra que se desea buscar, sin espacios y en letras mayùsculas

Despuès de ingresar estos inputs el programa se ejecuta y resuelve la sopa de letras palabra a palabra indicando si 
encuentra dicha palabra y su posiciòn, o por el contrario si no la encuentra.
La bùsqueda se realiza en sentido alfabètico español, izquierda a derecha, arriba a abajo y diagonal desde la parte superior
izquierda a la inferior derecha

Para mejor entendimiento de un input ejemplo para el programa, ver el archivo test15Input.txt de este repositorio

En caso de que se desee ejecutar el programa con un archivo de texto existente, use el siguiente comando en una terminal:

python3 Test15.py < nombredelarchivo.txt

-----------------------------------------------------------------------------------------------------------

Test 9 

Para correr este archivo se necesitan ùnicamente 3 inputs:

1. Lista de enteros separados por espacios que indican los pisos a los cuales el ascensor accederà
2. Entero que indica el piso inicial del ascensor
3. Diccionario, escrito linea a linea como parejas de enteros indicando llave y valor de cada piso y el piso al que se llamarà desde el mismo

Al ejecutar el archivo e ingresar estos inputs, el programa imprimirà una soluciòn òptima del recorrido del ascensor 
usando una estrategia voraz con el algoritmo de dijkstra.

Para mejor entendimiento de un input ejemplo para el programa, ver el archivo test9Input.txt de este repositorio

En caso de que se desee ejecutar el programa con un archivo de texto existente, use el siguiente comando en una terminal:

python3 Test9.py < nombredelarchivo.txt
