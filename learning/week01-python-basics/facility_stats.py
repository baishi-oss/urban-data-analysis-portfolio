
def clean_records(records):
    cleaned_records = []
    for record in records:
        if record.get("category") and record.get("district"):
            cleaned_records.append(record)
    return cleaned_records


def sum_by_category(records):
    result_1={}
    for record in records:
        category = record.get("category")
        quantity = record.get("quantity")
        result_1[category] = result_1.get(category, 0) + quantity
    return result_1


def sum_by_district(records):
    result_2={}
    for record in records:
        district = record.get("district")
        quantity = record.get("quantity")
        result_2[district] = result_2.get(district, 0) + quantity
    return result_2
