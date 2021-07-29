import re
import tech_news.scraper_pack.scraper_selector as selector


def cut_blanks_spaces(string):
    return str(string)[1:-1]


def cut_blanks_spaces_list(item_list):
    items = item_list if type(item_list) == "list" else list(item_list)
    return list(map(lambda category: cut_blanks_spaces(category), items))


def extract_number(string):
    if not isinstance(string, str):
        return 0
    return int(re.sub(r"\D", "", string))


def extract_summary(base):
    content_list = "".join(selector.get_many(base, "*::text"))
    return content_list


def get_writer(base):
    writer_contain = "a[contains(@href, 'autor')]"
    writer = cut_blanks_spaces(
        selector.get_one_xpath(
            base,
            f"//p/{writer_contain}/text()|/{writer_contain}/text()",
        )
    )
    return writer if writer != "on" else None


def get_sources(base):
    sources_contain = (
        'contains(@class,"z--mb-16")',
        'contains(@title,"Ir para")',
    )
    sources = cut_blanks_spaces_list(
        selector.get_many_xpath(
            base,
            f"//div[{sources_contain[0]}]//a[{sources_contain[1]}]/text()",
        )
    )
    return sources
