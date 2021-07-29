# from tech_news.menu_pack import menu_options
import sys
from tech_news.scraper import get_tech_news
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_source,
    search_by_category,
)
from tech_news.analyzer.ratings import top_5_news, top_5_categories


def insert_database_opt():
    amount = input("Digite quantas notícias serão buscadas:")
    return get_tech_news(int(amount))


def search_by_title_opt():
    title = input("Digite o título:")
    return search_by_title(title)


def search_by_date_opt():
    date = input("Digite a data no formato aaaa-mm-dd:")
    return search_by_date(date)


def search_by_source_opt():
    source = input("Digite a fonte:")
    return search_by_source(source)


def search_by_category_opt():
    category = input("Digite a categoria:")
    return search_by_category(category)


def search_top5_news_opt():
    return top_5_news()


def search_top5_category_opt():
    return top_5_categories()


options = [
    ("Popular o banco com notícias", insert_database_opt),
    ("Buscar notícias por título", search_by_title_opt),
    ("Buscar notícias por data", search_by_date_opt),
    ("Buscar notícias por fonte", search_by_source_opt),
    ("Buscar notícias por categoria", search_by_category_opt),
    ("Listar top 5 notícias", search_top5_news_opt),
    ("Listar top 5 categorias", search_top5_category_opt),
]


# Requisito 12


def generate_view_menu():
    print("Selecione uma das opções a seguir:")

    for index, option in enumerate(options):
        print(f" {index} - {option[0]};")

    exit_index = len(options)
    print(f" {exit_index} - Sair.")

    option_selected = int(input())

    return option_selected if option_selected != exit_index else -1


def analyzer_menu():
    try:
        option_selected = generate_view_menu()

        if option_selected == -1:
            return print("Encerrando script")

        result = options[option_selected][1]()
        print(result)
    except ValueError:
        print("Opção inválida")
    except IndexError:
        print("Opção inválida", file=sys.stderr)
