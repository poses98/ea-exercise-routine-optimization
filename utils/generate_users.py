import pandas as pd
import random

# Niveles de usuario
user_levels = {
    "beginner": 0,
    "novice": 1,
    "intermediate": 2,
    "advanced": 3,
    "expert": 4,
    "master": 5
}

# Pesos de los equipos
equipment_frequencies = {
    "Kettlebell": 808,
    "Dumbbell": 448,
    "Barbell": 252,
    "Clubbell": 197,
    "Bodyweight": 189,
    "Sliders": 153,
    "Gymnastic Rings": 121,
    "Macebell": 107,
    "Suspension Trainer": 78,
    "Cable": 74,
    "Landmine": 63,
    "Stability Ball": 51,
    "Heavy Sandbag": 51,
    "Pull Up Bar": 48,
    "Parallette Bars": 44,
    "Sandbag": 38,
    "Weight Plate": 37,
    "Bulgarian Bag": 36,
    "Resistance Band": 31,
    "Miniband": 31,
    "Superband": 30,
    "Battle Ropes": 30,
    "Tire": 25,
    "EZ Bar": 24,
    "Trap Bar": 22,
    "Indian Club": 12,
    "Wall Ball": 9,
    "Medicine Ball": 3,
    "Ab Wheel": 2,
    "Slam Ball": 2
}

equipment_list = list(equipment_frequencies.keys())
equipment_weights = list(equipment_frequencies.values())

# Lista de músculos
muscle_frequencies = {
    "Quadriceps": 1296,
    "Shoulders": 497,
    "Abdominals": 404,
    "Glutes": 171,
    "Back": 170,
    "Chest": 153,
    "Biceps": 91,
    "Triceps": 63,
    "Calves": 49,
    "Hamstrings": 41,
    "Forearms": 22,
    "Trapezius": 19,
    "Abductors": 18,
    "Adductors": 14,
    "Shins": 6,
    "Hip Flexors": 2
}

muscles_list = list(muscle_frequencies.keys())
muscle_weights = list(muscle_frequencies.values())

users_data = []

for _ in range(50):
    userLevel = random.choice(list(user_levels.keys()))
    
    # 20% chance de ser 'Gym', si no selecciona ponderado
    if random.random() < 0.4:
        equipment = ["Gym"]
    else:
        num_equipment = random.randint(1, 5)
        equipment = random.choices(equipment_list, weights=equipment_weights, k=num_equipment)
        equipment = list(set(equipment))  # eliminar duplicados
        while len(equipment) < num_equipment:
            extra = random.choices(equipment_list, weights=equipment_weights, k=1)[0]
            if extra not in equipment:
                equipment.append(extra)
    
    num_muscles = random.randint(2, 6)
    requestMuscles = random.choices(muscles_list, weights=muscle_weights, k=num_muscles)
    requestMuscles = list(set(requestMuscles))
    while len(requestMuscles) < num_muscles:
        extra = random.choices(muscles_list, weights=muscle_weights, k=1)[0]
        if extra not in requestMuscles:
            requestMuscles.append(extra)

    duration = random.randint(1, 10)
    userID = random.randint(10000, 99999)
    
    users_data.append({
        "userID": userID,
        "userLevel": userLevel,
        "equipment": ";".join(equipment),
        "requestMuscles": ";".join(requestMuscles),
        "duration": duration
    })

df = pd.DataFrame(users_data)
output_file = "../assets/random_users.csv"
df.to_csv(output_file, index=False)
