# src/decision_support.py

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier


class DecisionSupportSystem:
    def __init__(self, features, labels):
        """
        features: pandas DataFrame, 训练数据的特征部分。
        labels: list, 目标标签列表。
        """
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)
        # 将 DataFrame 转换为 NumPy 数组，以避免特征名称问题
        X = features.values if hasattr(features, 'values') else np.array(features)
        self.model.fit(X, labels)
        # 如果 features 是 DataFrame，则保存其列名用于后续预测时保持特征顺序一致
        self.feature_names = list(features.columns) if hasattr(features, 'columns') else None
        self.labels = labels

    def generate_recommendation(self, user_data):
        """
        user_data: dict，包含与训练时相同特征名称和顺序的键值对。
        返回预测的标签（例如 'History'）。
        """
        # 若保存了特征名，则使用 DataFrame 保持一致性
        if self.feature_names:
            X_new = pd.DataFrame([user_data], columns=self.feature_names)
            X_new_array = X_new.values
        else:
            # 假设 user_data 已经是按正确顺序排列的字典，则转换为列表
            X_new_array = np.array([list(user_data.values())])

        # 进行预测，返回的是 NumPy 数组
        prediction = self.model.predict(X_new_array)[0]

        # 将 NumPy 标量转换为 Python 标量，处理 numpy.str_ 或 numpy.int64 类型
        if isinstance(prediction, np.generic):
            prediction = prediction.item()

        # 如果预测结果为字符串，则在 labels 列表中查找其索引；否则直接转换为整数
        if isinstance(prediction, str):
            try:
                pred_index = self.labels.index(prediction)
            except ValueError:
                raise ValueError(f"Predicted label '{prediction}' not found in labels list.")
        else:
            pred_index = int(prediction)

        # 返回预测结果对应的标签
        return self.labels[pred_index]
