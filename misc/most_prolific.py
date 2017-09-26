def most_prolific(discography):
    """
    given a discography, return the year(s) in which the most albums were released
    :param discography:
    :return:
    """
    year_counts = {}

    for title in discography:
        year = discography[title]
        if year in year_counts:
            year_counts[year] += 1
        else:
            year_counts[year] = 1

    return max(year_counts, key=year_counts.get)


Beatles_Discography = {"Please Please Me": 1963, "With the Beatles": 1963,
    "A Hard Day's Night": 1964, "Beatles for Sale": 1964, "Twist and Shout": 1964,
    "Help": 1965, "Rubber Soul": 1965, "Revolver": 1966,
    "Sgt. Pepper's Lonely Hearts Club Band": 1967,
    "Magical Mystery Tour": 1967, "The Beatles": 1968,
    "Yellow Submarine": 1969 ,'Abbey Road': 1969,
    "Let It Be": 1970}

# for album_title in Beatles_Discography:
#     print("title: {}, year: {}".format(album_title, Beatles_Discography[album_title]))

foo = {"Please Please Me": 1963, "With the Beatles": 1963,
    "A Hard Day's Night": 1964, "Beatles for Sale": 1964,
    "Help": 1965, "Rubber Soul": 1965, "Revolver": 1966,
    "Sgt. Pepper's Lonely Hearts Club Band": 1967,
    "Magical Mystery Tour": 1967, "The Beatles": 1968,
    "Yellow Submarine": 1969 ,'Abbey Road': 1969,
    "Let It Be": 1970}

#print(most_prolific(Beatles_Discography))
print(most_prolific(foo))
