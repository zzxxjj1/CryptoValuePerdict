from newsapi import NewsApiClient
import json


key = '62187b5c441141f3a3d0de1d242b5062'
# Init
newsapi = NewsApiClient(api_key=key)

def searchCryptoNews(start_date, end_date, cryptocurrency = 'cryptocurrency'):
    all_articles = newsapi.get_everything(q = cryptocurrency,
                                          from_param = start_date,
                                          to = end_date,
                                          language = 'en',
                                          sort_by = 'popularity',
                                          page_size = 100)

    result_num = all_articles['totalResults']
    articles = all_articles['articles']
    
    # Search and dump all the news
    # pageSize = 100
    # num_of_page = (result_num // pageSize) + 1
    # if num_of_page >= 100:
    #     num_of_page = 99 # Maximum 100 searches per day, assuming no previous search took place
    # for i in range(2, num_of_page+1):
    #     all_articles = newsapi.get_everything(q = cryptocurrency,
    #                                        from_param = start_date,
    #                                        to = end_date,
    #                                        language = 'en',
    #                                        sort_by = 'popularity',
    #                                        page = i,
    #                                        page_size = 100)
    #     if all_articles['status'] == 'error':
    #         print('Reaches the daily search limit!')
    #         break
    #     else:
    #         temp = all_articles['articles']
    #         articles.extend(temp)
    
    #printing out the titles of all the articles
    #for x , y in enumerate(articles):
     #   print(f'{x} {y["title"]}')
    #printing out the keys of all the articles
    #for key, value in articles[0].items():
    #    print(f"\n{key.ljust(15)} {value}")
    with open('articles.json', 'w') as outfile:
        json.dump(articles, outfile)

    return articles

# Sample method
#searchCryptoNews('2021-10-01', '2021-10-05')
