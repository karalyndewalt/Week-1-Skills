"""Skills Assessment: Lists.

To work on an item, uncomment the entire function (including the docstring)
and then run this script. It should output an error that the newly-uncommented
function is now failing its tests.

Edit the function body until you have a solution and the test passes, and then
move on to the next function.

This assessment is DUE TO YOUR ADVISOR BY SUNDAY EVENING.
"""


def all_odd(number_list):
    """Return a list of only the odd numbers in the input list.

        >>> all_odd([1, 2, 7, -5])
        [1, 7, -5]

        >>> all_odd([2, -6, 8])
        []

    """
    all_odd = []
    all_even = []
    for num in number_list:
        # if num % 2 == 0:
        #     all_even.append(num)
        # else:
        #     all_odd.append(num)
        if num % 2 != 0:
            all_odd.append(num)
    return all_odd


def all_even(number_list):
    """Return a list of only the even numbers in the input list.

        >>> all_even([2, 6, -1, -2])
        [2, 6, -2]

        >>> all_even([-1, 3, 5])
        []

    """
    all_even = []
    for num in number_list:
        if num % 2 == 0:
            all_even.append(num)

    return all_even


def print_indeces(my_list):
    """Print the index of each list item, followed by the item itself.
    Do this without using a counting variable. I.e. don't do something
    like this:

    count = 0
    for item in list:
        print count
        count = count + 1

    Output should look like this:

    >>> print_indeces(["Toyota", "Jeep", "Volvo"])
    0 Toyota
    1 Jeep
    2 Volvo

    """
    #wanted to use unpacking, but in looking up syntax saw the answer... :( cheating..
    # enumerate()
    for indicies in range(len(my_list)):
        print indicies, my_list[indicies]

    #** try to make into a list comprehension


def long_words(word_list):
    """Return all words in input list that are longer than 4 characters.

        >>> long_words(["hello", "hey", "spam", "spam", "bacon", "bacon"])
        ['hello', 'bacon', 'bacon']

        >>> long_words(["all", "are", "tiny"])
        []

    """
    # long_words = []
    # for word in word_list:
    #     if len(word) > 4:
    #         long_words.append(word)
    # return long_words
    return [word for word in word_list if len(word) > 4]


def smallest_int(number_list):
    """Find the smallest integer in a list of integers and return it.

        >>> smallest_int([-5, 2, -5, 7])
        -5


    If the input list is empty, return None:

        >>> smallest_int([]) is None
        True

    """
    # if else seems real janky. also checking [0] against [0], silly.
    smallest_int = []
    if number_list == []:
        return None
    else:
        for num in number_list:
            smallest_int = number_list[0]
            if num < smallest_int:
                smallest_int = num
    return smallest_int

    # Come back and try using reduce

    # special docstring test. -> my code fails this test.
    #    >>> smallest_int([2, -5, 1, 0])
    #   -5

    #first
    #bubble search/binary? need count, compare [n] to [n+1] keeping smallest number
    # # under small_num variable. return small_num at the end of the loop
    #     if number_list == []:
    #         return number_list
    #     else:
    #         count = 0
    #         index_of_smallest_int = 0
    #         smallest_int = []
    #         for num in number_list:
    #             if num[index_of_smallest_int] < num[count + 1]:
    #                 smallest_int = num[index_of_smallest_int]
    #                 count += 1
    #             else:
    #                 smallest_int = num[count + 1]
    #                 index_of_smallest_int += 1
        # return smallest_int


def largest_int(number_list):
    """Find the largest integer in a list of integers and return it.

        >>> largest_int([-5, 2, -5, 7])
        7

    If the input list is empty, return None:

        >>> largest_int([]) is None
        True

    """
    if number_list == []:
        return None
    else:
        for num in number_list:
            largest_int = number_list[0]
            if num > largest_int:
                largest_int = num

        return largest_int


def halvesies(number_list):
    """Return list of numbers from input list, each divided by two.

        >>> halvesies([2, 6, -2])
        [1.0, 3.0, -1.0]

    If any of the numbers are, make sure you don't round off the half:

        >>> halvesies([1, 5])
        [0.5, 2.5]

    """
    # number_list = float(number_list) Error float() for stirng or number
    return [num/2.0 for num in number_list]


def word_lengths(word_list):
    """Return the length of words in the input list.

        >>> word_lengths(["hello", "hey", "hello", "spam"])
        [5, 3, 5, 4]

    """

    return [len(word) for word in word_list]


def sum_numbers(number_list):
    """Return the sum of all of the numbers in the list.

    Python has a built-in function, `sum()`, which already does this -- but for
    this exercise, you should not use it.

        >>> sum_numbers([1, 2, 3, 10])
        16

    Any empty list should return the sum of zero:

        >>> sum_numbers([])
        0

    """
    total = 0
    for num in number_list:
        total += num
    return total
    # addition = (lambda total: total + num for num in number_list)
    # return addition


def mult_numbers(number_list):
    """Return product (result of multiplication) of the numbers in the list.

        >>> mult_numbers([1, 2, 3])
        6

    Obviously, if there is a zero in the input, the product will be zero:

        >>> mult_numbers([10, 20, 0, 50])
        0

    As explained at http://en.wikipedia.org/wiki/Empty_product, if the list is
    empty, the product should be 1:

        >>> mult_numbers([])
        1

    """
    total = 1
    for num in number_list:
        total = total * num
    return total


def join_strings(word_list):
    """Return a string of all input strings joined together.

    Python ha a built-in method on lists, `join` -- but this exercise, you
    should not use it.

        >>> join_strings(["spam", "spam", "bacon", "balloonicorn"])
        'spamspambaconballoonicorn'

    For an empty list, you should return an empty string:

        >>> join_strings([])
        ''

    """
    string = ""
    for word in (word_list):
        string += word
    return string


def average(number_list):
    """Return the average (mean) of the list of numbers given.

        >>> average([2, 12, 3])
        5.666666666666667

    There is no defined answer if the list given is empty. It's fine if
    this raises an error when given an empty list.
    """
    # sum_of_num/index count must be float

    avg = 0
    sum_of_num = 0
    list_len = 0
    for num in number_list:
        sum_of_num += float(num)
        list_len = float(len(number_list))
        avg = sum_of_num/list_len
    return avg



#############################################################################
# END OF SKILLS TEST: You can stop here, or read on to work on advanced problem.

# Uncomment the function below to work on the advanced problem.
# Tip: To comment or uncomment blocks of code, highlight what you want to
#    comment or uncomment, and then CMD+"/" or CTRL-"/"

# def advanced_join_strings(list_of_words):
#     """Return a single string with each word from the input list
#     separated by a comma.

#         >>> advanced_join_strings(["Labrador", "Poodle", "French Bulldog"])
#         'Labrador, Poodle, French Bulldog'

#     If there's only one thing in the list, it should return just that
#     thing, of course:

#         >>> advanced_join_strings(["Pretzel"])
#         'Pretzel'

#     """

#     return ""

# END OF ASSIGNMENT: You can ignore everything below.
##############################################################################

if __name__ == "__main__":
    import doctest
    print
    result = doctest.testmod()
    if not result.failed:
        print "*** %s TESTS PASSED. GOOD WORK!" % result.attempted
    print
