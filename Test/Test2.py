from bs4 import BeautifulSoup
import PostTem
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
}


html = requests.get(
    'https://cryptoslate.com/news',
    headers=headers).text

soup = BeautifulSoup(html, 'html.parser')
# 查找<div class="list-post">下的<article>标签下的所有<a>标签
div_list_post = soup.find_all('div', {'class': 'list-post'})
for post in div_list_post:
    article_tags = post.find_all('article')
    # 遍历所有的<a>标签，获取href和title属性

    for article in article_tags:
        try:
            a_tag2 = article.find('h2')
            a_tag = a_tag2.find('a')
            href = a_tag['href']
            title = a_tag['title']
            if href is not None:
                print(article['id'])
                print('Link:', href)
                print('Title:', title)
                PostTem.postTem(article['id'], href)
        except AttributeError as e:
            print('出现异常了')




