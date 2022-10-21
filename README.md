# Operational-Research-project
Two optimization problems in which we are looking for the minimum time using gurobi optimization in python


# The first problem:
A factory, among the various colors and related products it produces,
also produces five different special color shades (named: 1, 2, 3, 4 and 5) for
its large customers, for which demand is stable. Each such special shade arises
by a specific mixing machine which should be cleaned before its production
next (different) shade. The mixing process for each shade from 1 to 5
lasts 40, 35, 45, 32 and 50 minutes, respectively. The cleaning times of the above machine
they depend on both the type and the shade of the colors. For example, a color
that is based on oil requires more cleaning time than a paint that is based on it
water. Something similar happens when after a shade of dark color it should be produced
a shade of white. The cleaning time of the machine (in minutes) required so that the
machine to produce shade j given that the immediately preceding shade i was given
from element (i, j) of the table below.

|  | 1 | 2 | 3 | 4 | 5 |
| --- | --- | --- | --- | --- | --- |
|  1 | 0 | 11 | 7 | 13 | 11 |
|  2 | 5 | 0 | 13 | 15 | 15 |
|  3 | 13 | 15 | 0 | 23 | 11 |
|  4 | 9 | 13 | 5 | 0 | 3 |
|  5 | 3 | 7 | 7 | 7 | 0 |

Because the factory has other production activities, its management wants the weekly production of the five special shades to be done in the shortest possible time (mixing and cleanings).
Which production line of shades best serves the above desire of the administration? 
The series will repeat every week, so the cleaning time in between
last production of one week and first production of the next
weeks should be counted towards the total cleaning time of the machine


# The second problem:

A factory has also undertaken the coloring of three wallpapers with the codes
designations: T1, T2 and T3. T1 has a blue background and yellow patterns, T2 has green
background and blue and yellow patterns and T3 has a yellow background and blue and green patterns. For
achieving the above colorings, the factory has three different machines that each
one can color with only one of the above colors (green, blue or yellow). Τ1
to be produced the blue background must first be created and then created
the yellow drawings. T2 to be produced must first create the green background, at
then to create the blue designs and finally to create the yellow designs. T3
to produce the yellow background must first be created, then they will be created
the blue designs and finally to create the green designs.
The application time of each color for the production of each type of wallpaper differs based on
of the material of the surfaces to be painted. Specifically, this time (in minutes) is given
in the table below.

|  Machine | Color | T1  | T2  | T3  |
| ---      | ---   | --- | --- | --- |
|  1       | Blue  | 45  | 20  | 12  |
|  2       | Green |     | 10  | 17  |
|  3       | Yellow| 10  | 34  | 28  |

Knowing that each machine can process one wallpaper at a time and that each
wallpaper cannot be processed in parallel by different machines, 
the management asks you to find that schedule that will complete the production of all three types
wallpaper in the shortest possible time.
