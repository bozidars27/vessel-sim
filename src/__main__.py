from models.vessel import Vessel
import random

def instantiate_vessels():
    vessels = []

    for i in range(5):
        angle = random.uniform(0, 2 * 3.14159)
        radius = random.uniform(0, 1000)
        x = radius * random.uniform(-1, 1)
        y = (radius**2 - x**2) ** 0.5 * (1 if random.random() > 0.5 else -1)

        vessel = Vessel(
            name=f"Vessel_{i+1}",
            length=random.uniform(20, 300),
            width=random.uniform(5, 40),
            draft=random.uniform(2, 12),
            x=x,
            y=y
        )

        vessels.append(vessel)

    return vessels

def move_vessels(vessels):
    for v in vessels:
        dx = random.uniform(-50, 50)
        dy = random.uniform(-50, 50)
        v.move(dx, dy)

def main():
    vessels = instantiate_vessels()

    print("Initial vessel positions:")
    for v in vessels:
        print(f"{v.name}: ({v.x:.2f}, {v.y:.2f})")

    move_vessels(vessels)

    print("\nFinal vessel positions after simulation:")
    for v in vessels:
        print(f"{v.name}: ({v.x:.2f}, {v.y:.2f})")

if __name__ == "__main__":
    main()