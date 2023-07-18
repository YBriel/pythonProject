from bs4 import BeautifulSoup

filename = '/Users/yuzhen/PycharmProjects/pythonProject/demo2.html'
html = open(filename)

soup = BeautifulSoup(html, 'html.parser')
# 查找<div class="list-post">下的<article>标签下的所有<a>标签
div_list_post = soup.find_all('div', {'class': 'list-post'})
for post in div_list_post:
    article_tags = post.find_all('article')
    # 遍历所有的<a>标签，获取href和title属性
    for article in article_tags:
       # print(article_tags)
        a_tag2 = article.find('h2')
        a_tag = a_tag2.find('a')

        print(article)
        href = a_tag['href']
        title = a_tag['title']
        print('Link:', href)
        print('Title:', title)
     #   print('-----')



