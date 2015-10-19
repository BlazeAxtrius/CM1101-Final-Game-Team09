# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 15:08:33 2015

@author: KHADIJA
"""


from items import *


room_hallway_g_w = { 
        "name": "hallway, G, W",
                
        "description":
        """Y...........................................
        
        
        .""",

    "exits": {"north" : "dining room, G, W", "south": "lounge, G, W", "east": "hallway, G, C, W"},

    "items": []
}



room_hallway_g_e = {
    "name": "hallway, G, E",

    "description":
    """Y...............................................


    .""",

    "exits": {"west": "hallway, G, C, E", "up": "hallway, F1, S", "down": "hallway, F-1"}, 

    "items": []
}  



room_hallway_g_c_w = {
    "name": "hallway, G, C, W",

    "description": 
    """Y...............................................


    .""",

    "exits": {"west": "hallway, G, W", "north": "dining room, G, E", "south": "lounge, G, E"},

    "items": []
}



room_hallway_g_c_e = {
    "name": "hallway, G, C, E",

    "description": 
    """Y...............................................


    .""",

    "exits": {"north": "kitchen", "south": "office, G", "east": "hallway, G, E"},

    "items": []
}

            
            
room_dining_w = { 
        "name": "dining room, G, W",
                
        "description":
        """Y...........................................
        
        
        .""",

    "exits": {"south" : "hallway, G, W", "east": "dining room, G, E"},

    "items": []
}    



room_dining_e = {
    "name": "dining room, G, E",

    "description":
    """Y...............................................


    .""",

    "exits": {"west": "dining room, G, W", "east": "kitchen, G", "south": "hallway, G, C, W"},

    "items": []
}


 
room_kitchen = { 
        "name": "kitchen,G",
                
        "description":
        """Y...........................................
        
        
        .""",

    "exits": {"south" : "hallway, G, C, E", "west": "dining room, G, E"},

    "items": []
}     


room_office = { 
        "name": "office,G",
                
        "description":
        """Y...........................................
        
        
        .""",

    "exits": {"north" : "hallway, G, C, E", "west": "lounge, G, E"},

    "items": []
}  
    
room_lounge_e = { 
        "name": "lounge, G, E",
                
        "description":
        """Y...........................................
        
        
        .""",

    "exits": {"north" : "hallway, G, C, W", "east": "office, G", "west": "lounge, G, W"},

    "items": []
}    


room_lounge_w = {
    "name": "lounge, G, W",

    "description": 
    """Y...............................................


    .""",

    "exits": {"north": "hallway, G, W", "east": "lounge, G, E"}, 

    "items": []
}



room_store = { 
        "name": "store,F-1",
                
        "description":
        """Y...........................................
        
        
        .""",

    "exits": {"north" : "pantry, F-1", "south": "wine cellar, F-1", "east": "hallway, F-1"},

    "items": []
}    

room_pantry = { 
        "name": "pantry,F-1",
                
        "description":
        """Y...........................................
        
        
        .""",

    "exits": {"south" : "store, F-1", "east": "torture, F-1"},

    "items": []
}    

room_torture = { 
        "name": "torture,F-1",
                
        "description":
        """Y...........................................
        
        
        .""",

    "exits": {"west" : "pantry, F-1", "south": "hallway, F-1"},

    "items": []
}    

room_hallway_b = { 
        "name": "hallway,F-1",
                
        "description":
        """Y...........................................
        
        
        .""",

    "exits": {"north" : "torture, F-1", "south": "workshop, F-1", "west": "store, F-1", "up": "hallway, G, E"},

    "items": []
}    

room_secret = { 
        "name": "secret room,F-1",
                
        "description":
        """Y...........................................
        
        
        .""",

    "exits": {"west" : "workshop, F-1"},

    "items": []
}    

room_workshop = { 
        "name": "workshop,F-1",
                
        "description":
        """Y...........................................
        
        
        .""",

    "exits": {"west" : "wine cellar, F-1", "east": "secret, F-1", "north": "hallway, F-1"},

    "items": []
}    

room_winecellar = { 
        "name": "wine cellar,F-1",
                
        "description":
        """Y...........................................
        
        
        .""",

    "exits": {"north" : "store, F-1", "east": "workshop, F-1"},

    "items": []
}    

room_hallway_f_s = { 
        "name": "hallway, F1, S",
                
        "description":
        """Y...........................................
        
        
        .""",

    "exits": {"north" : "hallway, F1, E", "west": "master bedroom, F1", "down": "hallway, G, E" },

    "items": []
}    


room_hallway_f_e = {
    "name": "hallway, F1, E",

    "description":
    """Y................................................


    .""",

    "exits": {"south": "hallway, F1, S", "west": "hallway, F1, N"},

    "items": []
}


room_hallway_f_n = {
    "name": "hallway, F1, N",

    "description":
    """Y.................................................


    .""",

    "exits": {"west": "hallway, F1, W", "south": "master bedroom, F1", "east": "hallway, F1, E"},

    "items": []
}


room_hallway_f_w = {
    "name": "hallway, F1, W",

    "description": 
    """Y..................................................


    .""",

    "exits": {"south": "child bedroom, F1", "east": "hallway, F1, N"},

    "items": []
}


room_child = { 
        "name": "child bedroom,F1",
                
        "description":
        """Y...........................................
        
        
        .""",

    "exits": {"north" : "hallway, F1, W", "east": "master bedroom, F1", "south": "store, F1"},

    "items": []
}    


room_store = { 
        "name": "store,F1",
                
        "description":
        """Y...........................................
        
        
        .""",

    "exits": {"north" : "child bedroom, F1", "east": "bathroom, F1"},

    "items": []
}    


room_bathroom = { 
        "name": "bathroom,F1",
                
        "description":
        """Y...........................................
        
        
        .""",

    "exits": {"north" : "master bedroom, F1", "west": "store, F1"},

    "items": []
}    

room_master = { 
        "name": "master bedroom,F1",
                
        "description":
        """Y...........................................
        
        
        .""",

    "exits": {"north" : "hallway, F1, N", "south": "bathroom, F1", "west": "child bedroom, F1", "east": "hallway, F1, S"},

    "items": []
}    


rooms = { 
        
       "hallway, G, W": room_hallway_g_w,
       "hallway, G, E": room_hallway_g_e,
       "hallway, G, C, W": room_hallway_g_c_w,
       "hallway, G, C, E": room_hallway_g_c_e,
       "dining room, G, W": room_dining_w,
       "dining room, G, E": room_dining_e,
       "kitchen,G": room_kitchen,
       "office,G": room_office,
       "lounge, G, E": room_lounge_e,
       "lounge, G, W": room_lounge_w,
       "store,F-1": room_store,
       "pantry,F-1": room_pantry,
       "torture,F-1": room_torture,
       "hallway,F-1": room_hallway_b,
       "secret room,F-1": room_secret,
       "workshop,F-1": room_workshop,
       "wine cellar,F-1": room_winecellar,
       "hallway, F1, S": room_hallway_f_s,
       "hallway, F1, E": room_hallway_f_e,
       "hallway, F1, N": room_hallway_f_n,
       "hallway, F1, W": room_hallway_f_w,
       "child bedroom,F1": room_child,
       "store,F1": room_store,
       "bathroom,F1": room_bathroom,
       "master bedroom,F1": room_master
 }

