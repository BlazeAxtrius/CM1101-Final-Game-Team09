# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 15:08:33 2015

@author: KHADIJA
"""


from items import *
room_entrance = { 
    "name": "entrance",
                
    "description":"""As you close the door behind you it booms with a huge 
weight. The hallway that lies in front of you to the east is sparsely 
decorated other than a carpet leading down the room and a grandfather clock
to your right. Upon listening the clock seems to be broken.""",

    "exits": {"north" : "dining room, G, W", "south": "lounge, G, W", "east": "hallway, G, W", "west": "porch"},

    "has_plank": "False",
    
    "items": []
}


room_hallway_g_e = {
    "name": "hallway, G, E",

    "description":"""As you leave the stairs you can see a door to the south 
and the stairs to the basement to the north. There is a small table against
the wall and on it you can see a torch. The hallway continues to the 
west.""",

    "exits": {"west": "hallway, G, C", "up": "hallway, F1, S", "down": "hallway, F-1"}, 

    "items": []
}  



room_hallway_g_w = {
    "name": "hallway, G, W",

    "description": """The stacked wood lies to one side of you, blocking your 
path towards the stairs. The hole that you created is to the other side 
like a gaping maw reminding you of the fall. You look for a way around it 
but the wood has broken nearly all the way around. You doubt whether the 
remaining floorboards would support any weight on them at all and decide 
not to find out. """,


    "exits": {"west": "entrance", "north": "dining room, G, E", "south": "lounge, G, E"},


    "items": []
}



room_hallway_g_c = {
    "name": "hallway, G, C",

    "description": """You can see that there is a pile of what appears to be 
wood in front of you, blocking your path back towards the front door. It 
is impossible to get through or around as it is stacked to the ceiling. 
There are doors to the north and south and the stairway to the east.""",

    "exits": {"north": "kitchen, G", "south": "office, G", "east": "hallway, G, E"},

    "items": []
}

            
            
room_dining_w = { 
    "name": "dining room, G, W",
                
    "description": """There is a glass cabinet in the corner of the room with 
what looks like some exotic plates and drawers underneath that. This end of
the table has a very large chair placed at it, as though it was saved for 
someone important. There is a door to the south and the room continues to 
the east.""",

    "exits": {"south" : "entrance", "east": "dining room, G, E"},

    "items": []
}    



room_dining_e = {
    "name": "dining room, G, E",

    "description": """In the room you can see a large dining table sitting 
below a grand chandelier. Both have seen better days but seem to be sturdy.
There is a cabinet in the corner of the room and the room continues to the 
west. There is also a door to the south. """,

    "exits": {"west": "dining room, G, W", "east": "kitchen, G", "south": "hallway, G, W"},

    "items": []
}


 
room_kitchen = { 
    "name": "kitchen, G",
                
    "description": """You enter what appears to be a kitchen. You can see an 
oven with a hob in one corner, next to that a sink and a worktop along the 
wall. There are several shelves and cupboards that seem to be broken and 
empty. You can see a rack of cutlery including some larger knives used for 
chopping food. There is a door to the west and to the south.""",

    "exits": {"south" : "hallway, G, C", "west": "dining room, G, E"},

    "items": []
}     



room_office = { 
    "name": "office, G",
                
    "description": """As you enter the room you can see a large desk in front 
of you along with a thick leather chair. Behind that there are two large 
bookcases in the corners of the rooms filled with books that are dusted but
look as though they are expensive. """,

    "exits": {"north" : "hallway, G, C", "west": "lounge, G, E"},

    "items": []
}  
    
room_lounge_e = { 
    "name": "lounge, G, E",
                
    "description": """You can immediately see that this is the lounge. There 
are sofas and armchairs in the centre of the room. To against the wall to 
the south there is a large fireplace although it looks unused for some time
now. There is a door to the north as well as the east and the room 
continues to the west.""",

    "exits": {"north" : "hallway, G, W", "east": "office, G", "west": "lounge, G, W"},

    "items": []
}    


room_lounge_w = {
    "name": "lounge, G, W",

    "description": """There is more furniture here, in particular two armchairs
arranged next to a small table, seemingly to encourage conversation. There 
is also a cupboard to in the corner of the room with the doors slightly 
open. There is a door to the north and the room continues to the east.""",

    "exits": {"north": "entrance", "east": "lounge, G, E"}, 

    "items": []
}



room_storage = { 

    "name": "storage, F-1",
                
    "description": """As you pull yourself to your feet once more you can't 
help be thankful for the carpet breaking your fall somewhat. As you fumble 
around in the darkness you realise that you are in a small storage 
cupboard. You can just about make out a rusted oil lamp on a shelf along 
with a match box. You tread carefully avoiding the large pieces of wood 
that have splintered as a result of the fall. You also notice a small 
cupboard in the corner when noises that emanate from it startle you.""",

    "exits": {"north" : "pantry, F-1", "south": "wine cellar, F-1", "east": "hallway, F-1"},

    "items": []
}    

room_pantry = { 

    "name": "pantry, F-1",
                
    "description": """As you open the door the smell of rotten food hits you 
like a brick wall of gas. Whatever was once in here would appear to be 
inedible now. You can see shelves stacked with some cheeses that have been 
gnawed at by what you would assume were rats along with some other food 
which is too old to distinguish between. You wonder just how long some of 
this has been here. You can see a door to the east and the door that you 
entered the room with.""",

    "exits": {"south" : "storage, F-1", "east": "torture, F-1"},

    "items": []
}    

room_torture = { 
    "name": "torture, F-1",
                
    "description": """As you enter the room, the light glimmers off some metal 
on the walls. When you look closer, you can see that they are chains and 
shackles bolted to the wall. There are what appear to be instruments that 
were used to inflict pain covered in congealed blood along with a large red
stain on the floor. You don't want to be in this room for any longer than 
you have to. A door leads to the south and back from where you came.""",

    "exits": {"west" : "pantry, F-1", "south": "hallway, F-1"},

    "items": []
}    

room_hallway_b = { 
    "name": "hallway, F-1",
                
    "description": """The hallway is dingy and very dark. You can see a few 
cobwebs hanging from the corners of the room and the floor is covered in 
dust and dirt. You can't see much more than this. There are doors leading 
to the north and south and a staircase to the east.""",

    "exits": {"north" : "torture, F-1", "south": "workshop, F-1", "west": "storage, F-1", "up": "hallway, G, E"},

    "items": []
}    

room_secret = { 
    "name": "secret room, F-1",
                
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

    "exits": {"west" : "workshop, F-1"},

    "items": []
}    

room_workshop = { 
    "name": "workshop, F-1",
                
    "description": """Upon entering the room you can see a large wooden table 
in the middle of the room. As you look closer you can see a few vices on 
the sides of the table along with some files and blunt chisels that would 
be used for crafting. An old shelf with some dusty equipment and a few 
books is to the east of the room. A door leads to the north of the room and
another from where you came. """,

    "exits": {"west" : "wine cellar, F-1", "east": "secret room, F-1", "north": "hallway, F-1"},

    "items": []
}    

room_winecellar = { 
    "name": "wine cellar, F-1",
                
    "description": """As you enter the room, the large number of wine racks is 
immediately visible. There are a few empty spaces but most are filled with 
bottles that have so much dust on them that the labels can't be read. You 
can also see a door to the east and another from where you came.""",

    "exits": {"north" : "storage, F-1", "east": "workshop, F-1"},

    "items": []
}    

room_hallway_f_s = { 
    "name": "hallway, F1, S",
                
    "description": """As you come up the stairs you can see a long dark 
corridor leading to the north along with a door to the west. The stairs to 
the south lead back downstairs. It is difficult to see much else. """,

    "exits": {"north" : "hallway, F1, E", "west": "master bedroom, F1", "down": "hallway, G, E" },

    "items": []
}    


room_hallway_f_e = {
    "name": "hallway, F1, E",

    "description": """As you reach the corner you can see the corridor leads 
west as well as south. There is a small round table in the corner with a 
lamp on top of it.""",

    "exits": {"south": "hallway, F1, S", "west": "hallway, F1, N"},

    "items": []
}


room_hallway_f_n = {
    "name": "hallway, F1, N",

    "description": """As you move down the corridor you can see a door to the 
south. The corridor continues to the west and to the east.""",

    "exits": {"west": "hallway, F1, W", "south": "master bedroom, F1", "east": "hallway, F1, E"},

    "items": []
}


room_hallway_f_w = {
    "name": "hallway, F1, W",

    "description": """Reaching the end of the corridor there is a door to the 
south and the corridor goes back to the east.""",

    "exits": {"south": "child bedroom, F1", "east": "hallway, F1, N"},

    "items": []
}


room_child = { 
    "name": "child bedroom, F1",
                
    "description": """You realise this is a child's bedroom by the colourful
décor. There is a small cot that looks broken along with a single bed 
against one wall. There is a trunk at the foot of the bed overflowing with 
toys and soft toy animals in another corner; their glass eyes reflecting 
the light of your torch giving them a sinister look. The moonlight shining 
through the dirty window casts long shadows over parts of the room adding 
to the atmosphere of the unknown. There are doors leading to the north, 
east and south""",

    "exits": {"north" : "hallway, F1, W", "east": "master bedroom, F1", "south": "store, F1"},

    "items": []
}    


room_store ={
    "name": "store, F1",
                
    "description": """The room is the darkest that you have seen in the house. 
The light form your torch pierces it to reveal a store room that is cloaked
in cobwebs from many years of neglect. There are many boxes, some open but 
mostly closed and taped up. There are a few broken boards in one corner 
along with a large plank which upon closer inspection seems to be solid, 
maybe even strong enough to hold a significant weight. """,

    "exits": {"north" : "child bedroom, F1", "east": "bathroom, F1"},

    "items": []
}    


room_bathroom = { 
    "name": "bathroom, F1",
                
    "description": """The light from your torch illuminates the white tiles of 
this bathroom despite the obvious dirt that covers most of it. There is a 
deep empty bath against the back wall along with a sink above which is a 
cabinet. There are doors leading to the north and to the west.""",

    "exits": {"north" : "master bedroom, F1", "west": "store, F1"},

    "items": []
}    

room_master = { 
    "name": "master bedroom, F1",
                
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

    "exits": {"north" : "hallway, F1, N", "south": "bathroom, F1", "west": "child bedroom, F1", "east": "hallway, F1, S"},

    "items": []
}    


room_porch = {
    "name": "porch",
    
    "description": """When you are standing in front of the house you can see a 
huge and magnificent structure attached to the exterior of a house which form 
a covered entrance and the structure will lead you to the east. """,
    
    "exits": {"east": "entrance"},

    "items": []
}

rooms = {
       "porch": room_porch,
       "entrance": room_entrance,
       "hallway, G, E": room_hallway_g_e,
       "hallway, G, W": room_hallway_g_w,
       "hallway, G, C": room_hallway_g_c,
       "dining room, G, W": room_dining_w,
       "dining room, G, E": room_dining_e,
       "kitchen, G": room_kitchen,
       "office, G": room_office,
       "lounge, G, E": room_lounge_e,
       "lounge, G, W": room_lounge_w,
       "storage, F-1": room_storage,
       "pantry, F-1": room_pantry,
       "torture, F-1": room_torture,
       "hallway, F-1": room_hallway_b,
       "secret room, F-1": room_secret,
       "workshop, F-1": room_workshop,
       "wine cellar, F-1": room_winecellar,
       "hallway, F1, S": room_hallway_f_s,
       "hallway, F1, E": room_hallway_f_e,
       "hallway, F1, N": room_hallway_f_n,
       "hallway, F1, W": room_hallway_f_w,
       "child bedroom, F1": room_child,
       "store, F1": room_store,
       "bathroom, F1": room_bathroom,
       "master bedroom, F1": room_master
 }

