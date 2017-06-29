"""Please write a method to normalize a string which represents a file path.  
For the purposes of this question, normalizing means:

-all single dot components of the path must be removed.  For example, "foo/./bar" 
should be normalized to "foo/bar".
-all double dots components of the path must be removed, along with their 
parent directory.  For example, "foo/bar/../baz" should be normalized to "foo/baz".
 
That's it.  Normally, a path normalization algorithm would do aha lot of other 
stuff, but for this question, don't try any other kind of normalization or 
transformation of the path.  As an example, "foo//bar" should be normalized 
to "foo/bar" (i.e. a no-op).
"""


def normalize_path(path):
    """
    Normalize "path".

    This function takes in a string that denotes absolute file path and returns another
    string denoting the normalized absolute file path. 

    Function makes use of two other data structures, two lists:
        - my_path containing list of strings
        - my_stack containing filtered list of strings. 

    Runtime of this function is O(n).

    Function is written as standalone, not as a method of an object. 

    >>> normalize_path("foo/bar")
    'foo/bar'

    >>> normalize_path("foo/bar/../baz")
    'foo/baz'

    >>> normalize_path("foo//bar")
    'foo/bar'

    >>> normalize_path("foo/biz/rate/../bar")
    'foo/biz/bar'

    >>> normalize_path("")
    ''

    >>> normalize_path("/")
    '/'


    """

    if not path:
        return ''

    my_path = path.split('/')
    my_stack = []

    for item in my_path:
        if item:
            if my_stack:
                if my_stack[-1] == ".":
                    my_stack.pop()
                elif my_stack[-1] == "..":
                    my_stack.pop()
                    my_stack.pop()

            my_stack.append(item)

    if my_stack:
        return "/".join(my_stack)

    return "/"


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print