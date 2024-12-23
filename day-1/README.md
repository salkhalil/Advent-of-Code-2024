# Day 1 Solution

[Link to problem](https://adventofcode.com/2024/day/1)

## Part 1

### Steps required

- Sort left and right lists
  - As we need to be comparing the lowest value in the left list compared to the right list to the right list, we'll have to sort them
- Calculate difference
  - Given two numbers, we want to find the difference between them
  - To avoid negative numbers, we'll take the absolute value of these inputs
- Sum differences
  - Once we have the list of differences we'll sum it to get the score

### Implementation log

- I'm going to start doing this using pandas as it has some neat APIs for some of the tasks I have to do here
  - `sort_values` for sorting, `sum` etc
- To do the difference operation efficiently I'll vectorise the function using `np.vectorize`
- In order to read this into a df I'll edit the input file so that it can be a csv
  - Added a row at the top for the the headings: left and right
  - Used a regex substitution in vim to replace triple space `\s{3}` with a comma
- After loading in the df, I'll get the sorted left and right lists as pandas `Series` objects
- I'll then call the vectorised absolute difference function to get the list of results
- Sum the results, bob's my uncle

## Part 2

### Steps required

- Calculate value counts in right list
- Calculate multipliers
  - Iterate over the left list, find counts in right list
- Calculate scores
  - Multiply values in left list by multipliers
- Sum scores to get final answer

### Implementation log

- Pandas makes this too easy, can grab the value counts using the `value_counts` api
- In my multipliers function, will use a try/except to return 0 if it's not in the list
- Use pandas syntactic sugar to calculate scores and sum
