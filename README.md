# py-prime-algorithms
This file contains a short summary of the project. 

## background
This project was created for the first technical paper of the author. It was written on the topic "Theoretical and practical differences between different prime number sieves". It covers how and why the sieves function and some experiments were carried out with the sieves. 

## file summaries 
- 100_mil_checked.txt contains all primes<100 million

- README.md is this file

- atkin.py contains the sieve of atkin which searches for all primes p<n
    - input: n
    - output: formatted array [number, isPrime, time], runtime, performed Checks

- check_primes.py compares primes in file (in new format) to primes in 100_mil_checked.txt and prints results
    - input: filename (should contain path to file) 

- check_primes_legacy.py compares primes in file (in old format) to primes in 100_mil_checked.txt and prints results
    - input: filename (should contain path to file)

- eratosthenes.py contains sieve of eratosthenes which searches for all primes p<n
    - input: n
    - output: formatted array [number, isPrime, time], runtime, performed Checks

- execute.bat executes main.py with

- main.py takes an input n, executes all sieves with input n and prints the formatted arrays to files

- multi-execute.bat takes an input n, executes main.py four times with input n (those executions are performed after one another)

- sundaram.py contains sieve of sundaram which searches for all primes p<n
    - input: n
    - output: formatted array [number, isPrime, time], runtime, performed Checks