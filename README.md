# EA exercise routine optimization

### Before executing the notebook, make sure to install the required dependencies

Use the `requirements.txt` file to install all necessary packages.

### Install dependencies:

```bash
pip install -r requirements.txt
```

Ensure you have the correct Python environment activated before running the command.

## Fitness Function
$$
fitness = 100 \cdot \frac{\sum_{i=1}^{NumeroEjercicios} y}{NúmeroEjercicios} \cdot \frac{MinUsados}{MinTotales} \cdot \frac{MúsculosEjercitados}{MúsculosSolicitados} \cdot \frac{\sum_{i=1}^{NumeroEjercicios} x}{NúmeroEjercicios} \cdot (0.1 \cdot \frac{EquipamientoUsado}{EquipamientoDisponible} + 0.9)
$$

## Penalizaciones de Fitness

### Ejercicios iguales (implementado con un *for* iterado)  
- muy seguidos (0 - 2 ejs distancia) [y = 0.95]  
- seguidos (3 - 8 ejs distancia) [y = 0.99]  
- separados (9+ ejs distancia) [y = 1]

$$
fitness \cdot \frac{\sum_{i=1}^{NumeroEjercicios} y}{NúmeroEjercicios}
$$ 

### Minutos ocupados
$$
fitness \cdot \frac{MinUsados}{MinTotales}
$$

### Músculos ejercitados
$$
fitness \cdot \frac{MúsculosEjercitados}{MúsculosSolicitados}
$$

En caso de que no exceda 100 el fitness:
- Se sumará 0.05 por cada músculo extra de body region diferente.
- Se sumará 0.1 por cada músculo extra del mismo body region.
<br>

### Dificultad
$$
fitness \cdot \frac{\sum_{i=1}^{NumeroEjercicios} x}{NúmeroEjercicios}
$$  

- Si el ejercicio es de dificultad superior al usuario:  
$x = 1 - 0.3 \cdot diferencia$  

- Si el ejercicio es de dificultad inferior al usuario:  
$x = 1 - 0.2 \cdot diferencia$

### Uso de Equipamiento
$$
fitness \cdot 0.1 \cdot \frac{EquipamientoUsado}{EquipamientoDisponible} + 0.9
$$ 

## Constraints

### Soft Constraints
- Porcentaje Mínimo de ejercicios de músculos solicitados (80%).

### Hard Constraints
- Equipamiento no disponible.
- No se puede exceder el tiempo disponible de la rutina.

## Codificación

### Duración de Ejercicios (Proporcional al nivel de dificultad):
- Beginner &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 10 min  
- Novice &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 12 min  
- Intermediate &nbsp; 14 min  
- Advanced &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 16 min  
- Expert &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 18 min  
- Master &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 20 min  

### Solución Codificada:
| --- | Exercise_ID |
|----------|----------|
| Ex1   | 4   |
| Ex2   | 2851   |
| Ex3   | 26   |
| Ex4   | 550   |
| Ex5   | 1   |
