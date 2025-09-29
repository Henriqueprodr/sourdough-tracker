import json
from datetime import date

class Config():
    """Configure the script and save the user's information"""

    def __init__(self, jar_weight: int, keep_target: int, ratio: tuple[int, int, int], path: str):
        self.jar_weight = jar_weight
        self.keep_target = keep_target
        self.ratio = ratio
        self.path = path

    # Save the initial config.json file during configuration
    def save(self, filename="config.json") -> None:
        try:
            with open(filename,"w+") as f:
                json.dump(self.__dict__, f, indent=4)
        except (OSError, TypeError) as e:
            print(f"Could not save config: {e}")

    # Load the config.json file
    @classmethod
    def load(cls, filename="config.json") -> "Config":
        try:
            with open(filename, "r") as f:
                data = json.load(f)
            return cls(**data)
        except (FileNotFoundError, json.JSONDecodeError, PermissionError, TypeError) as e:
            raise e
        
class Feeding():
    """Update and track the sourdough starter information"""

    def __init__(self, jar_weight_total: int, config: Config, smell: str, peak_hours: int, notes: str):
        self.date = date.today().isoformat()
        self.jar_weight_total = jar_weight_total
        self.config = config
        self.starter_weight = jar_weight_total - config.jar_weight
        self.smell = smell
        self.peak_hours = peak_hours
        self.notes = notes

    def target_weight(self) -> int:
        target_total_weight = self.config.jar_weight + self.config.keep_target
        return target_total_weight

    def flour_and_water(self) -> tuple[int, int]:
        flour = self.config.keep_target * self.config.ratio[1]
        water = self.config.keep_target * self.config.ratio[2]
        return flour, water
    
    def to_row(self) -> list:
        flour, water = self.flour_and_water()
        return [
            self.date,
            self.jar_weight_total,
            self.starter_weight,
            self.target_weight(),
            flour,
            water,
            self.smell,
            self.peak_hours,
            self.notes]