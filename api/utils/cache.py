import asyncio
from werkzeug.contrib.cache import SimpleCache

cache_content = SimpleCache(default_timeout=7000)


def set_result_in_cache(search_result):
    cache_content.set('search_result', search_result)
    

def get_data_from_cache():
    retrieved_data = cache_content.get('search_result')

    return retrieved_data['results']
