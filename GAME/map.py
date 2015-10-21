from enemies import *
from items import *

cabinet = {
    "name": "Cabinet",

    "items": [item_biscuits]

}

searchable_objects = {
    "Cabinet": cabinet
}

room_entrance = { 
    "name": "Entrance",
                
    "description": """As you close the door behind you it booms with a huge
weight. The hallway that lies in front of you to the east is sparsely 
decorated other than a carpet leading down the room and a grandfather clock
to your right. Upon listening, the clock seems to be broken.""",

    "exits": {"north": "Ground floor west dining room", 
              "south": "Ground floor west lounge", 
              "east": "Ground floor west hallway", 
              "west": "Porch"},
              
    "object_in_room": False,
         
    "search_object": {},
    
    "items": [],
    
    "first_visit": True,

    "enemy": [enemy1]
}


room_hallway_g_e = {
    "name": "Ground floor east hallway",

    "description": """As you leave the stairs you can see a door to the south
and the stairs to the basement to the north. There is a small table against
the wall and on it you can see a torch. The hallway continues to the 
west.""",

    "exits": {"west": "Ground floor central hallway", 
              "up": "First floor south hallway", 
              "down": "Basement hallway"}, 
              
    "object_in_room": False,
              
    "search_object": {},

    "items": [],

    "enemy": []
}


room_hallway_g_w = {
    "name": "Ground floor west hallway",

    "description": """The stacked wood lies to one side of you, blocking your 
path towards the stairs. The hole that you created is to the other side 
like a gaping maw reminding you of the fall. You look for a way around it 
but the wood has broken nearly all the way around. You doubt whether the 
remaining floorboards would support any weight on them at all and decide 
not to find out. """,

    "exits": {"west": "Entrance", 
              "north": "Ground floor east dining room", 
              "south": "Ground floor east lounge"},
               
    "object_in_room": False,
             
    "search_object": {},

    "items": [],

    "enemy": []
}


room_hallway_g_c = {
    "name": "Ground floor central hallway",

    "description": """You can see that there is a pile of what appears to be 
wood in front of you, blocking your path back towards the front door. It 
is impossible to get through or around as it is stacked to the ceiling. 
There are doors to the north and south and the stairway to the east.""",

    "exits": {"north": "Ground floor kitchen", 
              "south": "Ground floor office", 
              "east": "Ground floor east hallway"},
              
    "object_in_room": False,
              
    "search_object": {},

    "items": [],

    "enemy": []
}

            
room_dining_w = { 
    "name": "Ground floor west dining room",
                
    "description": """There is a glass cabinet in the corner of the room with 
what looks like some exotic plates and drawers underneath that. This end of
the table has a very large chair placed at it, as though it was saved for 
someone important. There is a door to the south and the room continues to 
the east.""",

    "exits": {"south": "Entrance", 
              "east": "Ground floor east dining room"},
              
    "object_in_room": False,
              
    "search_object": {},

    "items": [item_metal_key],

    "enemy": []
}    


room_dining_e = {
    "name": "Ground floor east dining room",

    "description": """In the room you can see a large dining table sitting 
below a grand chandelier. Both have seen better days but seem to be sturdy.
There is a cabinet in the corner of the room and the room continues to the 
west. There is also a door to the south. """,

    "exits": {"west": "Ground floor west dining room", 
              "east": "Ground floor kitchen", 
              "south": "Ground floor west hallway"},
               
    "object_in_room": False,
             
    "search_object": {},

    "items": [],

    "enemy": []
}

 
room_kitchen = { 
    "name": "Ground floor kitchen",
                
    "description": """You enter what appears to be a kitchen. You can see an 
oven with a hob in one corner, next to that a sink and a worktop along the 
wall. There are several shelves and cupboards that seem to be broken and 
empty. You can see a rack of cutlery including some larger knives used for 
chopping food. There is a door to the west and to the south.""",

    "exits": {"south": "Ground floor central hallway", 
              "west": "Ground floor east dining room"},
               
    "object_in_room": False,
             
    "search_object": {},

    "items": [item_knife, item_potion_health],

    "enemy": []
}     


room_office = { 
    "name": "Ground floor office",
                
    "description": """As you enter the room you can see a large desk in front 
of you along with a thick leather chair. Behind that there are two large 
bookcases in the corners of the rooms filled with books that are dusted but
look as though they are expensive. """,

    "exits": {"north": "Ground floor central hallway",
              "west": "Ground floor east lounge"},
               
    "object_in_room": False,
            
    "search_object": {},

    "items": [],

    "enemy": []
}  
    
room_lounge_e = { 
    "name": "Ground floor east lounge",
                
    "description": """You can immediately see that this is the lounge. There 
are sofas and armchairs in the centre of the room. To against the wall to 
the south there is a large fireplace although it looks unused for some time
now. There is a door to the north as well as the east and the room 
continues to the west.""",

    "exits": {"north": "Ground floor west hallway", 
              "east": "Ground floor office", 
              "west": "Ground floor west lounge"},
                
    "object_in_room": False,
            
    "search_object": {},

    "items": [item_copper_key],

    "enemy": []
}    


room_lounge_w = {
    "name": "Ground floor west lounge",

    "description": """There is more furniture here, in particular two armchairs
arranged next to a small table, seemingly to encourage conversation. There 
is also a cupboard to in the corner of the room with the doors slightly 
open. There is a door to the north and the room continues to the east.""",

    "exits": {"north": "Entrance", 
              "east": "Ground floor east lounge"}, 
               
    "object_in_room": True,
             
    "search_object": {"south": cabinet},

    "items": [],

    "enemy": []
}


room_storage = { 

    "name": "Basement storage",
                
    "description": """As you pull yourself to your feet once more you can't 
help be thankful for the carpet breaking your fall somewhat. As you fumble 
around in the darkness you realise that you are in a small storage 
cupboard. You can just about make out a rusted oil lamp on a shelf along 
with a match box. You tread carefully avoiding the large pieces of wood 
that have splintered as a result of the fall. You also notice a small 
cupboard in the corner when noises that emanate from it startle you.""",

    "exits": {"north": "Pantry", 
              "south": "Wine Cellar", 
              "east": "Basement hallway"},
               
    "object_in_room": False,
             
    "search_object": {},

    "items": [item_lamp],

    "enemy": []
}    

room_pantry = { 

    "name": "Pantry",
                
    "description": """As you open the door the smell of rotten food hits you 
like a brick wall of gas. Whatever was once in here would appear to be 
inedible now. You can see shelves stacked with some cheeses that have been 
gnawed at by what you would assume were rats along with some other food 
which is too old to distinguish between. You wonder just how long some of 
this has been here. You can see a door to the east and the door that you 
entered the room with.""",

    "exits": {"south": "Basement storage", 
              "east": "Torture room"},
                
    "object_in_room": False,
            
    "search_object": {},

    "items": [item_torch],

    "enemy": []
}    

room_torture = { 
    "name": "Torture room",
                
    "description": """As you enter the room, the light glimmers off some metal 
on the walls. When you look closer, you can see that there are chains and 
shackles bolted to the wall. There appear to be instruments that 
were used to inflict pain covered in congealed blood along with a large red
stain on the floor. You don't want to be in this room for any longer than 
you have to. A door leads to the south and back from where you came.""",

    "exits": {"west": "Pantry", 
              "south": "Basement hallway"},
                
    "object_in_room": False,
            
    "search_object": {},

    "items": [],

    "enemy": []
}    

room_hallway_b = { 
    "name": "Basement hallway",
                
    "description": """The hallway is dingy and very dark. You can see a few 
cobwebs hanging from the corners of the room and the floor is covered in 
dust and dirt. You can't see much more than this. There are doors leading 
to the north and south and a staircase to the east.""",

    "exits": {"north": "Torture room", 
              "south": "Workshop", 
              "west": "Basement storage", 
              "up": "Ground floor east hallway"},
                 
    "object_in_room": False,
           
    "search_object": {},

    "items": [],

    "enemy": []
}    

room_secret = { 
    "name": "Secret room",
                
    "description": """As you enter the room it seems empty at first but as you
look closer you can see a chair and a table in one corner. Upon lifting 
your torch you can see that the walls are covered in writing. As you look 
closer you can clearly see that the words "For all intents and purposes" are 
written over and over with the writing becoming more frantic and jagged
the further around the room you look. Whoever wrote these words was clearly
not in the right frame of mind for anything. You wonder what could drive a 
person to such insanity. As you are about to leave you hear a whisper from 
the corner. As you move closer towards the sound you begin to see a pair of
sunken eyes staring back at you. As you shine a light on the person in the 
corner it becomes very clear; Matt Morgan is rocking back and forth 
uttering the words "for all intents and purposes" under his breath. As you 
reach out to help him he is startled and screams at you "FOR ALL INTENTS 
AND PURPOSES!!!!!" You decide its best to leave him for now, there seems to
be little you can do to comfort him. """,

    "exits": {"west": "Workshop"},
                 
    "object_in_room": False,
           
    "search_object": {},

    "items": [item_plank],

    "enemy": []
}    

room_workshop = { 
    "name": "Workshop",
                
    "description": """Upon entering the room you can see a large wooden table 
in the middle of the room. As you look closer you can see a few vices on 
the sides of the table along with some files and blunt chisels that would 
be used for crafting. An old shelf with some dusty equipment and a few 
books is to the east of the room, you can see what looks to be a door that has
tried to be hidden behind the shelf. But you can't seem to work out how to open it. A door leads
to the north of the room and another from where you came. """,

    "exits": {"west": "Wine Cellar", 
              "east": "Secret room", 
              "north": "Basement hallway"},
                
    "object_in_room": False,
            
    "search_object": {},

    "items": [],

    "enemy": []
}    

room_winecellar = { 
    "name": "Wine Cellar",
                
    "description": """As you enter the room, the large number of wine racks is 
immediately visible. There are a few empty spaces but most are filled with 
bottles that have so much dust on them that the labels can't be read. You 
can also see a door to the east and another from where you came.""",

    "exits": {"north": "Basement storage", 
              "east": "Workshop"},
                
    "object_in_room": False,
            
    "search_object": {},

    "items": [],

    "enemy": []
}    

room_hallway_f_s = { 
    "name": "First floor south hallway",
                
    "description": """As you come up the stairs you can see a long dark 
corridor leading to the north along with a door to the west. The stairs to 
the south lead back downstairs. It is difficult to see much else. """,

    "exits": {"north": "First floor east hallway", 
              "west": "First floor master bedroom", 
              "down": "Ground floor east hallway"},
                
    "object_in_room": False,
            
    "search_object": {},

    "items": [],

    "enemy": []
}    


room_hallway_f_e = {
    "name": "First floor east hallway",

    "description": """As you reach the corner you can see the corridor leads 
west as well as south. There is a small round table in the corner with a 
lamp on top of it.""",

    "exits": {"south": "First floor south hallway", 
              "west": "First floor north hallway"},
                 
    "object_in_room": False,
           
    "search_object": {},

    "items": [],

    "enemy": []
}


room_hallway_f_n = {
    "name": "First floor north hallway",

    "description": """As you move down the corridor you can see a door to the 
south. The corridor continues to the west and to the east.""",

    "exits": {"west": "First floor west hallway", 
              "south": "First floor master bedroom", 
              "east": "First floor east hallway"},
                  
    "object_in_room": False,
          
    "search_object": {},

    "items": [],

    "enemy": []
}


room_hallway_f_w = {
    "name": "First floor west hallway",

    "description": """Reaching the end of the corridor there is a door to the 
south and the corridor goes back to the east.""",

    "exits": {"south": "First floor child's bedroom", 
              "east": "First floor north hallway"},
                   
    "object_in_room": False,
         
    "search_object": {},

    "items": [],

    "enemy": []
}


room_child = { 
    "name": "First floor child's bedroom",
                
    "description": """You realise this is a child's bedroom by the colourful
décor. There is a small cot that looks broken along with a single bed 
against one wall. There is a trunk at the foot of the bed overflowing with 
toys and soft toy animals in another corner; their glass eyes reflecting 
the light of your torch giving them a sinister look. The moonlight shining 
through the dirty window casts long shadows over parts of the room adding 
to the atmosphere of the unknown. There are doors leading to the north, 
east and south""",

    "exits": {"north": "First floor west hallway", 
              "east": "First floor master bedroom", 
              "south": "First floor store room"},
                 
    "object_in_room": False,
           
    "search_object": {},

    "items": [],

    "enemy": [enemy3]
}    


room_store = {
    "name": "First floor store room",
                
    "description": """The room is the darkest that you have seen in the house. 
The light from your torch pierces it to reveal a store room that is cloaked
in cobwebs from many years of neglect. There are many boxes, some open but 
mostly closed and taped up. There are a few broken boards in one corner 
along with a large plank which upon closer inspection seems to be solid, 
maybe even strong enough to hold a significant weight. """,

    "exits": {"north": "First floor child's bedroom", 
              "east": "First floor bathroom"},
                 
    "object_in_room": False,
           
    "search_object": {},

    "items": [item_clue],

    "enemy": [enemy1]
}    


room_bathroom = { 
    "name": "First floor bathroom",
                
    "description": """The light from your torch illuminates the white tiles of 
this bathroom despite the obvious dirt that covers most of it. There is a 
deep empty bath against the back wall along with a sink above which is a 
cabinet. There are doors leading to the north and to the west.""",

    "exits": {"north": "First floor master bedroom", 
              "west": "First floor store room"},
                 
    "object_in_room": False,
           
    "search_object": {},

    "items": [],

    "enemy": [enemy2]
}    

room_master = { 
    "name": "First floor master bedroom",
                
    "description": """Walking into the room, it is quite obviously the master 
bedroom. There is a king sized bed against one wall along with a chest of 
drawers in one corner. A wardrobe is in another corner with a mirror on the
doors. Looking straight into the mirror you can see yourself and as you 
move closer a figure appears behind you. The closer you get the clearer the
face becomes until you realise that it is Kirill behind you. He smiles 
menacingly at you. You turn around sharply to find that no one is there. 
Looking back to the mirror Kirill once again smiles at you and waves as he 
turns away from the mirror and moves into the shadows. There are four doors
leading in each direction, north, south, east and west. """,

    "exits": {"north": "First floor north hallway", 
              "south": "First floor bathroom", 
              "west": "First floor child's bedroom", 
              "east": "First floor south hallway"},
              
    "object_in_room": False,
              
    "search_object": {},

    "items": [],

    "enemy": []
}    


room_porch = {
    "name": "Porch",
    
    "description": """As you look around you can clearly see a house in front of you.
It looks old, almost an antique in itself, climbing a floor above you and 
possibly an attic space above that. Looking around you see that there is no 
path leading away from the house, just east towards the porch. The door is made
of a wood that has seen better days but the handle gleams like the day it was 
installed. """,
    
    "exits": {"east": "Entrance"},
                
    "object_in_room": False,
            
    "search_object": {},

    "items": [],

    "enemy": []
}

rooms = {"Porch": room_porch,
         "Entrance": room_entrance,
         "Ground floor east hallway": room_hallway_g_e,
         "Ground floor west hallway": room_hallway_g_w,
         "Ground floor central hallway": room_hallway_g_c,
         "Ground floor west dining room": room_dining_w,
         "Ground floor east dining room": room_dining_e,
         "Ground floor kitchen": room_kitchen,
         "Ground floor office": room_office,
         "Ground floor east lounge": room_lounge_e,
         "Ground floor west lounge": room_lounge_w,
         "Basement storage": room_storage,
         "Pantry": room_pantry,
         "Torture room": room_torture,
         "Basement hallway": room_hallway_b,
         "Secret room": room_secret,
         "Workshop": room_workshop,
         "Wine Cellar": room_winecellar,
         "First floor south hallway": room_hallway_f_s,
         "First floor east hallway": room_hallway_f_e,
         "First floor north hallway": room_hallway_f_n,
         "First floor west hallway": room_hallway_f_w,
         "First floor child's bedroom": room_child,
         "First floor store room": room_store,
         "First floor bathroom": room_bathroom,
         "First floor master bedroom": room_master}

locked_exit_E_D = {
    "rooms": ["Entrance", "Ground floor west dining room"],
    
    "key_required": "bkey",
    
    "locked": True
}

locked_exit_E_L = {
    "rooms": ["Entrance", "Ground floor west lounge"],
    
    "key_required": "bkey",
    
    "locked": True
}

locked_exit_S_P = {
    "rooms": ["Basement storage", "Pantry"],
    
    "key_required": "rkey",
    
    "locked": True
}

locked_exit_S_W = {
    "rooms": ["Basement storage", "Wine Cellar"],
    
    "key_required": "rkey",
    
    "locked": True
}

locked_exit_S_H = {
    "rooms": ["Basement storage", "Basement hallway"],
    
    "key_required": "mkey",
    
    "locked": True
}

locked_exit_secret = {
    "rooms": ["Workshop", "Secret room"],
    
    "key_required": "clue",
    
    "locked": True
}

locked_exit_O_L = {
    "rooms": ["Ground floor office", "Ground floor east lounge"],
    
    "key_required": "rkey",
    
    "locked": True
} 

locked_exit_GEH_FSH = {
    "rooms": ["Ground floor east hallway", "First floor south hallway"],
    
    "key_required": "mkey",
    
    "locked": True
}

locked_exit_FSH_FMB = {
    "rooms": ["First floor master bedroom", "First floor south hallway"],
    
    "key_required": "bkey",
    
    "locked": True
}

locked_exit_FCB_FS = {
    "rooms": ["First floor child's bedroom", "First floor store room"],
    
    "key_required": "ckey",
    
    "locked": True
}

locked_exit_FB_FS = {
    "rooms": ["First floor bathroom", "First floor store room"],
    
    "key_required": "ckey",
    
    "locked": True
}

locked_exit_plank = {
    "rooms": ["Ground floor west hallway", "Entrance"],
    
    "key_required": "plank",
    
    "locked": False
}

locked_room_exits = {
    "Entrance_Dining_room": locked_exit_E_D,
    "Entrance_Lounge": locked_exit_E_L,
    "Storage_Pantry": locked_exit_S_P,
    "Storage_Wine_cellar": locked_exit_S_W,
    "Storage_Hallway": locked_exit_S_H,
    "Secret_Room": locked_exit_secret,
    "Office_Lounge": locked_exit_O_L,
    "Ground_Floor_First_Floor": locked_exit_GEH_FSH,
    "South_Hallway_Master_Bedroom": locked_exit_FSH_FMB,
    "Child_Room_Store": locked_exit_FCB_FS,
    "Bathroom_Store": locked_exit_FB_FS,
    "Hole_In_Floor": locked_exit_plank
}