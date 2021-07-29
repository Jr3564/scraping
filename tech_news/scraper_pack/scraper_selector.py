from parsel import Selector


def get_one(base, query):
    selector = Selector(base)
    return selector.css(query).get()


def get_one_xpath(base, query):
    selector = Selector(base)
    return selector.xpath(query).get()


def get_many(base, query):
    selector = Selector(base)
    return selector.css(query).getall()


def get_many_xpath(base, query):
    selector = Selector(base)
    return selector.xpath(query).getall()
