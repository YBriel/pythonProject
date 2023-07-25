
first_level_p_tags = ['i', 'am', 'tom']
content = '  \n'.join([" " + p.strip() for p in first_level_p_tags])
content2 = '  \n'.join([" " + p for p in first_level_p_tags])
print(content)
print(content2)
