class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if user in group.get_users():
        return True

    for sub_group in group.get_groups():
        if is_user_in_group(user, sub_group):
            return True

    return False

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1
def test_empty_group():
    empty_group = Group("empty")
    assert not is_user_in_group("some_user", empty_group), "Error: Test Case 1 failed"

# Test Case 2
def test_deeply_nested_user():
    main_group = Group("main_group")
    nested_group = main_group
    user = "deeply_nested_user"

    for i in range(5):
        new_group = Group(f"nested_group_{i}")
        nested_group.add_group(new_group)
        nested_group = new_group

    nested_group.add_user(user)

    assert is_user_in_group(user, main_group), "Error: Test Case 2 failed"

# Test Case 3
def test_general_case():
    # Create groups
    main_group = Group("main_group")
    group_a = Group("group_a")
    group_b = Group("group_b")
    group_c = Group("group_c")

    # Create users
    user1 = "user1"
    user2 = "user2"
    user3 = "user3"
    user4 = "user4"

    # Add users to groups
    group_a.add_user(user1)
    group_b.add_user(user2)
    group_c.add_user(user3)

    # Add groups to main_group
    main_group.add_group(group_a)
    main_group.add_group(group_b)
    main_group.add_group(group_c)

    # Test if users are in their respective groups
    assert is_user_in_group(user1, main_group), "Error: General Test Case failed - User1"
    assert is_user_in_group(user2, main_group), "Error: General Test Case failed - User2"
    assert is_user_in_group(user3, main_group), "Error: General Test Case failed - User3"

    # Test if a user not in any group is correctly identified
    assert not is_user_in_group(user4, main_group), "Error: General Test Case failed - User4"

    # Test if users are not found in the wrong groups
    assert not is_user_in_group(user1, group_b), "Error: General Test Case failed - Wrong Group User1"
    assert not is_user_in_group(user2, group_c), "Error: General Test Case failed - Wrong Group User2"
    assert not is_user_in_group(user3, group_a), "Error: General Test Case failed - Wrong Group User3"
    
if __name__ == "__main__":    
    test_empty_group()
    test_deeply_nested_user()
    test_general_case()
    print("All test cases passed")