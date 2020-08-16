(define (problem prob)
 (:domain puzzle)
 (:objects n1 n2 n3 n4 n5 n6 n7 n8 - num l1 l2 l3 l4 l5 l6 l7 l8 l9 - loc)
 (:init (empty l6)(at n1 l1)(at n2 l2)(at n3 l3)(at n7 l4)(at n8 l5)
        (at n6 l7)(at n4 l8)(at n5 l9)(near l1 l2)(near l1 l4)(near l2 l1)
        (near l2 l3)(near l2 l5)(near l3 l2)(near l3 l6)(near l4 l1)
        (near l4 l5)(near l4 l7)(near l5 l4)(near l5 l2)(near l5 l8)
        (near l5 l6)(near l6 l5)(near l6 l3)(near l6 l9)(near l7 l4)
        (near l7 l8)(near l8 l7)(near l8 l5)(near l8 l9)(near l9 l8)
        (near l9 l6))
 (:goal ( and (at n1 l1)(at n2 l2)(at n3 l3)(at n4 l4)
              (at n5 l5)(at n6 l6)(at n7 l7)(at n8 l8)) )
)

            |            |    E       |
            |    F       |    F       |    F
A           |    A       |    A       |    A
B   E       |    B   E   |    B       |    B
C   D   F   |    C   D   |    C   D   |    C   D   E



A               |                   |
B               |   B           A   |           B   A
C   D   E   F   |   C   D   E   F   |   C   D   E   F   



                |   F           |   F           |   F   E
A       B       |   A       B   |   A   B       |   A   B
C   D   E   F   |   C   D   E   |   C   D   E   |   C   D




cores:      8           16      32          64
elapsed:   104757   51068.8     26117.6     13613.2
            128         256         512
           8629.28     7848.1    11254.5


n = 8192    res = 22042.6                                                                                                
cores:      1           2               4               8               16              32              64
elapsed     1.12812ms   0.794842ms      0.159442ms      0.205739ms      1.10202ms       1.21004ms       125.975ms



n = 32768:  res = 22033.1
cores:      1           2               4               8               16              32              64
elapsed     2.201ms     1.50676ms       1.16636ms       0.980213ms      1.44338ms       2.16186ms       113.489ms


n = 32768:  res = 22033.1
cores:      1           2               4               8               16              32              64
elapsed     2.201ms     1.50676ms       1.16636ms       0.980213ms      1.44338ms       2.16186ms       113.489ms





<<<<<<<<<<<<<
point to point
n = 4096:   res = 22055.4
cores:      1           2               4               8               16              32              64
elapsed     0.823469    0.776083ms      0.747984ms      0.893934ms      0.913741ms      1.30085ms       128.121ms
---------------------

<<<<<<<<
n = 16384:  res = 22036.3
cores:      1           2               4               8               16              32              64
elapsed     1.43843ms   1.12172ms       1.34236ms       1.15174ms       1.07895ms       1.14479ms       124.432ms
-------

<<<<<<<<
n = 262144:  res = 22030.3
cores:      1           2               4               8               16              32              64
elapsed     15.8693ms   8.30205ms       4.55824ms       2.4704ms        1.99807ms       0.707826ms      122.273ms
-------


<<<<<<<<
n = 67108864:  res = 22029.9
cores:      1           2               4               8               16              32              64
elapsed     1688.17ms   975.115ms       533.17ms        302.508ms       177.892ms       135.56ms        610.763ms
-------

n = 4194304
cores:      1           2               4               8               16              32              64
elapsed     
-------


<<<<<<<<
n = 1073741824: res = 22029.9
cores:      1           2               4               8               16              32              64
elapsed     22671ms     11482.5ms       5885.25ms       3114.86ms       1712.18ms       1048.06ms       613.911ms
-------


n = 2147483647 res = 22029.9
cores:      1           2               4               8               16              32              64
elapsed                 23704.4ms       11452.5ms       6012.49ms       3106.97ms       1800.46ms       1078.06ms
-------









++++++++++
REDUCE
n = 4096:   res = 22055.1
cores:      1           2               4               8               16              32              64
elapsed     0.799612ms  0.776437ms      0.764292ms      0.796369ms      0.993905ms      1.18951ms       1.34684ms
---------------------

<<<<<<<<
n = 16384:  res = 22036.3
cores:      1           2               4               8               16              32              64
elapsed     1.418ms     1.0772ms        0.929058ms      0.856655ms      1.12957ms       1.22453ms       3.48978ms
-------


<<<<<<<<
n = 262144:  res = 22030.3
cores:      1           2               4               8               16              32              64
elapsed     13.3681ms   8.37699ms       4.61821ms       2.74311ms       1.99807ms       1.65998ms       4.39467ms
-------


<<<<<<<<
n = 67108864:  res = 22029.9
cores:      1           2               4               8               16              32              64
elapsed     1681.09ms   977.724ms       523.26ms        298.573ms       204.15ms        116.322ms       87.7305ms
-------


<<<<<<<<
n = 1073741824: res = 22029.9
cores:      1           2               4               8               16              32              64
elapsed     22613.5ms   11747.5ms       5872.45ms       3153.26ms       1743.75ms       1041.52ms       607.758ms
-------


n = 2147483647 res = 22029.9
cores:      1           2               4               8               16              32              64
elapsed                 22029.9         11505.6ms       5951.08ms       3159.09ms       1821.54ms       1084.84ms
-------

<span class="time" id="news-time" data-val="1571622654000">2019-10-21 09:50</span>

<meta name="apub:time" content="2019-10-21 08:13:45">
