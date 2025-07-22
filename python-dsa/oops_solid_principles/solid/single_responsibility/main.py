from vehicle import Vehicle
from object_formatter import ObjectFormatter
from insurance_calculator import InsuranceCalculator

def main():
    vehicle = Vehicle("Toyota", "Camry", 2024)
    formatter = ObjectFormatter()
    insurance_calculator = InsuranceCalculator()

    print(f"Car insurance cost: ${insurance_calculator.calculate_car_insurance(vehicle)}")
    print(f"Vehicle JSON: {formatter.vehicle_to_json(vehicle)}")

if __name__ == "__main__":
    main()