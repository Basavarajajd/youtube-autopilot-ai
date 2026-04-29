import json
from pathlib import Path
from datetime import datetime
from core.logger import logger

MEMORY_FILE = Path("brain_memory.json")


class BrainMemory:
    def __init__(self):
        if not MEMORY_FILE.exists():
            logger.info("🧠 Creating new brain memory")
            self.memory = {}
            self._save()
        else:
            with open(MEMORY_FILE, "r") as f:
                self.memory = json.load(f)
            logger.info("🧠 Brain memory loaded")

    # --------------------------
    # Save memory
    # --------------------------
    def save(self, key, value):
        logger.info(f"💾 Saving to brain: {key}")
        self.memory[key] = {
            "value": value,
            "timestamp": str(datetime.now())
        }
        self._save()

    # --------------------------
    # Load memory
    # --------------------------
    def load(self, key):
        return self.memory.get(key, None)

    # --------------------------
    # Internal save
    # --------------------------
    def _save(self):
        with open(MEMORY_FILE, "w") as f:
            json.dump(self.memory, f, indent=2)
