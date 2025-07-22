import json
from vehicle import Vehicle

class ObjectFormatter:
    def vehicle_to_json(self, vehicle: Vehicle):
        return json.dumps({
            "make": vehicle.make,
            "model": vehicle.model,
            "year": vehicle.year,
        })