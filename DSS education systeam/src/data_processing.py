import pandas as pd
from sklearn.preprocessing import LabelEncoder

class DataProcessing:
    def __init__(self, data):
        self.data = pd.DataFrame(data)
        self.cleaned_data = None

    def clean_data(self):
        # 清理数据，去除缺失值
        self.cleaned_data = self.data.dropna()
        return self.cleaned_data

    def feature_extraction(self):
        # 将分类数据转换为数值型数据
        le = LabelEncoder()
        self.cleaned_data['goal'] = le.fit_transform(self.cleaned_data['goal'])
        self.cleaned_data['problem'] = le.fit_transform(self.cleaned_data['problem'])
        self.cleaned_data['feedback'] = le.fit_transform(self.cleaned_data['feedback'])
        return self.cleaned_data
