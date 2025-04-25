def mass_to_energy():
    C = 299792458  # Speed of light in meters per second
    
    try:
        mass = float(input("Enter kilos of mass: "))
        energy = mass * C**2
        print("e = m * C^2...")
        print(f"m = {mass} kg")
        print(f"C = {C} m/s")
        print(f"{energy:.12e} joules of energy!")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
    except KeyboardInterrupt:
        print("\nProgram terminated.")

if __name__ == "__main__":
    mass_to_energy()