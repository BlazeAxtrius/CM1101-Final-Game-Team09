# -*- coding: utf-8 -*- 
2 """ 
3 Created on Sun Oct 18 15:08:33 2015 
4  
5 @author: KHADIJA 
6 """ 
7 
 
8 
 
9 from items import * 
10 
 
11 
 
12 room_hallway_g_w = {  
13         "name": "hallway, G, W", 
14                  
15         "description": 
16         """Y........................................... 
17          
18          
19         .""", 
20 
 
21     "exits": {"north" : "dining room, G, W", "south": "lounge, G, W", "east": "hallway, G, C, W}, 
22 
 
23     "items": [] 
24 } 
25 
 
26 
 
27 
 
28 room_hallway_g_e = { 
29     "name": "hallway, G, E", 
30 
 
31     "description": 
32     """Y............................................... 
33  
34  
35     .""", 
36 
 
37     "exits": {"west": "hallway, G, C, E", "up": "hallway, F1, S", "down": "hallway, F-1"},  
38 
 
39     "items": [] 
40 }   
41 
 
42 
 
43 
 
44 room_hallway_g_c_w = { 
45     "name": "hallway, G, C, W", 
46 
 
47     "description":  
48     """Y............................................... 
49  
50  
51     .""", 
52 
 
53     "exits": {"west": "hallway, G, W", "north": "dining room, G, E", "south": "lounge, G, E"}, 
54 
 
55     "items": [] 
56 } 
57 
 
58 
 
59 
 
60 room_hallway_g_c_e = { 
61     "name": "hallway, G, C, E", 
62 
 
63     "description":  
64     """Y............................................... 
65  
66  
67     .""", 
68 
 
69     "exits": {"north": "kitchen", "south": "office, G", "east": "hallway, G, E"}, 
70 
 
71     "items": [] 
72 } 
73 
 
74              
75              
76 room_dining_w = {  
77         "name": "dining room, G, W", 
78                  
79         "description": 
80         """Y........................................... 
81          
82          
83         .""", 
84 
 
85     "exits": {"south" : "hallway, G, W", "east": "dining room, G, E"}, 
86 
 
87     "items": [] 
88 }     
89 
 
90 
 
91 
 
92 room_dining_e = { 
93     "name": "dining room, G, E", 
94 
 
95     "description": 
96     """Y............................................... 
97  
98  
99     .""", 
100 
 
101     "exits": {"west": "dining room, G, W", "east": "kitchen, G", "south": "hallway, G, C, W"}, 
102 
 
103     "items": [] 
104 } 
105 
 
106 
 
107   
108 room_kitchen = {  
109         "name": "kitchen,G", 
110                  
111         "description": 
112         """Y........................................... 
113          
114          
115         .""", 
116 
 
117     "exits": {"south" : "hallway, G, C, E", "west": "dining room, G, E"}, 
118 
 
119     "items": [] 
120 }      
121 
 
122 
 
123 room_offfice = {  
124         "name": "office,G", 
125                  
126         "description": 
127         """Y........................................... 
128          
129          
130         .""", 
131 
 
132     "exits": {"north" : "hallway, G, C, E", "west": "lounge, G, E"}, 
133 
 
134     "items": [] 
135 }   
136      
137 room_lounge_e = {  
138         "name": "lounge, G, E", 
139                  
140         "description": 
141         """Y........................................... 
142          
143          
144         .""", 
145 
 
146     "exits": {"north" : "hallway, G, C, W", "east": "office, G", "west": "lounge, G, W"}, 
147 
 
148     "items": [] 
149 }     
150 
 
151 
 
152 room_lounge_w = { 
153     "name": "lounge, G, W", 
154 
 
155     "description":  
156     """Y............................................... 
157  
158  
159     .""", 
160 
 
161     "exits": {"north": "hallway, G, W", "east": "lounge, G, E"},  
162 
 
163     "items": [] 
164 } 
165 
 
166 
 
167 
 
168 room_store = {  
169         "name": "store,F-1", 
170                  
171         "description": 
172         """Y........................................... 
173          
174          
175         .""", 
176 
 
177     "exits": {"north" : "pantry, F-1", "south": "wine cellar, F-1", "east": "hallway, F-1"}, 
178 
 
179     "items": [] 
180 }     
181 
 
182 room_pantry = {  
183         "name": "pantry,F-1", 
184                  
185         "description": 
186         """Y........................................... 
187          
188          
189         .""", 
190 
 
191     "exits": {"south" : "store, F-1", "east": "torture, F-1"}, 
192 
 
193     "items": [] 
194 }     
195 
 
196 room_torture = {  
197         "name": "torture,F-1", 
198                  
199         "description": 
200         """Y........................................... 
201          
202          
203         .""", 
204 
 
205     "exits": {"west" : "pantry, F-1", "south": "hallway, F-1"}, 
206 
 
207     "items": [] 
208 }     
209 
 
210 room_hallway_b = {  
211         "name": "hallway,F-1", 
212                  
213         "description": 
214         """Y........................................... 
215          
216          
217         .""", 
218 
 
219     "exits": {"north" : "torture, F-1", "south": "workshop, F-1", "west": "store, F-1", "up": "hallway, G, E"}, 
220 
 
221     "items": [] 
222 }     
223 
 
224 room_secret = {  
225         "name": "secret room,F-1", 
226                  
227         "description": 
228         """Y........................................... 
229          
230          
231         .""", 
232 
 
233     "exits": {"west" : "workshop, F-1"}, 
234 
 
235     "items": [] 
236 }     
237 
 
238 room_workshop = {  
239         "name": "workshop,F-1", 
240                  
241         "description": 
242         """Y........................................... 
243          
244          
245         .""", 
246 
 
247     "exits": {"west" : "wine cellar, F-1", "east": "secret, F-1", "north": "hallway, F-1"}, 
248 
 
249     "items": [] 
250 }     
251 
 
252 room_winecellar = {  
253         "name": "wine cellar,F-1", 
254                  
255         "description": 
256         """Y........................................... 
257          
258          
259         .""", 
260 
 
261     "exits": {"north" : "store, F-1", "east": "workshop, F-1"}, 
262 
 
263     "items": [] 
264 }     
265 
 
266 room_hallway_f_s = {  
267         "name": "hallway, F1, S", 
268                  
269         "description": 
270         """Y........................................... 
271          
272          
273         .""", 
274 
 
275     "exits": {"north" : "hallway, F1, E", "west": "master bedroom, F1", "down": "hallway, G, E" }, 
276 
 
277     "items": [] 
278 }     
279 
 
280 
 
281 room_hallway_f_e = { 
282     "name": "hallway, F1, E", 
283 
 
284     "description": 
285     """Y................................................ 
286  
287  
288     .""", 
289 
 
290     "exits": {"south": "hallway, F1, S", "west": "hallway, F1, N"}, 
291 
 
292     "items": [] 
293 } 
294 
 
295 
 
296 room_hallway_f_n = { 
297     "name": "hallway, F1, N", 
298 
 
299     "description": 
300     """Y................................................. 
301  
302  
303     .""", 
304 
 
305     "exits": {"west": "hallway, F1, W", "south": "master bedroom, F1", "east": "hallway, F1, E"}, 
306 
 
307     "items": [] 
308 } 
309 
 
310 
 
311 room_hallway_f_w = { 
312     "name": "hallway, F1, W", 
313 
 
314     "description":  
315     """Y.................................................. 
316  
317  
318     .""", 
319 
 
320     "exits": {"south": "child bedroom, F1", "east", "hallway, F1, N"}, 
321 
 
322     "items": [] 
323 } 
324 
 
325 
 
326 room_child = {  
327         "name": "child bedroom,F1", 
328                  
329         "description": 
330         """Y........................................... 
331          
332          
333         .""", 
334 
 
335     "exits": {"north" : "hallway, F1, W", "east", "master bedroom, F1", "south": "store, F1"}, 
336 
 
337     "items": [] 
338 }     
339 
 
340 
 
341 room_store = {  
342         "name": "store,F1", 
343                  
344         "description": 
345         """Y........................................... 
346          
347          
348         .""", 
349 
 
350     "exits": {"north" : "child bedroom, F1", "east": "bathroom, F1"}, 
351 
 
352     "items": [] 
353 }     
354 
 
355 
 
356 room_bathroom = {  
357         "name": "bathroom,F1", 
358                  
359         "description": 
360         """Y........................................... 
361          
362          
363         .""", 
364 
 
365     "exits": {"north" : "master bedroom, F1", "west": "store, F1"}, 
366 
 
367     "items": [] 
368 }     
369 
 
370 room_master = {  
371         "name": "master bedroom,F1", 
372                  
373         "description": 
374         """Y........................................... 
375          
376          
377         .""", 
378 
 
379     "exits": {"north" : "hallway, F1, N", "south": "bathroom, F1", "west": "child bedroom, F1", "east": "hallway, F1, S"}, 
380 
 
381     "items": [] 
382 }     
383 
 
384 
 
385 rooms = {  
386          
387        "hallway, G, W": room_hallway_g_w, 
388        "hallway, G, E": room_hallway_g_e, 
389        "hallway, G, C, W": room_hallway_g_c_w, 
390        "hallway, G, C, E": room_hallway_g_c_e, 
391        "dining room, G, W": room_dining_w, 
392        "dining room, G, E": room_dining_e, 
393        "kitchen,G": room_kitchen, 
394        "office,G": room_office, 
395        "lounge, G, E": room_lounge_e, 
396        "lounge, G, W": room_lounge_w, 
397        "store,F-1": room_store, 
398        "pantry,F-1": room_pantry, 
399        "torture,F-1": room_torture, 
400        "hallway,F-1": room_hallway, 
401        "secret room,F-1": room_secert, 
402        "workshop,F-1": room_workshop, 
403        "wine cellar,F-1": room_winecellar, 
404        "hallway, F1, S": room_hallway_f_s, 
405        "hallway, F1, E": room_hallway_f_e, 
406        "hallway, F1, N": room_hallway_f_n, 
407        "hallway, F1, W": room_hallway_f_w, 
408        "child bedroom,F1": room_child, 
409        "store,F1": room_store, 
410        "bathroom,F1": room_bathroom, 
411        "master bedroom,F1": room_master 
412  } 

