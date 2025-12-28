import json
import pandas as pd
from typing import Union, List, Dict, Any


def json_to_excel(json_data: Union[str, List[Dict[str, Any]]], excel_path: str):
    """
    将JSON数据转换为Excel文件
    
    :param json_data: JSON文件路径或JSON数据列表
    :param excel_path: 输出Excel文件路径
    """
    # 如果输入是字符串（文件路径），则先加载JSON
    if isinstance(json_data, str):
        with open(json_data, 'r', encoding='utf-8') as f:
            data = json.load(f)
    else:
        data = json_data

    # 准备转换为DataFrame的数据
    rows = []
    for item in data:
        row = {}
        for key, value in item.items():
            # 将所有值转换为字符串
            if isinstance(value, list):
                row[key] = ', '.join(map(str, value))
            elif isinstance(value, dict):
                # 对于嵌套的字典，将其转换为JSON字符串
                row[key] = json.dumps(value, ensure_ascii=False)
            else:
                row[key] = str(value)
        rows.append(row)

    # 创建DataFrame
    df = pd.DataFrame(rows)
    
    # 保存到Excel
    df.to_excel(excel_path, index=False)
    print(f"JSON数据已成功转换为Excel并保存到: {excel_path}")


def excel_to_json(excel_path: str, json_path: str):
    """
    将Excel文件转换为JSON格式
    
    :param excel_path: Excel文件路径
    :param json_path: 输出JSON文件路径
    """
    # 读取Excel文件
    df = pd.read_excel(excel_path)
    
    # 转换回JSON格式
    json_data = []
    for _, row in df.iterrows():
        item = {}
        for col in df.columns:
            value = row[col]

            if col == "key":
                item[col] = value
            else:
                # 如果单元格内容是字符串且以{或[开头，尝试解析为JSON
                if isinstance(value, str) and value.startswith(('{', '[')):
                    try:
                        item[col] = json.loads(value)
                    except json.JSONDecodeError:
                        # 如果解析失败，保持为字符串
                        item[col] = value
                # 如果值是NaN，设置为适当的默认值
                elif pd.isna(value):
                    item[col] = [""]
                # 如果值包含逗号，且原始JSON中可能为数组，则拆分为列表
                elif isinstance(value, str) and ',' in value and col in ['time', 'space', 'parents', 'kids', 'persons', 'works', 'concepts', 'inventions']:
                    item[col] = [x.strip() for x in value.split(',')]
                else:
                    item[col] = [value]
        json_data.append(item)

    # 保存为JSON文件
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(json_data, f, ensure_ascii=False, indent=2)
    
    print(f"Excel数据已成功转换为JSON并保存到: {json_path}")


def main():
    import sys
    if len(sys.argv) != 4:
        print("使用方法:")
        print("  JSON转Excel: python json_excel_converter.py json2excel <input.json> <output.xlsx>")
        print("  Excel转JSON: python json_excel_converter.py excel2json <input.xlsx> <output.json>")
        return

    operation = sys.argv[1]
    input_path = sys.argv[2]
    output_path = sys.argv[3]

    if operation == "json2excel":
        json_to_excel(input_path, output_path)
    elif operation == "excel2json":
        excel_to_json(input_path, output_path)
    else:
        print("操作必须是 'json2excel' 或 'excel2json'")


if __name__ == "__main__":
    main()
    # python json_excel_converter.py json2excel math.json math.xlsx
    # python json_excel_converter.py excel2json math.xlsx math.json
    # python json_excel_converter.py json2excel pysics.json pysics.xlsx
    # python json_excel_converter.py excel2json pysics.xlsx pysics.json
