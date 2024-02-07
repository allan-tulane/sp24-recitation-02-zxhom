# CMPS 2200  Recitation 02

**Name (Team Member 1):** Zach Hom  
**Name (Team Member 2):** Disha Amin

In this recitation, we will investigate recurrences. 
To complete this recitation, follow the instructions in this document. Some of your answers will go in this file, and others will require you to edit `main.py`.



## Running and testing your code
- To run tests, from the command-line shell, you can run
  + `pytest test_main.py` will run all tests
  + `pytest test_main.py::test_one` will just run `test_one`
  + We recommend running one test at a time as you are debugging.

## Turning in your work

- Once complete, click on the "Git" icon in the left pane on repl.it.
- Enter a commit message in the "what did you change?" text box
- Click "commit and push." This will push your code to your github repository.
- Although you are working as a team, please have each team member submit the same code to their repository. One person can copy the code to their repl.it and submit it from there.

## Recurrences

In class, we've started looking at recurrences and how to we can establish asymptotic bounds on their values as a function of $n$. In this lab, we'll write some code to generate recursion trees (via a recursive function) for certain kinds of recurrences. By summing up nodes in the recurrence tree (that represent contributions to the recurrence) we can compare their total cost against the corresponding asymptotic bounds. We'll focus on  recurrences of the form:

$$ W(n) = aW(n/b) + f(n) $$

where $W(1) = 1$.

- [ ] 1. (2 point) In `main.py`, you have stub code which includes a function `simple_work_calc`. Implement this function to return the value of $W(n)$ for arbitrary values of $a$ and $b$ with $f(n)=n$.

- [ ] 2. (2 point) Test that your function is correct by calling from the command-line `pytest test_main.py::test_simple_work` by completing the test cases and adding 3 additional ones.

- [ ] 3. (2 point) Now implement `work_calc`, which generalizes the above so that we can now input $a$, $b$ and a *function* $f(n)$ as arguments. Test this code by completing the test cases in `test_work` and adding 3 more cases.

- [ ] 4. (2 point) Now, derive the asymptotic behavior of $W(n)$ using $f(n) = 1$, $f(n) = \log n$ and $f(n) = n$. Then, generate actual values for $W(n)$ for your code and confirm that the trends match your derivations.

**TODO: your answer goes here**
Asymptotic behavior:
f(n)=1 --> W(n) = O(n)
f(n)=logn --> W(n) = O(nlog(n) 
f(n)=n --> W(n) = O(nlog(n)) 
|     n |   W_1 |    W_2 |
|-------|-------|--------|
|    10 |    15 |     36 |
|    20 |    31 |     92 |
|    50 |    63 |    276 |
|   100 |   127 |    652 |
|  1000 |  1023 |   9120 |
|  5000 |  8191 |  61728 |
| 10000 | 16383 | 133456 |
|     n |   W_1 |       W_2 |
|-------|-------|-----------|
|    10 |    15 |    16.294 |
|    20 |    31 |    35.584 |
|    50 |    63 |    84.201 |
|   100 |   127 |   173.008 |
|  1000 |  1023 |  1471.608 |
|  5000 |  8191 |  9919.326 |
| 10000 | 16383 | 19847.862 |

W_1 in both tables are the outputs for f(n) = 1
W_2 in the first table is f(n) = n
W_2 in the second table is f(n) = log(n)

- [ ] 5. (4 points) Now that you have a nice way to empirically generate valuess of $W(n)$, we can look at the relationship between $a$, $b$, and $f(n)$. Suppose that $f(n) = n^c$. What is the asypmptotic behavior of $W(n)$ if $c < \log_b a$? What about $c > \log_b a$? And if they are equal? Modify `test_compare_work` to compare empirical values for different work functions (at several different values of $n$) to justify your answer.

**TODO: your answer goes here**
If c < log_b(a) where b=2 and a=4, then c < 2. The work of linear functions, f(n)=n^1, are asymptotically bounded by O(nlog(n)) as seen above in question 4. (Leaf dominated)

If c > log_b(a) where b=2 and a=4, then c > 2. The work of quadratic functions, such as f=n^3, are asymptotically bounded by O(n^3) as seen below. (Root dominated)

If they are equal where b=2 and a=4, then c = 2. The work of f=n^2 is bounded by O(n^2) as seen below. (Balanced)

|     n |     W(f(n^3)) |   W(f(n^2))|
|-------|---------------|------------|
|    10 |          1692 |        328 |
|    20 |         14768 |       1712 |
|    50 |        236908 |      12936 |
|   100 |       1947632 |      61744 |
|  1000 |    1987993280 |    8544512 |
|  5000 |  249711292352 |  294904064 |
| 10000 | 1998845169408 | 1279616256 |


- [ ] 6. (3 points) $W(n)$ is meant to represent the running time of some recursive algorithm. Suppose we always had $a$ processors available to us and we wanted to compute the span of the same algorithm. Implement the function `span_calc` to compute the empirical span, where the work of the algorithm is given by $W(n)$. Implement `test_compare_span` to create a new comparison function for comparing span functions. Derive the asymptotic expressions for the span of the recurrences you used in problem 4 above. Confirm that everything matches up as it should. 

**TODO: your answer goes here**
Asymptotic Expressions:
f(n) = 1 --> W(n) = O(1)
f(n) = n --> W(n) = O(n)
f(n) = log(n) --> W(n) = O(n^(1/2))

     n |   W_1 |   W_2 |
|-------|-------|-------|
|    10 |     4 |    18 |
|    20 |     5 |    38 |
|    50 |     6 |    97 |
|   100 |     7 |   197 |
|  1000 |    10 |  1994 |
|  5000 |    13 |  9995 |
| 10000 |    14 | 19995 |
     n |   W_1 |    W_2 |
|-------|-------|--------|
|    10 |     4 |  5.605 |
|    20 |     5 |  8.601 |
|    50 |     6 | 13.506 |
|   100 |     7 | 18.111 |
|  1000 |    10 | 37.786 |
|  5000 |    13 | 56.944 |
W_1 in both tables are the outputs for f(n) = 1
W_2 in the first table is f(n) = n
W_2 in the second table is f(n) = log(n)
