class Glassware:
    # Parent class
    def __init__(self, name="Glassware"):
        self.name = name

class Beaker(Glassware):
    # Beaker inherits from Glassware (Inheritance)
    def __init__(self, volume_ml):
        super().__init__("Beaker")
        self.volume_ml = volume_ml

    def __str__(self):
        return f"{self.volume_ml}ml Beaker"

class Tray:
    # Tray creates and owns 5 beakers (Composition)
    def __init__(self):
        # If the Tray gets deleted, these beakers are lost with it
        self.beakers = [Beaker(250) for _ in range(5)]

    def show_inventory(self):
        print("Tray Inventory:")
        for i, beaker in enumerate(self.beakers, 1):
            print(f"  - Slot {i}: {beaker}")

# --- Test it out ---
if __name__ == "__main__":
    my_tray = Tray()
    my_tray.show_inventory()

    # Deleting the tray also deletes the beakers inside it
    del my_tray
