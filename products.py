import os 

def read_file(filename): #讀取檔案
    products = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            if '商品,價格' in line:
                continue
            name, price = line.strip().split(',')
            products.append([name, price])
    return products
    
#請使用者輸入
def user_input(products):
    while True:
        name = input('請輸入商品名稱：')
        if name == 'q':
            break 
        price = input('請輸入商品價格：')
        price = int(price)
        products.append([name, price])
    print(products)
    return products

#印出所有商品購買紀錄
def print_products(products):
    for p in products:
        print(p[0], '的價格是', p[1])

# 寫入檔案
def write_file(filename, products):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('商品,價格\n')
        for p in products:
            f.write(p[0] + ',' + str(p[1]) + '\n')

def main():
    filename = 'products.csv'
    if os.path.isfile(filename): #檢查檔案是否在同一個資料夾
        print ('Yeah, the file is found!')
        products = read_file(filename)
    else:
        print('cant found the file!')
    products = user_input(products) #將products 原本個database擺入個function到，有新輸入野後save翻；落products
    print_products(products)
    write_file('products.csv', products)

main()
