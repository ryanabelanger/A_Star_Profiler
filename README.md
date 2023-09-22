# A* Profiler
## Description
 This is a tool I wrote to help iterate on my A* implementation for another project. 
 
 The problem I was trying to solve was finding a balance between map size (a simple cartesian grid) and the time it took to find a path to a randomly selected location within the grid.
 
## Usage
 Modifying the w_range and h_range lists with integers will change the size of the map being 
 searched. The map object will produce a list of x,y coordinate tuples and pick a random point 
 as the 'exit' or 'hatch'.
 
 The map will then subdivide the map into chunks based on the subsection_size variable. The 
 script then produces a list of random starting points for each map created based on the sample 
 size variable.
 
 The A* algorithm is used to navigate the subdivided map from the starting point to the exit.
 A new map is created using those subdivisions, then the A* algorithm is run again to produce the
 final path from the starting point to the hatch. It returns a dictionary for 'Method' (m), path length (p),
 and time taken to calculate the path (t).
 
 Finally, all of these dictionaries are collected into one larger dictionary and printed to the console.
 
## Notes
 Currently all m values are 2 (the default A* algorithm). Method 1 is the un-sectioned A* algorithm which can take
 hours to traverse a sufficiently large map. Creating a map > 2500x2500 takes a long time to build and traverse. A
 second subdivided map is created, but not implemented in a 3rd method because of this time-to-build constraint.
 
## Example Output
Sample Size: 5
Subsection Size: 10
```
Map created for 100x100, 10000 squares
Map created for 150x150, 22500 squares
Map created for 250x250, 62500 squares
Map created for 400x400, 160000 squares
Map created for 500x500, 250000 squares
Map created for 1000x1000, 1000000 squares
Map created for 2000x2000, 4000000 squares
Map created for 2500x2500, 6250000 squares
Created 8 maps
{'Map_10000': {'(15, 24)': {'m': 2, 'p': 76, 't': 0.01136},
               '(47, 26)': {'m': 2, 'p': 58, 't': 0.00202},
               '(67, 22)': {'m': 2, 'p': 82, 't': 0.00309},
               '(69, 9)': {'m': 2, 'p': 97, 't': 0.00458},
               '(98, 80)': {'m': 2, 'p': 65, 't': 0.0021}},
 'Map_1000000': {'(156, 727)': {'m': 2, 'p': 221, 't': 0.02127},
                 '(441, 309)': {'m': 2, 'p': 678, 't': 0.17338},
                 '(545, 535)': {'m': 2, 'p': 556, 't': 0.11459},
                 '(663, 568)': {'m': 2, 'p': 641, 't': 0.15322},
                 '(691, 887)': {'m': 2, 'p': 916, 't': 0.29794}},
 'Map_160000': {'(110, 210)': {'m': 2, 'p': 109, 't': 0.00592},
                '(112, 224)': {'m': 2, 'p': 125, 't': 0.00737},
                '(14, 214)': {'m': 2, 'p': 17, 't': 0.00062},
                '(267, 326)': {'m': 2, 'p': 382, 't': 0.05474},
                '(343, 111)': {'m': 2, 'p': 419, 't': 0.06592}},
 'Map_22500': {'(108, 127)': {'m': 2, 'p': 156, 't': 0.00944},
               '(116, 5)': {'m': 2, 'p': 108, 't': 0.0049},
               '(142, 99)': {'m': 2, 'p': 162, 't': 0.01074},
               '(25, 16)': {'m': 2, 'p': 40, 't': 0.00475},
               '(67, 95)': {'m': 2, 'p': 83, 't': 0.00288}},
 'Map_250000': {'(12, 150)': {'m': 2, 'p': 371, 't': 0.06076},
                '(272, 61)': {'m': 2, 'p': 118, 't': 0.03934},
                '(364, 132)': {'m': 2, 'p': 47, 't': 0.0017},
                '(426, 216)': {'m': 2, 'p': 193, 't': 0.01556},
                '(60, 299)': {'m': 2, 'p': 472, 't': 0.19406}},
 'Map_4000000': {'(1565, 1264)': {'m': 2, 'p': 1349, 't': 0.68043},
                 '(237, 685)': {'m': 2, 'p': 1888, 't': 6.82388},
                 '(321, 1712)': {'m': 2, 'p': 777, 't': 1.5605},
                 '(831, 1597)': {'m': 2, 'p': 382, 't': 0.4611},
                 '(92, 738)': {'m': 2, 'p': 1980, 't': 10.22951}},
 'Map_62500': {'(146, 45)': {'m': 2, 'p': 181, 't': 0.05082},
               '(153, 136)': {'m': 2, 'p': 83, 't': 0.01516},
               '(157, 193)': {'m': 2, 'p': 40, 't': 0.00407},
               '(45, 139)': {'m': 2, 'p': 188, 't': 0.0591},
               '(81, 175)': {'m': 2, 'p': 116, 't': 0.02216}},
 'Map_6250000': {'(1009, 1010)': {'m': 2, 'p': 1545, 't': 0.92072},
                 '(1018, 2)': {'m': 2, 'p': 2562, 't': 2.48346},
                 '(1988, 727)': {'m': 2, 'p': 2807, 't': 2.99873},
                 '(1994, 1723)': {'m': 2, 'p': 1817, 't': 1.25451},
                 '(858, 413)': {'m': 2, 'p': 1991, 't': 1.50878}}}`
```
