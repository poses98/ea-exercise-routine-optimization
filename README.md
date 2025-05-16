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
fitness = 100 \cdot \frac{\sum_{i=1}^{NumeroEjercicios} y}{NúmeroEjercicios} \cdot (Cobertura \cdot Equilibrio) \cdot \frac{\sum_{i=1}^{NumeroEjercicios} x}{NúmeroEjercicios} \cdot (0.1 \cdot \frac{EquipamientoUsado}{EquipamientoDisponible} + 0.9)
$$

## Penalizaciones de Fitness

### Ejercicios iguales y/o repetidos
- muy seguidos (0 - 2 ejs distancia) [y = 0.2]  
- seguidos (3 - 8 ejs distancia) [y = 0.4]  
- separados (9+ ejs distancia) [y = 0.6]

$$
fitness \cdot \frac{\sum_{i=1}^{NumeroEjercicios} y}{NúmeroEjercicios}
$$ 

### Músculos ejercitados
#### - Cobertura:
Se toma en cuenta la cantidad de ejercicios que entrenan músculos solicitados en relación a la cantidad total de ejercicios en la rutina:

$$
Cobertura = \frac{MúsculosEjercitados}{MúsculosSolicitados}
$$

#### - Equilibrio:
Se valora que haya un reparto equitativo entre todos los ejercicios que entrenan músculos solicitados:

$$
Equilibrio = 1 - \frac{{\sum_{m=1}^{MúsculosSolicitados}} |{EjerciciosMúsculoSolicitado}[m] - CantidadIdeal|} {TotalEjerciciosSolicitados}
$$

### Ejercicios Extra
En caso de que no exceda 100 el fitness:
- Se sumará 0.05 por cada músculo extra de body region diferente.
- Se sumará 0.1 por cada músculo extra del mismo body region.
<br>

### Dificultad
$$
fitness \cdot \frac{\sum_{i=1}^{NumeroEjercicios} x}{NúmeroEjercicios}
$$  

- Si el ejercicio es de dificultad superior al usuario:  
$x = 1 - 0.2 \cdot diferencia$  

- Si el ejercicio es de dificultad inferior al usuario:  
$x = 1 - 0.1 \cdot diferencia$

### Uso de Equipamiento
$$
fitness \cdot 0.1 \cdot \frac{EquipamientoUsado}{EquipamientoDisponible} + 0.9
$$ 

## Constraints

### Soft Constraints
- Porcentaje Mínimo de ejercicios de músculos solicitados (75%).

### Hard Constraints
- No pueden realizarse ejercicios que requieran equipamiento no disponible.
- No se puede exceder el tiempo disponible de la rutina.



## Codificación

### Solución Codificada:
| --- | Exercise_ID |
|----------|----------|
| Ex1   | 4   |
| Ex2   | 2851   |
| Ex3   | 26   |
| Ex4   | 550   |
| Ex5   | 1   |
