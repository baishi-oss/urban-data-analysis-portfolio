from facility_stats import clean_records, sum_by_category, sum_by_district

def main(records):
    new_records = clean_records(records)
    dict_sum_1 = sum_by_category(new_records)
    dict_sum_2 = sum_by_district(new_records)

    print('按类别统计：')
    for k,v in dict_sum_1.items():
        print(f'{k}:{v}')

    print('按行政区统计：')
    for k,v in dict_sum_2.items():
        print(f'{k}:{v}')

    #清洗数据,分类统计,打印结果

records = [
    {"name": "社区卫生服务中心", "category": "医疗", "district": "鼓楼", "quantity": 2},
    {"name": "社区卫生服务站", "category": "医疗", "district": "玄武", "quantity": 1},
    {"name": "小学", "category": "教育", "district": "鼓楼", "quantity": 5},
    {"name": "幼儿园", "category": "教育", "district": "玄武", "quantity": 2},
    {"name": "图书馆", "category": "文化", "district": "鼓楼", "quantity": 1},
    {"name": "公园", "category": "休闲", "district": "玄武", "quantity": 1},

    # 以下两条应被清洗掉
    {"name": "待核实", "category": "", "district": "鼓楼", "quantity": 3},
    {"name": "未知设施", "category": "教育", "district": "", "quantity": 2},
]

if __name__ == "__main__":
    main(records)
