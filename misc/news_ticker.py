def truncate_headlines(headlines, max_chars):
    """
    concats headlines, limited by max_chars
    :param headlines:
    :param max_chars:
    :return:
    """
    return " ".join(headlines)[:max_chars]


headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

news_ticker = truncate_headlines(headlines, 140)
print(news_ticker)
# TODO: set news_ticker to a string that contains no more than 140 characters long.
# HINT: modify the headlines list to verify your loop works with different inputs
