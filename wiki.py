import wikipedia


def get_page(name):
    return wikipedia.summary(str(name))
