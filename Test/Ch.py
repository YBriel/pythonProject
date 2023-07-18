from bs4 import BeautifulSoup

# 假设HTML文档存在于html变量中
html = '''
<div class="title">
    <h2>这是标题1</h2>
</div>
<div class="content">
    <h2>这是标题2</h2>
</div>
<div class="title">
    <h2>这是标题3</h2>
</div>
'''

# 创建BeautifulSoup对象
soup = BeautifulSoup(html, 'html.parser')

# 查找所有class属性值为"title"的div元素
div_titles = soup.find_all('div', {'class': 'title'})

# 遍历div_titles列表
for div_title in div_titles:
    # 查找div_title下的h2标签
    h2_tag = div_title.find('h2')
    # 提取h2标签的内容
    h2_content = h2_tag.text
    # 输出结果
    print(h2_content)
