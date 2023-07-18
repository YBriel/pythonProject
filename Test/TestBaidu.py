# from lxml import etree

from bs4 import BeautifulSoup

# from lxml import etree

# 遍历div_titles列表

try:
    filename = '/Users/yuzhen/PycharmProjects/pythonProject/demo.html'
    demo = open(filename, 'r')
    # soup = BeautifulSoup(demo, 'lxml')
    soup = BeautifulSoup(demo, 'html.parser')

    # a = soup.find_all('div', {'class': 'title'})

    # 查找所有class属性值为"title"的div元素
    div_titles = soup.find_all('div', {'class': 'article'})
    for div_title in div_titles:
        h2_tag = div_title.find('h2')
        print(h2_tag)
    # 你想要执行的，例如输出a的number属性值,可是a并没有number属性，这个时候就会报AttributeError的错误，为了让程序不报错而正常运行，你需要捕捉异常
        h2_content = h2_tag.text
    # 输出结果
        print(h2_content)
except AttributeError as e:
    # 捕捉异常
    print("a没有number属性")
    pass








    # print(soup.p.string)
# print("hello")
# print(type(soup))
