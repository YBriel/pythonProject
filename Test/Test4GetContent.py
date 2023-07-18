from bs4 import BeautifulSoup

filename = '/Users/yuzhen/PycharmProjects/pythonProject/demo3.html'
html = open(filename)

soup = BeautifulSoup(html, 'html.parser')
# 查找<div class="list-post">下的<article>标签下的所有<a>标签
title = soup.find('h1', {'class': 'post-title'})
print("文章标题:{}",title)

#文章id
cover = soup.find('div', {'class': 'post-header article clearfix'})
#文章封面
coverInfo = cover.find('img', {'class': 'nolazy'})
#print(coverInfo)
#print(coverInfo['src']) #图片地址

#文章内图片
pics = soup.find_all('figure', {'class': 'wp-caption aligncenter'})
for pic in pics:
    contentPic = pic.find('img')
    #print(contentPic['src'])
#文章内容

# articles = soup.find_all('article')
# print(articles)
# articleRes = articles.find_all('p')
# for ar in articleRes:
#     print(ar)
paragraphs = soup.find_all('p')
content = '\n'.join([p.text.strip() for p in paragraphs])
print('文章内容：\n', content)








