def opencsv():
    import csv
    from collections import namedtuple
    # 读取
    # csv.read() 设置delimiter='\t'，即以Tab作为分隔符读取数据
    with open('C:\\Users\\Ronnie Yang\\PycharmProjects\\notes\\python_cookbook\\capture_8\\test.csv') as f:
        f_csv = csv.reader(f)
        headers = next(f_csv)
        for row in f_csv:  # 显示所有数据
            print(row)

    with open('C:\\Users\\Ronnie Yang\\PycharmProjects\\notes\\python_cookbook\\capture_8\\test.csv') as f:
        f_csv = csv.reader(f)
        headings = next(f_csv)
        Row = namedtuple('Row', headings)
        for r in f_csv:  # 按照下标显示
            row = Row(*r)
            print(row.Symbol)

    with open('C:\\Users\\Ronnie Yang\\PycharmProjects\\notes\\python_cookbook\\capture_8\\test.csv') as f:
        f_csv = csv.DictReader(f)
        for row in f_csv:  # 以字典的形式储存
            print(row['Change'])

    # 写入
    headers = ['Symbol', 'Price', 'Date', 'Time', 'Change', 'Volume']
    rows = [('TEST', 222.58, '6/11/2222', '12:36am', -0.22, 935000)]
    with open('capture_8/stocks.csv', 'w') as f:  # 列表序列
        f_csv = csv.writer(f)
        f_csv.writerow(headers)
        f_csv.writerows(rows)
    rows = [{'Symbol': 'AA', 'Price': 39.48, 'Date': '6/11/2007',
             'Time': '9:36am', 'Change': -0.18, 'Volume': 181800},
            {'Symbol': 'AIG', 'Price': 71.38, 'Date': '6/11/2007',
             'Time': '9:36am', 'Change': -0.15, 'Volume': 195500}]
    with open('capture_8/dictstocks.csv', 'w') as f:  # 字典序列
        f_csv = csv.DictWriter(f, headers)
        f_csv.writeheader()
        f_csv.writerows(rows)

    field_types = [('Price', float),
                   ('Change', float),
                   ('Volume', int)]
    with open('capture_8/stocks.csv') as f:  # 按照filed_types将某些列转为int，float等
        for row in csv.DictReader(f):
            row.update((key, conversion(row[key])) for key, conversion in field_types)
            print(row)


def openjson():
    import json
    data = {
        'name': 'ACME',
        'shares': 100,
        'price': 542.23
    }
    json_str = json.dumps(data)  # 编码为json格式
    data = json.loads(json_str)  # 解码为python格式
    print(data)

    from pprint import pprint
    # pprint()会根据key的顺序来输出，更方便查看

# 关于xml的部分，因为大量网页会涉及到js渲染的问题，不能简单依靠xml的代码来检索数据，因此xml部分的暂且跳过

# 读取二进制数据使用struct库相关



openjson()



