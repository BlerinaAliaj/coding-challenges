"""A sequence of integers is called a zigzag sequence if each of its elements is either strictly less than both neighbors or strictly greater than both neighbors. For example, the sequence 4 2 3 1 5 3 is a zigzag, but 7 3 5 5 2 and 3 8 6 4 5 aren't.
For a given array of integers return the length of its longest contiguous sub-array that is a zigzag sequence.
Example
For a = [9, 8, 8, 5, 3, 5, 3, 2, 8, 6], the output should be
zigzag(a) = 4.
The longest zigzag sub-arrays are [5, 3, 5, 3] and [3, 2, 8, 6] and they both have length 4.
Input/Output
[time limit] 4000ms (py)
[input] array.integer a
Guaranteed constraints:
2 <= a.length <= 25,
0 <= a[i] <= 100.
[output] integer

"""


def longest_sub(arr):

    """Return the length of the longest zig-zag sub array"""

    if not arr:
        return 0

    longest = 1
    sub_arr = [arr[0]]

    if len(arr) == 2 and arr[0] != arr[-1]:
        return len(arr)

    for i in range(1, len(arr)-1):
        if (arr[i] > arr[i-1] and arr[i] > arr[i+1]) or (arr[i] < arr[i-1] and arr[i] < arr[i+1]):
            if i == len(arr)-2:
                sub_arr.append(arr[i])
                sub_arr.append(arr[i+1])
            else:
                sub_arr.append(arr[i])

            longest = len(sub_arr)
        else:
            sub_arr.append(arr[i])
            longest = max(longest, len(sub_arr))
            sub_arr = [arr[i]]
    return longest


def test():
    assert longest_sub([9, 8, 8, 5, 3, 5, 3, 2, 8, 6]) == 4
    assert longest_sub([1, 2, 0, 3, 2, 1, 3, 2, 4, 0]) == 6
    assert longest_sub([1, 2, 1]) == 3
    assert longest_sub([1, 2]) == 2
    assert longest_sub([1, 1]) == 1
    assert longest_sub([]) == 0

test()
