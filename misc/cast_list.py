def create_cast_list(filename):
    cast_list = []

    with open(filename, 'r') as f:
        for line in f:
            tokens = line.split(',')
            actor_name = tokens[0]
            cast_list.append(actor_name)

    return cast_list


print(create_cast_list('data/flying_circus_cast.txt'))
