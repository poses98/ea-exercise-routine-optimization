import pandas as pd
import random

# Possible values
user_levels = {
    "beginner": 0,
    "novice": 1,
    "intermediate": 2,
    "advanced": 3,
}

equipment_list = [
    "Kettlebell", "Dumbbell", "Barbell", "Clubbell", "Bodyweight",
    "Sliders", "Gymnastic Rings", "Macebell", "Suspension Trainer",
    "Cable", "Landmine", "Stability Ball", "Heavy Sandbag", "Pull Up Bar",
    "Parallette Bars", "Sandbag", "Weight Plate", "Bulgarian Bag",
    "Resistance Band", "Miniband", "Superband", "Battle Ropes", "Tire", "EZ Bar"
]

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

for _ in range(20):
    userLevel = random.choice(list(user_levels.keys()))
    
    # Equipment: either "Gym" or a random sample of equipment
    if random.random() < 0.2:  # 20% chance to be "Gym"
        equipment = ["Gym"]
    else:
        num_equipment = random.randint(0, 5)
        equipment = random.sample(equipment_list, num_equipment)
    
    num_muscles = random.randint(2, 6)
    # Selección ponderada de músculos únicos
    requestMuscles = random.choices(muscles_list, weights=muscle_weights, k=num_muscles)
    requestMuscles = list(set(requestMuscles))  # Eliminar duplicados

    # Si al eliminar duplicados quedó corto, volver a completar
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
