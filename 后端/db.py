import json
import os
from datetime import datetime

# 定义数据库文件名
DB_FILE = 'history.json'

def get_history():
    """
    从 JSON 文件中读取历史记录
    如果文件不存在，返回空列表
    """
    if not os.path.exists(DB_FILE):
        return []
    
    try:
        with open(DB_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return []

def add_to_history(item):
    """
    将新的计算记录添加到 JSON 文件中
    """
    # 1. 获取现有历史
    history = get_history()
    
    # 2. 创建新记录对象
    # 如果 item 已经是包含 time 的字典，则直接使用，否则包装一下
    if isinstance(item, dict) and 'time' in item:
        new_record = item
    else:
        new_record = {
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "detail": str(item)
        }

    # 3. 添加到列表
    history.append(new_record)
    
    # 4. 写回文件
    with open(DB_FILE, 'w', encoding='utf-8') as f:
        json.dump(history, f, ensure_ascii=False, indent=4)
        
    return history