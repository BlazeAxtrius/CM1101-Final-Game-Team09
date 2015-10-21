item_id = {
    "id": "id",

    "name": "id card",

    "description":
    """Your new shiny student ID card. Your picture really doesn't show your best features
    and you really regret the cringy smile.""",

    "mass": 0.5,
    
    "isPotion": False,
}

item_knife = {
    "id": "knife",

    "name": "a kitchen knife",

    "description":
    """Light and very sharp from the looks of it.
    This knife will certainly come in handy. """,

    "mass": 0.75, 
        
    "isPotion": False,
}

item_wood_sword = {
    "id": "wsword",

    "name": "a wooden sword",

    "description":
    """Light and not very sharp. This weapon will
     help you a bit.""",

    "mass": 0.75,

    "isPotion": False,
}

# item_leather_armor = {
#     "id": "larmor",
#
#     "name": "leather armor",
#
#     "description":
#     """Light but not very safe. Still protects you a little.""",
#
#     "mass": 0.75,
#
#     "isPotion": False,
# }

item_money = {
    "id": "money",

    "name": "money",

    "description":
    "This wad of cash is barely enough to pay your tuition fees.",

    "mass": 0.75,
    
    "isPotion": False,
}

item_biscuits = {
    "id": "biscuits",

    "name": "a pack of biscuits",

    "description": """These biscuits look fairly new and you are tempted to take one.
    After all, you can't really pass up free food as a student""",

    "mass": 1,
    
    "isPotion": False,
}

item_pen = {
    "id": "pen",
    
    "name": "a pen",

    "description": """A basic ballpoint pen. One end seems to have been chewed slightly.""",

    "mass": 0.5,
    
    "isPotion": False,
}

item_card = {
    "id": "card",
    
    "name": "card with a mobile number",

    "description": """This card has a mobile number wrote on it. I wonder who's 
number it is?""",

    "mass": 0.05,
    
    "isPotion": False,
}

item_note = {
    "id": "note",
    
    "name": "the note from outside",

    "description": """This is the note you picked up from outside""",

    "mass": 0.05,
    
    "isPotion": False,
}

item_clue = {
    "id": "clue",
    
    "name": "a piece of paper with writing on",

    "description": """Reading will reveal things that you don't want to know and will never forget.""",

    "mass": 0.05,
    
    "isPotion": False,
}

item_plank = {
    "id": "plank",

    "name": "a large, wooden plank",

    "description": """This could easily support your weight""",

    "mass": 5.0,
    
    "isPotion": False,
}

item_brass_key = {
    "id": "bkey",
    
    "name": "a brass key",
    
    "description": "The key allows you to open doors with brass locks",

    "mass": 0.2,
    
    "isPotion": False,

}

item_rusty_key = {
    "id": "rkey",
    
    "name": "rusty key",
    
    "description": "The key allows you to open doors with rusty locks",

    "mass": 0.2,
    
    "isPotion": False,
}

item_metal_key = {
    "id": "mkey",
    
    "name": "metal key",
    
    "description": "The key allows you to open doors with metal locks",
    
    "mass": 0.2,
    
    "isPotion": False,
}

item_copper_key = {
    "id": "ckey",
    
    "name": "copper key",
    
    "description": "The key allows you to open doors with copper locks",
    
    "mass": 0.2,
    
    "isPotion": False,
}


item_lamp = {
    "id": "lamp",
    
    "name": "an oil lamp",
    
    "description": """This oil lamp has just enough for you to see exits in
    the room which you are in and the furniture within the room.
    However its light is too dim to see the floor, you even struggle to see your own feet.""",

    "mass": 2.0,
    
    "isPotion": False,
}

item_torch = {
    "id": "torch",
    
    "name": "a torch",
    
    "description": "The torch allows you to see everything in the dark.",

    "mass": 0.5,
    
    "isPotion": False,
}

item_potion_health = {
    "id": "health",

    "name": "health potion",

    "description": """This small flask feels warm to the touch. Opening it releases
a strong and sweet aroma that fills your exhausted body with vigor. Imagine 
what drinking it would do.""",

    "mass": 2.0,

    "isPotion": True
}

item_potion_mana = {
    "id": "mana",

    "name": "Mana Potion",

    "description":
    "This glass bottle buzzes almost as if with electricity, in fact you're sure it just sparked",

    "mass": 2.0,

    "isPotion": True
}

item_potion_damage = {
    "id": "damage",

    "name": "Damage Potion",

    "description":
    "The damage you deal is doubled while this potion is active.",

    "mass": 2.0,

    "isPotion": True
}

item_potion_defense = {
    "id": "defense",

    "name": "Defense Potion",

    "description":
    "The defense you have is twice as great while this potion is active.",

    "mass": 2.0,

    "isPotion": True
}

all_items = {
    "id": item_id,
    "knife": item_knife,
    "wsword": item_wood_sword,
    # "larmor": item_leather_armor,
    "money": item_money,
    "biscuits": item_biscuits,
    "pen": item_pen,
    "card": item_card,
    "note": item_note,
    "plank": item_plank,
    "rkey": item_rusty_key,
    "lamp": item_lamp,
    "torch": item_torch,
    "mkey": item_metal_key,
    "bkey": item_brass_key,
    "ckey": item_copper_key,
    "health": item_potion_health,
    "mana": item_potion_mana,
    "damage": item_potion_damage,
    "defense": item_potion_defense,
    "clue": item_clue
}
