def remove_duplicates(items):
    unique_items = []

    for item in items:
        if item not in unique_items:
            unique_items.append(item)

    return unique_items


print(remove_duplicates(['foo', 'bar', 'foo', 'bar', 'baz', 'bat', 'bar']))
print(remove_duplicates([1, 2, 'c', 43]))
print(remove_duplicates([]))
