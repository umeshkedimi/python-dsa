from vehicle import Vehicle

class InsuranceCalculator:
    def calculate_car_insurance(self, vehicle: Vehicle):
        # Example insurance calculation logic
        base_rate = 500
        age_factor = 2023 - vehicle.year
        insurance_cost = base_rate + (age_factor * 20)
        return insurance_cost