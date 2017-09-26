def is_tag(tag):
    """
    indicates if provided tag is an XML tag. i.e. looks like <this>.
    will choke on empty string
    :param tag:
    :return:
    """
    return tag[0] == '<' and tag[-1] == '>'

def tag_count(tags):
    """Write a function, `tag_count`, that takes as its argument a list
    of strings. It should return a count of how many of those strings
    are XML tags. You can tell if a string is an XML tag if it begins
    with a left angle bracket "<" and end with a right angle bracket ">".
    """
    num_tags = 0

    for tag in tags:
        if is_tag(tag):
            num_tags += 1

    return num_tags


# Test for the tag_count function:
list1 = ['<greeting>', 'Hello World!', '</greeting>']
count = tag_count(list1)
print("Expected result: 2, Actual result: {}".format(count))
