import requests
import time
import tech_news.scraper_services as scraper
from tech_news.database import create_news

# Requisito 1


def fetch(url):
    try:
        response = requests.get(url, timeout=3)
        time.sleep(1)
        return response.text if response.status_code == 200 else None
    except requests.Timeout:
        return None


# Requisito 2
def scrape_noticia(html_content):
    url = scraper.get_one(html_content, 'link[rel="canonical"]::attr("href")')
    title = scraper.get_one(
        html_content, 'h1[class="tec--article__header__title"]::text'
    )
    timestamp = scraper.get_one(html_content, "time::attr(datetime)")

    writer_contain = "a[contains(@href, 'autor')]"
    writer = scraper.cut_blanks_spaces(
        scraper.get_one_xpath(
            html_content,
            f"//p/{writer_contain}/text()|/{writer_contain}/text()",
        )
    )
    writer = writer if writer != "on" else None
    sources_query = '//div[contains(@class,"z--mb-16")]//a[contains(@title,"Ir para")]/text()'
    sources = scraper.cut_blanks_spaces_list(
        scraper.get_many_xpath(
            html_content,
            sources_query,
        )
    )
    attributes = dict(
        {
            "url": url,
            "title": title,
            "timestamp": timestamp,
            "writer": writer,
            "shares_count": scraper.extract_number(
                scraper.get_one(
                    html_content, 'div[class="tec--toolbar__item"]::text'
                )
            ),
            "comments_count": int(
                scraper.get_one(
                    html_content, "#js-comments-btn::attr(data-count)"
                )
            ),
            "summary": scraper.extract_summary(
                scraper.get_one(html_content, ".tec--article__body p")
            ),
            "sources": sources,
            "categories": scraper.cut_blanks_spaces_list(
                scraper.get_many(html_content, "#js-categories a::text")
            ),
        }
    )
    return attributes


# Requisito 3 class="tec--list__item"
def scrape_novidades(html_content):
    url_list = scraper.get_many(
        html_content,
        'main a[class="tec--card__title__link"]::attr(href)',
    )
    return url_list


# Requisito 4
def scrape_next_page_link(html_content):
    class_name = "tec--btn tec--btn--lg tec--btn--primary z--mx-auto z--mt-48"
    return scraper.get_one(
        html_content, f"a[class='{class_name}']::attr(href)"
    )


def scrape_all_to(url_list, stop_len):
    full_news_list = []

    for url_current in url_list:
        if len(full_news_list) == stop_len:
            break
        current_html_content = fetch(url_current)
        full_news = scrape_noticia(current_html_content)
        full_news_list.append(full_news)

    return full_news_list


# Requisito 5
def get_tech_news(amount):
    url = "https://www.tecmundo.com.br/novidades"
    full_news_list = list()

    while len(full_news_list) < amount:
        html_content = fetch(url)

        if not html_content:
            break

        url_list = scrape_novidades(html_content)
        stop_len = amount - len(full_news_list)
        current_full_news_list = scrape_all_to(url_list, stop_len)
        full_news_list.extend(current_full_news_list)

        url = scrape_next_page_link(html_content)

    create_news(full_news_list)
    return full_news_list
