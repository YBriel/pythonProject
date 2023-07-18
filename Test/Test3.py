from bs4 import BeautifulSoup

filename = '/Users/yuzhen/PycharmProjects/pythonProject/demo2.html'
html = open(filename)

soup = BeautifulSoup(html, 'html.parser')
# 查找<div class="list-post">下的<article>标签下的所有<a>标签
div_list_post = soup.find('div', {'class': 'list-feed slate'})
for post in div_list_post:
    article_tags = post.find_all('article')
    for article in article_tags:
        # a_tag2 = article.find('h2')
        a_tag = article.find('a')

#//*[@id="single-post-box-container-340799"]/div[1]/div[4]/div/article/p[1]
#//*[@id="single-post-box-container-340799"]/div[1]/div[4]/div/article/blockquote/p
#//*[@id="single-post-box-container-340799"]/div[1]/div[4]/div/article/p[12]
       # print(article)
        href = a_tag['href']
        title = a_tag['title']
        print('Link:', href)
        print('Title:', title)
#        print(article)
     #   print('-----')



