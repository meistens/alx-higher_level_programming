# Function to chec[ if a singli linked list is looping

## Approach
Use a two-pointer approach (thanks leetcode!)

Basically, two pointers are defined - fast_ptr and slow_ptr. Fast_ptr is moved\
 down the loop to the next 2 pointer, slow_ptr goes on at its own pace.

A condition (while statement fits) is written to define what happens when\
fast_ptr, slow_ptr and the node of the next fast_ptr (fast_ptr is moved twice)\
 are true;
 - move fast_ptr 2 nodes up
 - slow_ptr moves at normal pace

A condition is written to handle what happend if both pointers meet/match\
 (returns 1 to signify loop matches). Close the brace of the conditon, return 0\
 to end loop and call it a day.
 