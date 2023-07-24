
print("he")
a = 'https://cryptoslate.com/wp-content/themes/cryptoslate-2020/imgresize/timthumb.php?src=https://cryptoslate.com/wp-content/uploads/2022/06/doj-crypto-crime.jpg&w=800&h=420&q=75 1.5x, https://cryptoslate.com/wp-content/themes/cryptoslate-2020/imgresize/timthumb.php?src=https://cryptoslate.com/wp-content/uploads/2022/06/doj-crypto-crime.jpg&w=1200&h=630&q=75 2x'
b = a.rsplit(',')[-1].replace('2x', '').strip()
print(b)
