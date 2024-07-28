import os
import math

# Program information
__author__ = "CN8FF"
__version__ = "1.0"
__title__ = "Ham Radio RF Power Calculation"

# Function to clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Conversion of Watts to dBm
def watts_to_dbm(watts):
    dbm = 10 * math.log10(watts * 1000)
    return dbm

# Conversion of dBm to Watts
def dbm_to_watts(dbm):
    watts = 10 ** (dbm / 10) / 1000
    return watts

# Calculate output power after attenuation
def attenuation_output(input_power_watts, attenuation_db):
    output_power_watts = input_power_watts / (10 ** (attenuation_db / 10))
    return output_power_watts

# Calculate output power after amplification
def amplification_output(input_power_watts, amplification_db):
    output_power_watts = input_power_watts * (10 ** (amplification_db / 10))
    return output_power_watts

def main():
    while True:
        clear_screen()  # Clear the screen at the beginning of each iteration
        print(f"{__title__} by {__author__} (Version {__version__})")
        print("\nMenu:")
        print("1. Convert Watts to dBm")
        print("2. Convert dBm to Watts")
        print("3. Calculate Attenuation")
        print("4. Calculate Amplification")
        print("5. Quit")

        choice = input("Choose an option: ")

        if choice == '1':
            watts = float(input("Enter power in Watts: "))
            dbm = watts_to_dbm(watts)
            print(f"{watts} W is equivalent to {dbm:.2f} dBm\n")
            input("Press Enter to return to the menu...")

        elif choice == '2':
            dbm = float(input("Enter power in dBm: "))
            watts = dbm_to_watts(dbm)
            print(f"{dbm} dBm is equivalent to {watts:.6f} W\n")
            input("Press Enter to return to the menu...")

        elif choice == '3':
            input_power = float(input("Enter input power in Watts: "))
            attenuation_db = float(input("Enter attenuation in dB: "))
            output_power = attenuation_output(input_power, attenuation_db)
            print(f"Output power after {attenuation_db} dB attenuation: {output_power:.6f} W\n")
            input("Press Enter to return to the menu...")

        elif choice == '4':
            input_power = float(input("Enter input power in Watts: "))
            amplification_db = float(input("Enter amplification in dB: "))
            output_power = amplification_output(input_power, amplification_db)
            print(f"Output power after {amplification_db} dB amplification: {output_power:.6f} W\n")
            input("Press Enter to return to the menu...")

        elif choice == '5':
            print("Goodbye!")
            break

        else:
            print("Invalid option, please try again.\n")
            input("Press Enter to return to the menu...")

if __name__ == "__main__":
    main()
