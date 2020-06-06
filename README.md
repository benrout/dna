# dna
A program that identifies a person based on their DNA using Short Tandem Repeats (STRs).

Example usage:
```
$ python dna.py databases/large.csv sequences/5.txt
Lavender
```

## Short Tandem Repeats (STRs)

An STR is a short sequence of DNA bases that tends to repeat consecutively numerous times at specific locations inside of a person’s DNA. The number of times any particular STR repeats varies a lot among individuals.

The probability that two people have the same number of repeats for a single STR is 5%. Using multiple STRs can improve the accuracy of DNA profiling. By analysing the occurence of 10 different STRs, the probability that two DNA samples match purely by chance is about 1 in 1 quadrillion (assuming all STRs are independent of each other).
