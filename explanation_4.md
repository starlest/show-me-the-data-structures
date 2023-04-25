# Walkthrough
We use recursion to check all available sub groups.


# Time Efficiency
In the worst case, the function would have to traverse all groups and sub-groups in the hierarchy and check all users in each group. Assuming there are n groups (including sub-groups) and the maximum number of users in a group is m, the time complexity would be **O(n * m)**. This is because, in the worst-case scenario, the function checks every user in each group.

# Space Efficiency
The space complexity is determined by the maximum depth of the recursion, which corresponds to the maximum depth of the group hierarchy. In the worst case, the function would need to store one function call for each level of recursion on the call stack. Assuming the maximum depth of the group hierarchy is d, the space complexity would be **O(d)**.