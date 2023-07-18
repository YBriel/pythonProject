from bs4 import BeautifulSoup

# Your HTML content (assuming it's a complete HTML document)
html_content = """
<div class="parent">
    <p>First-Level Paragraph 1</p>
    <div>
        <p>Inner Paragraph</p>
    </div>
    <p>First-Level Paragraph 2</p>
</div>
"""

# Parse the HTML with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find the parent element
parent_element = soup.find(class_="parent")

# Find all the child tags of the parent element
child_tags = parent_element.find_all(recursive=False)

# Filter out the child tags that do not contain any grandchildren
direct_child_tags = [tag for tag in child_tags if not tag.find()]

# Extract and print the text content of the direct child tags
for tag in direct_child_tags:
    print(tag.get_text().strip())
