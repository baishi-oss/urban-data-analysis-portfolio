import json
from pathlib import Path

base_dir = Path(__file__).resolve().parent
input_path = base_dir / "facilities.json"
output_path = base_dir / "result.json"

try:
    # 1. 读取 facilities.json
    with open(input_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 2. 打印每个设施的 name，并累计数量
    total = 0
    for record in data:
        print(record['name'])
        total += record['quantity']

    # 3. 把统计结果保存到 result.json
    result = {'设施总数': total}
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=4)

except FileNotFoundError:
    print("文件未找到，请检查文件路径是否正确。")
except json.JSONDecodeError:
    print("JSON 解码错误，请检查 JSON 文件的格式是否正确。")
