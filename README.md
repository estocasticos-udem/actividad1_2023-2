# Actividad 1 - Repaso de probabilidad

## Enunciado

De la siguiente lista de problemas, resuelva aquellos que le fueron asignados teniendo en cuenta los siguientes requisitos:
1. Desarrollar de manera teorica y **a mano** el problema asignado. Este desarrollo debe ser presentado mostrando el procedimiento de manera clara y ordenada. Una vez hecho esto, deberá tomar una foto del procedimiento realizado y convertirlo en un documento en formato pdf el cual debe ser agregado como evidencia.
2. Desarrollar el notebook de python asociado al problema de tal manera que se evidencie el procedimiento realizado en python.

En construcción...

## Problemas 

### Probabilidades

**Ejercicio 1 - VIH testing**: Las pruebas de inmunoensayo enzimático (EIA) se utilizan para detectar la presencia de anticuerpos contra el VIH, el virus que causa el SIDA, en muestras de sangre. Los anticuerpos indican la presencia del virus. La prueba es bastante precisa, pero no siempre es correcta. Estas son las probabilidades aproximadas de resultados positivos y negativos de EIA cuando la sangre analizada contiene y no contiene anticuerpos contra el VIH.

||Resultado positivo (+)|Resultado negativo (-)|
|---|---|---|
|Anticuertos presentes| 0.9985| 0.0015|
|Anticuerpos ausentes |0.006| 0.994|

Suponga que el 1% de una gran población porta anticuerpos del VIH en su sangre.

1. Determine cada uno de los eventos de manera clara.
2. Dibuje un diagrama de árbol para seleccionar una persona de esta población (**resultados**: anticuerpos presentes o ausentes) y para analizar su sangre (**resultados**: EIA positivo o negativo).
3. ¿Cuál es la probabilidad de que la prueba EIA sea positiva para una persona de esta poblacion elegida al azar? (**Rta**: 0.015925)
4. ¿Cuál es la probabilidad de que una persona tenga la anticuerpo dado que la prueba EIA es positiva? (**Rta**: 0.6270)

**Ejercicio 2 - Riesgos médicos**: Los riñones de Morris están fallando y está esperando un trasplante de riñón. Su médico le da esta información para pacientes en su condición: el 90% sobrevive al trasplante y el 10% muere. El trasplante tiene éxito en el 60% de los que sobreviven, y el otro 40% debe volver a la diálisis renal. Las proporciones que sobreviven cinco años son 70% para aquellos con un riñón nuevo y 50% para aquellos que regresan a la diálisis.
1. Determine cada uno de los eventos de manera clara.
2. Realizar el diagrama de arbol donde se represente este problema de manera clara.
3. Encuentre la probabilidad de que Morris viva por cinco años (**Rta**: 0.558).

**Ejercicio 3 - Intolerancia a la lactosa**: La intolerancia a la lactosa provoca dificultad para digerir los productos lácteos que contienen lactosa (azúcar de la leche). Es particularmente común entre las personas de ascendencia africana y asiática. En Estados Unidos (desconociendo otros grupos y personas que se consideran pertenecientes a más de una raza), el 82% de la población es blanca, el 14% es negra y el 4% es asiática. Además, el 15 % de los blancos, el 70 % de los negros y el 90 % de los asiáticos son intolerantes a la lactosa.
1. Identifique cada uno de los eventos asociados al problema.
2. Teniendo en cuenta los eventos encontrados en el numeral anterior, dibuje el diagrama de arbol del problema.
3. ¿Qué porcentaje de la población total es intolerante a la lactosa? (**Rta**: 0.257)
4. ¿Qué porcentaje de personas que son intolerantes a la lactosa son asiáticos? (**Rta**: 0.1401)

**Ejercicio 4 - Acertijo de probabilidad**: Supongamos (como es más o menos correcto) que cada niño que nace tiene la misma probabilidad de ser niño o niña y que los géneros de los niños sucesivos son independientes. Si **BG** significa que el niño mayor es un niño y el menor es una niña, entonces cada una de las combinaciones **BB**, **BG**, **GB** y **GG** tiene una probabilidad de 0.25. Marta y Maria tienen dos pequeños cada una.
1. Identifique los eventos necesarios y dibuje el diagrama de arbol asociado a este problema mostrando claramente las probabilidades asociadas.
3. Si usted conoce que al menos uno de los hijos de Marta es un niño. ¿Cual es la probabilidad condicional de que los dos sean niños? (**Rta**: 0.333)
4. Si usted sabe que el hijo mayor de Maria es niño. ¿Cual es la probabilidad condicional de que los dos sean niños?  (**Rta**: 0.5)

### Tablas de continencia

**Ejercicio 5**: Un artículo en la New England Journal of Medicine, informó sobre un estudio de fumadores en California y Hawái. En una parte del informe se indicaba el origen étnico autodeclarado y la cantidad de cigarrillos por día. De las personas que fumaban como máximo diez cigarrillos al día, había 9886 afroamericanos, 2745 nativos de Hawái, 12831 latinos, 8378 japoneses americanos y 7650 blancos. De las personas que fumaban entre 11 y 20 cigarrillos al día, había 6514 afroamericanos, 3062 nativos de Hawái, 4932 latinos, 10680 japoneses americanos y 9877 blancos. De las personas que fumaban entre 21 y 30 cigarrillos al día, había 1671 afroamericanos, 1419 nativos de Hawái, 1406 latinos, 4715 japoneses americanos y 6062 blancos. De las personas que fumaban al menos 31 cigarrillos al día, había 759 afroamericanos, 788 nativos de Hawái, 800 latinos, 2305 japoneses americanos y 3970 blancos.
1. Rellene la siguiente tabla con los datos previamente proporcionados:
   
   | Nivel de fumadores | Afroamericanos |Nativos de Hawái| Latinos |Japoneses |Blancos| TOTALES|
   |---|---|---|---|---|---|---|
   |1 - 10|||||||
   |11 - 20|||||||
   |21 - 30|||||||
   |31 ó mas|||||||
   |TOTALES|||||||

2. Suponiendo que se selecciona al azar una persona del estudio. Calcule la probabilidad de que la persona haya fumado de 11 a 20 cigarrillos al día. (**Rta**:  35065/100450)
3. Calcule la probabilidad de que la persona sea latina.
4. En palabras, explique qué significa elegir una persona del estudio que sea "japonés americano **Y** que fume de 21 a 30 cigarrillos al día". Además, encuentra la probabilidad (**Rta**:  4715/100450)
5. En palabras, explique qué significa elegir una persona del estudio que sea "japonesa-americana **O** que fume de 21 a 30 cigarrillos al día. Además, encuentra la probabilidad.
6. En palabras, explique qué significa elegir una persona del estudio que sea "japonesa-americana, dado que esa persona fuma de 21 a 30 cigarrillos al día. Además, encuentra la probabilidad. (**Rta**:  4715/15273),
7. Demostrar que el hábito de fumar/día y la etnia son eventos dependientes.

**Ejercicio 6**: Los siguientes son datos reales del condado de Santa Clara, CA. Hasta cierto momento, había un total de 3059 casos documentados de SIDA en el condado. Se agruparon en las siguientes categorías:

||Homosexual/bisexual| Consumidor de drogas por vía intravenosa|	Contacto heterosexual|Otros|Totales|
|---|---|---|---|---|---|
|Mujeres|0|	70|	136|	49|	|
|Hombres|	2146|	463|	60|	135||
|Totales||||||

Supongamos que se selecciona al azar una persona con SIDA en el condado de Santa Clara.
1. Calcule **P(la persona es mujer)**. (**Rta**: 255/3059).
2. Calcule **P(La persona tiene un factor de riesgo contacto heterosexual)**. (**Rta**: 196/3059).
3. Calcule **P(La persona es mujer O tiene un factor de riesgo de usuario de drogas intravenosas)**. (**Rta**: 718/3059).
4. Calcule **P(La persona es mujer Y tiene un factor de riesgo homosexual/bisexual)**. (**Rta**: 0).
5. Calcule **P(La persona es hombre Y tiene un factor de riesgo de consumidor de drogas por vía intravenosa)**. (**Rta**: 463/3059).
6. Calcule **P(La persona DADA es una mujer se contagió de la enfermedad por contacto heterosexual)**. (**Rta**: 136/196).

**Ejercicio 7**: En un año anterior, los pesos de los miembros de los **San Francisco 49ers** y los **Dallas Cowboys** se publicaron en el *The Mercury News de San José*. Los datos fácticos se recopilaron en la siguiente tabla.

|N.º de camisa|	≤ 210|	211–250|	251–290	|> 290|
|---|---|---|---|---|
|1–33|	21|	5|	0|	0|
|34–66|	6|	18|	7| 4|
|66–99|	6|	12|	22|	5|

Para lo siguiente, suponga que selecciona al azar un jugador de los 49ers o de los Cowboys.
1. Calcule la probabilidad de que el número de su camiseta sea del 1 al 33. (**Rta**: 26/106)
2. Calcule la probabilidad de que pese como máximo 210 libras. (**Rta**: 33/106)
3. Calcule la probabilidad de que el número de su camisa esté entre el 1 y el 33 **Y** que pese como máximo 210 libras. (**Rta**: 21/106)
4. Calcule la probabilidad de que el número de su camisa sea del 1 al 33 **O** que pese como máximo 210 libras. (**Rta**: 38/106)
5. Calcule la probabilidad de que el número de su camisa sea del 1 al 33, **DADO** que pesa como máximo 210 libras. (**Rta**: 21/33)

## Referencias 

* Jupyter Notebooks:
  * https://www.datacamp.com/tutorial/tutorial-jupyter-notebook
  * https://realpython.com/jupyter-notebook-introduction/
* Markdown:
  * https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet
  * https://www.markdownguide.org/
* Manejo de pandas:
  * https://github.com/ssanchezgoe/curso_deep_learning_economia/blob/main/NBs_Google_Colab/DL_S02_Pandas_Data_Wrangling.ipynb
  * https://github.com/ssanchezgoe/curso_deep_learning_economia/blob/main/NBs_Google_Colab/DL_S03_Tipos_de_Datos.ipynb
  * https://github.com/ssanchezgoe/eafit_isa/blob/main/Nb_Google_Colab/S03_Bases_Estadisticas.ipynb
  * https://github.com/ssanchezgoe/eafit_isa/blob/main/Nb_Google_Colab/S03_Bases_Estadisticas_Version_Clase.ipynb
