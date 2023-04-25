import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    files = []
    
    if os.path.isfile(path):
        if path.endswith(suffix):
            files.append(path)
    elif os.path.isdir(path):
        for item in os.listdir(path):
            files += find_files(suffix, os.path.join(path, item))
        
    return files

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1
print(find_files(".h", "./testdir")) # Expected output: ['./testdir\\subdir1\\a.h', './testdir\\subdir3\\subsubdir1\\b.h', './testdir\\subdir5\\a.h', './testdir\\t1.h']

# Test Case 2
print(find_files(".c", "./testdir")) # Expected output: ['./testdir\\subdir1\\a.c', './testdir\\subdir3\\subsubdir1\\b.c', './testdir\\subdir4\\subsubdir1\\subsubdir2\\b.c', './testdir\\subdir5\\a.c', './testdir\\t1.c']

# Test Case 3
print(find_files(".adasd", "./testdir")) # Expected output: []