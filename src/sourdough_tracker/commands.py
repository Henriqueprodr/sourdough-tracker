import json
import logging
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
            logging.info(f"Content saved successfully to {filename}")
        except (OSError, TypeError) as e:
            logging.error(f"Could not save {filename}: {e}")


    # Load the config.json file
    @classmethod
    def load(cls, filename="config.json") -> "Config":
        try:
            with open(filename, "r") as f:
                data = json.load(f)
            logging.info(f"Content loaded successfully from {filename}")
            return cls(
                jar_weight=data["jar_weight"],
                keep_target=data["keep_target"],
                ratio=tuple(data["ratio"]),
                path=data["path"]
                )
        except (FileNotFoundError, json.JSONDecodeError, PermissionError, TypeError) as e:
            logging.error(f"Failed to load {filename}: {e}")
            raise
        
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

    def target_total_weight(self) -> int:
        """Return total grams (jar + kept starter) after discard."""
        target_total_weight = self.config.jar_weight + self.config.keep_target
        if self.config.keep_target <= 0:
            logging.error(f"Invalid keep_target: {self.config.keep_target} - must be positive")
            raise ValueError("keep_target must be a positive number of grams to keep")
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
            self.target_total_weight(),
            flour,
            water,
            self.smell,
            self.peak_hours,
            self.notes]