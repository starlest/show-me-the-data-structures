
# Walkthrough
Both functions use Python sets to efficiently perform union and intersection operations while automatically handling duplicate elements. The results are then converted back into linked lists for the final output.

# Efficiency

*m* and *n* are the lengths of the input linked lists.

## Time Efficiency
1. `union`: O(m + n). The function iterates through each list once to create sets representing the elements of the lists, and then iterates through the set resulting from the union operation to create the resulting linked list.
2. `intersection`: O(m + n). Similar to the union function, the intersection function iterates through each list once to create sets representing the elements of the lists, and then iterates through the set resulting from the intersection operation to create the resulting linked list.

Thus the overall time complexity for worst case scenario is O(m + n).

## Space Efficiency
1. `union`: O(m + n), as the function creates a new set to store the unique elements from both lists and a new linked list to store the result of the union.
2. `intersection`: O(m + n), as the function creates two new sets to store the unique elements from each list and a new linked list to store the result of the intersection.


Thus the overall space complexity for worst case scenario is O(m + n).