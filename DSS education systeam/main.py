from src.user_input import UserInput
from src.data_processing import DataProcessing
from src.decision_support import DecisionSupportSystem
from src.learning_tracker import LearningTracker
from src.visualization import Visualization


def main():
    # 加载用户输入
    user_input = UserInput()
    sample_data = user_input.load_sample_input('/Users/Chenxu/DSS education systeam/ data/sample_input.csv')

    # 数据处理
    data_processor = DataProcessing(sample_data)
    clean_data = data_processor.clean_data()
    features = data_processor.feature_extraction()

    # 假设标签是学习推荐的学科
    labels = ['Math', 'Physics', 'History', 'Chemistry']

    # 决策支持系统
    dss = DecisionSupportSystem(features, labels)
    user_data = [1, 2, 0]  # 示例用户输入的数据
    recommendation = dss.generate_recommendation(user_data)
    print(f"Recommended subject for further study: {recommendation}")

    # 学习进度追踪
    tracker = LearningTracker()
    tracker.track_progress('User A', 85)
    tracker.track_progress('User B', 70)
    print(tracker.get_progress('User A'))

    # 数据可视化
    visualization = Visualization()
    learners = ['User A', 'User B', 'User C', 'User D']
    progress = [85, 70, 78, 90]
    visualization.plot_learning_progress(learners, progress)


if __name__ == "__main__":
    main()
