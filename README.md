# EA exercise routine optimization

### Before executing the notebook, make sure to install the required dependencies

Use the `requirements.txt` file to install all necessary packages.

### Install dependencies:

```bash
pip install -r requirements.txt
```

Ensure you have the correct Python environment activated before running the command.

## Fitness Function

//TODO

## Penalizaciones de Fitness

### - Ejercicios iguales (implementado con un for iterado)
#### -> muy seguidos (0 - 2 ejs distancia) [* 0.95]
#### -> seguidos (3 - 8 ejs distancia) [* 0.99]
#### -> separados (9+ ejs distancia) [No penaliza]

### - Minutos ocupados
$$
\frac{MinUsados}{MinTotales}
$$

### - Músculos ejercitados
$$
\frac{MúsculosEjercitados}{MúsculosSolicitados}
$$
#### -> En caso de que no exceda 100 el fitness, se sumará 0.05 por cada músculo extra




## Codificación

### - Duración de Ejercicios (Proporcional al nivel de dificultad):
#### -> Beginner - 10
#### -> Novice - 12
#### -> Intermediate 14
#### -> Advanced - 16
#### -> Expert - 18
#### -> Master - 20
#### -> Grand Master - 22
#### -> Legendary - 24
