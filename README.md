#Internal Tandum Duplicate Checker 
Program that reads a file containing a query and reference strand of DNA and checks for internal tandum duplications

#ITD.py

|Parameters|Description|
|----------|-----------|
|-f        |path to file|

First compares the two strands to see how well they match. If the match percentage is greater than 70%, the program continues.
If an ITD is found, the program will display it to stdout.

#Example
`python ITD.py -f Example.txt`
