import re
from datetime import datetime
import tech_news.database as db


def get_tuple_list(news_list):
    return list(map(lambda news: (news["title"], news["url"]), news_list))


def check_date(date):
    try:
        return datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")


def search_off_case_sensitive(key, search):
    return db.search_news({key: {"$regex": re.compile(search, re.IGNORECASE)}})
