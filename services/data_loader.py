import json
from pathlib import Path

BASE_PATH = Path(__file__).resolve().parent.parent
STORE_PATH = BASE_PATH / "store"

def load_json(filename: str):
    file_path = STORE_PATH / filename
    if not file_path.exists():
        raise FileNotFoundError(f"{filename} not found in store/")
    
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def get_players():
    return load_json("player.json")

def get_weapons():
    return load_json("weapon.json")

def get_armors():
    return load_json("armor.json")
