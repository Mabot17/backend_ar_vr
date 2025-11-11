from fastapi import FastAPI, HTTPException
from services.data_loader import get_players, get_weapons, get_armors

app = FastAPI(title="XR Cards API", version="1.0.0")

@app.get("/")
def home():
    return {"message": "XR Cards API is running"}

# ------------------------------
# PLAYERS
# ------------------------------

@app.get("/players")
def players():
    return get_players()

@app.get("/players/{user_id}")
def player_detail(user_id: str):
    data = get_players()
    for player in data:
        if player["user_id"] == user_id:
            return player
    raise HTTPException(404, "Player not found")

# ------------------------------
# WEAPONS
# ------------------------------

@app.get("/weapons")
def weapons():
    return get_weapons()

@app.get("/weapons/{card_id}")
def weapon_detail(card_id: str):
    data = get_weapons()
    for item in data:
        if item["card_id"] == card_id:
            return item
    raise HTTPException(404, "Weapon not found")

# ------------------------------
# ARMORS
# ------------------------------

@app.get("/armors")
def armors():
    return get_armors()

@app.get("/armors/{card_id}")
def armor_detail(card_id: str):
    data = get_armors()
    for item in data:
        if item["card_id"] == card_id:
            return item
    raise HTTPException(404, "Armor not found")
