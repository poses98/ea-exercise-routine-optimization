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

### Ejercicios iguales (implementado con un *for* iterado)  
- muy seguidos (0 - 2 ejs distancia) [* 0.95]  
- seguidos (3 - 8 ejs distancia) [* 0.99]  
- separados (9+ ejs distancia) [No penaliza]  

### Minutos ocupados
$$
\frac{MinUsados}{MinTotales}
$$

### Músculos ejercitados
$$
\frac{MúsculosEjercitados}{MúsculosSolicitados}
$$  
- En caso de que no exceda 100 el fitness, se sumará 0.05 por cada músculo extra
<br>

## Codificación

### Duración de Ejercicios (Proporcional al nivel de dificultad):
- Beginner &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 10 min  
- Novice &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 12 min  
- Intermediate &nbsp; 14 min  
- Advanced &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 16 min  
- Expert &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 18 min  
- Master &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 20 min  
- Grand Master &nbsp;22 min  
- Legendary &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 24 min  
