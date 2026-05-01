from flask import Flask, request, jsonify
from flask_cors import CORS
# 导入刚才写的 db 模块
import db 

app = Flask(__name__)
CORS(app)

@app.route('/api', methods=['GET', 'POST'])
def handle_calculation():
    
    # --- 处理 GET 请求 (加载历史) ---
    if request.method == 'GET':
        # 从 db.py 获取历史列表
        history = db.get_history()
        return jsonify(history)

    # --- 处理 POST 请求 (进行计算) ---
    if request.method == 'POST':
        data = request.get_json()
        
        num1 = data.get('num1')
        num2 = data.get('num2')
        operator = data.get('operator')

        result = 0
        try:
            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                if num2 == 0:
                    return jsonify({"error": "除数不能为零"}), 400
                result = num1 / num2
            
            # --- 关键修改：保存到数据库 ---
            # 构造一条记录
            record = f"{num1} {operator} {num2} = {result}"
            # 调用 db.py 的函数保存它
            db.add_to_history(record)

            # 返回计算结果给前端
            return jsonify({"result": result})

        except Exception as e:
            return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)