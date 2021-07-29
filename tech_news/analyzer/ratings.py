import tech_news.database as db
from tech_news.analyzer.search_engine_pack import search_engine_service
from functools import reduce

# Requisito 10


def top_5_news():
    news_list = db.find_news()
    news_list.sort(
        key=lambda news: news["comments_count"] + news["shares_count"],
        reverse=True,
    )

    return search_engine_service.get_tuple_list(news_list[:5])


# Requisito 11
def spread_all_categories(news_list):
    categories_list = [news["categories"] for news in news_list]
    return reduce(
        lambda full_list, current: [*full_list, *current], categories_list, []
    )


def count_occurrences(items):
    return {category: items.count(category) for category in items}


def top_5_categories():
    news_list = db.find_news()
    categories_list = spread_all_categories(news_list)

    categories_occurrence = count_occurrences(categories_list)

    categories_occurrences_tuples = list(categories_occurrence.items())

    # alphabetical order
    categories_occurrences_tuples.sort(
        key=lambda category: category[0],
    )

    # order of occurrences
    categories_occurrences_tuples.sort(
        key=lambda category: category[1], reverse=True
    )

    sorted_categories = [
        category[0] for category in categories_occurrences_tuples
    ]

    return sorted_categories[:5]
