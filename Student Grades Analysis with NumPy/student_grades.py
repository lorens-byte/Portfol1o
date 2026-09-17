import numpy as np

grades = np.random.randint(0, 101, size=(100, 3))

average = np.mean(grades, axis=1)

print("Перші 10 студентів:")
print(grades[:10])

print("Середній бал:")

for i in range(10):
    print(f"Студент {i + 1}: {average[i]:.2f}")