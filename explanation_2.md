We will refer to each file and directory as a *node*.

# Walkthrough
The decision to use recursion in this function is based on the fact that the function needs to traverse all directories and subdirectories to find files with the given suffix. The use of recursion also makes the code more concise and easier to read. The function is able to handle an arbitrary number of nested directories without the need for complex loops or conditionals.

The `files` array (or list) is used to store the paths of all the files found with the specified suffix in the given path and its subdirectories.


# Time Efficiency
Time efficiency is $O(n)$ where n is the number of nodes.This is because the function recursively traverses all the directories and sub-directories to find the files with the given suffix. For each directory, the function calls `os.listdir()` which returns a list of all nodes in that directory. Then, the function iterates over each node in the list and calls itself recursively with the sub-path of that item.

# Space Efficiency
Space efficiency is $O(n)$ where n is the total number of nodes in the given path. This is because the function creates a list files to store the paths of all files with the given suffix. The size of this list can be at most n, which is the total number of nodes in the given path.