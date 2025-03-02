# src/visualization.py

import matplotlib.pyplot as plt
import matplotlib as mpl

class Visualization:
    def __init__(self):
        pass

    def plot_learning_progress(self, learners, progress):
        """
        learners: list[str] - 学习者名称
        progress: list[int] - 对应的学习进度或分数
        """

        # 1. 设置全局 rcParams, 提高分辨率, 加大字体
        mpl.rcParams.update({
            'figure.figsize': (12, 8),     # 图表尺寸(宽, 高), 单位英寸
            'figure.dpi': 300,            # 在屏幕上显示时的分辨率
            'savefig.dpi': 300,           # 保存图像时的分辨率
            'font.size': 18,              # 全局字体大小
            'axes.labelsize': 20,         # 坐标轴标签字体
            'axes.titlesize': 24,         # 标题字体
            'xtick.labelsize': 16,        # x轴刻度字体
            'ytick.labelsize': 16,        # y轴刻度字体
            'figure.facecolor': 'white',  # 图表背景为白色
            'axes.facecolor': 'white'     # 坐标轴背景为白色
        })

        # 2. 创建图表 (因为我们已经通过 rcParams 设置了 figsize 和 dpi, 不必再 plt.figure() 中重复)
        plt.figure()

        # 3. 绘制柱状图，使用更鲜明的颜色和黑色边框
        bars = plt.bar(learners, progress, color='dodgerblue', edgecolor='black')

        # 4. 设置标题与坐标轴标签
        plt.title('Learning Progress of Students', color='black')
        plt.xlabel('Learners', color='black')
        plt.ylabel('Progress (%)', color='black')
        plt.ylim(0, 100)  # 假设进度在 0~100

        # 5. 在每个柱子上方显示具体数值
        for i, bar in enumerate(bars):
            height = bar.get_height()
            plt.text(
                bar.get_x() + bar.get_width() / 2,
                height + 1,
                f'{progress[i]}%',
                ha='center',
                va='bottom',
                color='black',
                fontsize=16
            )

        # 6. 添加横向网格线
        plt.grid(axis='y', color='gray', linestyle='--', linewidth=0.5, alpha=0.7)

        # 7. 保存图像到 PNG 文件，建议在外部查看器中打开
        plt.savefig('learning_progress.png', bbox_inches='tight')
        print("图表已保存为 'learning_progress.png'，请在外部查看器中打开查看原始清晰度。")

        # 8. 如果仍想在当前环境弹窗显示，也可以 plt.show()
        plt.show()
