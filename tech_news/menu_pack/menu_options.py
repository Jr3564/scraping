from tech_news import scraper
from tech_news.analyzer import search_engine
from tech_news.analyzer import ratings


def insert_database_opt():
    amount = input("Digite quantas notícias serão buscadas:")
    return scraper.get_tech_news(int(amount))


def search_by_title_opt():
    title = input("Digite o título:")
    return search_engine.search_by_title(title)


def search_by_date_opt():
    date = input("Digite a data no formato aaaa-mm-dd:")
    return search_engine.search_by_date(date)


def search_by_source_opt():
    source = input("Digite a fonte:")
    return search_engine.search_by_source(source)


def search_by_category_opt():
    category = input("Digite a categoria:")
    return search_engine.search_by_category(category)


def search_top5_news_opt():
    return ratings.top_5_news()


def search_top5_category_opt():
    return ratings.top_5_categories()


options = [
    ("Popular o banco com notícias", insert_database_opt),
    ("Buscar notícias por título", search_by_title_opt),
    ("Buscar notícias por data", search_by_date_opt),
    ("Buscar notícias por fonte", search_by_source_opt),
    ("Buscar notícias por categoria", search_by_category_opt),
    ("Listar top 5 notícias", search_top5_news_opt),
    ("Listar top 5 categorias", search_top5_category_opt),
]
