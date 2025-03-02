# DSS-education-systeam
DSS for Multimedia Learning 是一个面向多媒体学习环境的决策支持系统（Decision Support System, DSS）原型。该项目整合了数据处理、机器学习模型、学习进度追踪以及数据可视化等模块，旨在通过智能化的数据分析与个性化推荐来提高学生的学习效率和认知能力。  项目主要目标包括：  提高学习效率：根据学生的学习行为数据，为学生推荐个性化的学习资源，从而帮助学生更高效地掌握知识。 提升认知能力：通过实时反馈和动态调整学习内容，帮助学生改善理解、记忆和问题解决能力。 个性化学习路径规划：利用机器学习技术，根据学生的实际学习情况生成个性化的学习路径，满足不同学生的需求。 数据可视化：通过直观的图表展示学习进度和相关数据，帮助教师和学生及时掌握学习效果。
DSS for Multimedia Learning
项目介绍
DSS for Multimedia Learning 是一个面向多媒体学习环境的决策支持系统（Decision Support System, DSS）原型。该项目整合了数据处理、机器学习模型、学习进度追踪以及数据可视化等模块，旨在通过智能化的数据分析与个性化推荐来提高学生的学习效率和认知能力。

项目主要目标包括：

提高学习效率：根据学生的学习行为数据，为学生推荐个性化的学习资源，从而帮助学生更高效地掌握知识。
提升认知能力：通过实时反馈和动态调整学习内容，帮助学生改善理解、记忆和问题解决能力。
个性化学习路径规划：利用机器学习技术，根据学生的实际学习情况生成个性化的学习路径，满足不同学生的需求。
数据可视化：通过直观的图表展示学习进度和相关数据，帮助教师和学生及时掌握学习效果。
功能说明
1. 数据处理模块
功能：
从 CSV 文件中加载学习数据（包括学习目标、问题描述、反馈建议和成绩等）。
对数据进行基本清洗（去除缺失值等）。
使用 LabelEncoder 对字符串特征进行编码，生成数值型数据，供后续机器学习模型训练使用。
文件：src/data_processing.py
2. 决策支持系统模块
功能：
使用 RandomForestClassifier 对学习数据进行建模，并根据学生的输入（如学习目标、问题和反馈）生成个性化的学习推荐。
保持训练和预测数据格式一致，确保预测结果能够正确映射到预定义的标签（如 Math、Physics、History、Chemistry）。
文件：src/decision_support.py
3. 学习进度追踪模块
功能：
为每个学生记录和更新学习进度或成绩。
提供接口获取指定学生的最新学习进度信息，便于教师和学生实时查看学习状态。
文件：src/learning_tracker.py
4. 用户输入模块
功能：
从控制台或 CSV 文件中获取用户（学生）的输入数据，包括学习目标、问题描述及反馈。
文件：src/user_input.py
5. 数据可视化模块
功能：
根据学习进度数据生成直观的柱状图，展示各学习者的学习进度。
支持保存高分辨率图像文件，便于在外部查看器中获得清晰的图像效果。
文件：src/visualization.py
部署与安装
环境要求
Python 版本：3.8 及以上（建议 Python 3.12）
依赖库：
pandas
numpy
scikit-learn
matplotlib
安装步骤
克隆项目

bash
复制
(https://github.com/Chenxu1103/DSS-education-systeam)
cd DSS_Multimedia_Learning_Project
安装依赖 使用 pip 安装项目依赖：

bash
复制
pip install -r requirements.txt
运行项目 运行项目主入口：

bash
复制
python main.py
项目将依次执行数据加载、模型训练、生成学习推荐、更新学习进度，并展示数据可视化图表（图表同时会保存为高分辨率的 PNG 文件）。

部署接口文档
如果你希望将该项目扩展为 Web 服务以便通过 API 进行交互，可以参考下面的部署接口文档示例。以下文档基于 Flask 框架，假设你已经创建了一个 Web 服务器（例如 app.py），并将部分功能暴露为 API 接口。

API 概述
该 API 服务主要提供以下两个功能接口：

学习推荐接口：根据学生输入返回个性化学习推荐。
学习进度查询接口：查询指定学生的学习进度数据。
1. 学习推荐接口
接口 URL：POST /api/predict
请求示例：
json
复制
{
  "goal": 2,
  "problem": 1,
  "feedback": 0
}
其中各字段的数值需与数据处理时的编码结果一致。
响应示例：
json
复制
{
  "recommended_subject": "History"
}
描述：
接口接收一个 JSON 格式的请求体，其中包含用户输入的数值化特征。服务器使用训练好的决策支持模型生成学习推荐，并返回对应的推荐学科。
2. 学习进度查询接口
接口 URL：GET /api/progress/<user_id>
请求示例：
bash
复制
GET /api/progress/UserA
响应示例：
json
复制
{
  "user_id": "UserA",
  "progress": 85
}
描述：
接口接收 URL 路径中的 user_id 参数，返回对应学生的学习进度数据。如果没有记录，则返回提示信息。
Flask 示例代码
以下是一个简单的 Flask 服务器示例（可保存为 app.py），用于部署上述 API 接口：

python
复制
from flask import Flask, request, jsonify
from src.decision_support import DecisionSupportSystem
from src.learning_tracker import LearningTracker
import pandas as pd
import numpy as np

app = Flask(__name__)

# 示例加载数据和模型（实际项目中可按需调整）
# 假设数据已经加载并预处理好，以下仅为示例：
sample_features = pd.DataFrame({
    'goal': [0, 1, 2, 3],
    'problem': [0, 1, 2, 3],
    'feedback': [0, 1, 2, 3]
})
labels = ['Math', 'Physics', 'History', 'Chemistry']
dss = DecisionSupportSystem(sample_features, labels)

# 学习进度追踪示例（全局变量，实际部署可接入数据库）
tracker = LearningTracker()
tracker.track_progress('UserA', 85)
tracker.track_progress('UserB', 70)

@app.route('/api/predict', methods=['POST'])
def predict():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid input"}), 400
    # 假设 data 中包含 'goal', 'problem', 'feedback'
    try:
        user_data = {
            'goal': int(data['goal']),
            'problem': int(data['problem']),
            'feedback': int(data['feedback'])
        }
    except KeyError:
        return jsonify({"error": "Missing required fields"}), 400

    recommended_subject = dss.generate_recommendation(user_data)
    return jsonify({"recommended_subject": recommended_subject})

@app.route('/api/progress/<user_id>', methods=['GET'])
def get_progress(user_id):
    progress = tracker.get_progress(user_id)
    return jsonify({"user_id": user_id, "progress": progress})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
部署说明
安装 Flask：

bash
复制
pip install flask
运行 Flask 服务：

bash
复制
python app.py
服务器启动后，会监听 5000 端口。你可以通过 Postman 或浏览器测试 API，例如：

POST 请求 http://localhost:5000/api/predict 传入 JSON 数据；
GET 请求 http://localhost:5000/api/progress/UserA 查询用户进度。
生产部署：
若需要生产部署，可以使用 Gunicorn 等 WSGI 服务器，并结合 Nginx 等反向代理进行部署。

贡献指南
欢迎各位开发者和教育工作者参与贡献！

如有建议或问题，请提交 issue。
代码提交请遵循 PEP8 编码规范，并在提交前确保所有单元测试通过。
许可证
该项目遵循 MIT 许可证。

