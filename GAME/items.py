from Potions_items import *

item_id = {
    "id": "id",

    "name": "id card",

    "description":
    """Your new shiny student ID card. Expires 1 June 2017.
You wonder why they have printed a suicide hotline number on it?...""",

    "mass": 0.5,
    
    "isPotion": False,
}

item_knife = {
    "id": "knife",

    "name": "a kitchen knife",

    "description":
    "It is very sharp",

    "mass": 0.75, 
        
    "isPotion": False,
}

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

    "description": "A pack of biscuits.",

    "mass": 1,
    
    "isPotion": False,
}

item_pen = {
    "id": "pen",
    
    "name": "a pen",

    "description": "A basic ballpoint pen.",

    "mass": 0.5,
    
    "isPotion": False,
}

item_card = {
    "id": "card",
    
    "name": "a card with a mobile number",

    "description": """This card has a mobile number wrote on it. I wonder who's 
number it is?""",

    "mass": 0.05,
    
    "isPotion": False,
}

item_note = {
    "id": "note",
    
    "name": "the note from outside",

    "description": """This is the note you pick up from outside""",

    "mass": 0.05,
    
    "isPotion": False,
}

item_clue = {
    "id": "clue",
    
    "name": "a piece of paper with writing on",

    "description": """Use books will reveal a horror you don't want to experience""",

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
    "id" : "bkey",
    
    "name": "a brass key",
    
    "description": "The key allows you to open doors with brass locks",

    "mass" : 0.2,
    
    "isPotion": False,

}

item_rusty_key = {
    "id" : "rkey",
    
    "name": "a rusty key",
    
    "description": "The key allows you to open doors with rusty locks",

    "mass" : 0.2,
    
    "isPotion": False,
}

item_metal_key = {
    "id": "mkey",
    
    "name": "a metal key",
    
    "description": "The key allows you to open doors with metal locks",
    
    "mass" : 0.2,
    
    "isPotion": False,
}

item_lamp = {
    "id": "lamp",
    
    "name": "an oil lamp",
    
    "description": """This oil lamp has just enough for you to see exits in the
room items you can look in. But you may need to find something else if you
want to look at the floor""",

    "mass": 2.0,
    
    "isPotion": False,
}

item_torch = {
    "id" : "torch",
    
    "name": "a torch",
    
    "description": "The torch allows you to see everything in the dark.",

    "mass" : 0.5,
    
    "isPotion": False,
}

item_potion_health = {
    "id": "health",

    "name": "health potion",

    "description": """This small flask feels warm to the touch. Opening it releases
a strong and sweet aroma that fills your exhausted body with vigor. Imagine 
what drinking it would do.""",

    "mass": 2.0,

    "isPotion": True,
}

all_items = {
    "id": item_id,
    "knife": item_knife,
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
    "health": item_potion_health

}


