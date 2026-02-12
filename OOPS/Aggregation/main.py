class Power:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __str__(self):
        return f"{self.name} (Level {self.level})"

class Hero:
    def __init__(self, name, power=None):
        self.name = name
        self.power = power  # Aggregation: Hero HAS-A Power

    def display_profile(self):
        if self.power:
            print(f"Hero: {self.name}, using {self.power}")
        else:
            print(f"Hero: {self.name} is currently powerless.")

# 1. Create a Power object independently
laser_eyes = Power("Laser Eyes", 90)

# 2. Create a Hero and aggregate the Power
homelander = Hero("Homelander", laser_eyes)
homelander.display_profile()

# 3. Demonstration of independence:
# If the Hero object is deleted, the Power object still exists.
print("\nDeleting the Hero object...")
del homelander

# The 'laser_eyes' object is still accessible
print(f"The power object still exists: {laser_eyes}")
