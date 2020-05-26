# Zorro y Conejos (Fox and rabbits)

Juego de simulación de GA en Pygame, inspirado por el juego realizado para
Unity por:

## Agentes

Existen dos tipos de agentes:
- **Zorro** Es el depredador del juego, se alimenta del otro agente para saciar
    su hambre y necesita beber agua y descansar.
- **Conejo** Es el agente principal del juego, debe comer, tomar agua y
    descansar a fin de considerarse como exitoso.

## Mapa

El mapa es generado utilizando un algoritmo similar al Perlin Noise, denominado
OpenSimplex.
Basado en el valor de entropia suministrado al programa se crearán varias capas
de visualización

### Terrenos

Existen dos tipos de terrenos:
- **WATER** Representa el agua en el mapa. Sirve para disminuir el nivel
    de sed de los agentes. En caso de ingresar a esta casilla cualquier agente
    muere por ahogamiento.
- **FLOOR** Representa el terreno sólido en el mapa. Los agentes pueden moverse
    libremente por este tipo de terreno.

### Características

Cualquier casilla de _FLOOR_ puede contener características adicionales, que le
permiten interactuar de manera diferente con los agentes.
- **GRASS** Las casillas con esta caraterísticas permitiran un desplazamiento
    más fácil para los agentes que viajen por este tipo de terreno.
- **FOOD** Estas casillas contienen alimento que podrá ser consumido por los
    conejos para disminuir su hambre. Una vez consumidos se regeneran luego
    de transcurrido un tiempo predefinido.

