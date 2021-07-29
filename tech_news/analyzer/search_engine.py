import tech_news.analyzer.search_engine_pack.search_engine_service as service

# Requisito 6


def search_by_title(title):
    news_list = service.search_off_case_sensitive("title", title)
    news_tuple_list = service.get_tuple_list(news_list)
    return news_tuple_list


# Requisito 7
def search_by_date(date):
    service.check_date(date)
    news_list = service.search_off_case_sensitive("timestamp", date)
    return service.get_tuple_list(news_list)


# Requisito 8
def search_by_source(source):
    news_list = service.search_off_case_sensitive("sources", source)
    return service.get_tuple_list(news_list)


# Requisito 9
def search_by_category(category):
    news_list = service.search_off_case_sensitive("categories", category)
    return service.get_tuple_list(news_list)
