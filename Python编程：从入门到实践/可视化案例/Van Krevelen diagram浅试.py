"""
Van Krevelen图是在石油化工领域应用广泛的图表，用来描述碳和氢之间的相对含量关系。
"""

import numpy as np
import matplotlib.pyplot as plt

# 生成数据
carbon = np.arange(0, 1.01, 0.01)  # 碳含量
hydrogen = np.arange(0, 1.01, 0.01)  # 氢含量
oxygen = np.arange(0, 1.01, 0.01)  # 氧含量
plt.xlabel('C/H')
plt.ylabel('O/H')

# # 绘制Van Krevelen图
# for x in range(len(oxygen)):
#     plt.plot(carbon/hydrogen, oxygen[x]/hydrogen, color='black', linewidth=0.5)
#
# for y in range(len(carbon)):
#     plt.plot(carbon[y]/hydrogen, oxygen/hydrogen, color='black', linewidth=0.5)

# 绘制Van Krevelen图
X, Y = np.meshgrid(carbon/hydrogen, oxygen/hydrogen)
plt.plot(X.flatten(), Y.flatten(), color='black', linewidth=0.5)

# 在图表上绘制示例数据
example_data = [(0.2, 0.1, 0.7), (0.3, 0.2, 0.5), (0.1, 0.25, 0.65), (0.15, 0.35, 0.5), (0.35, 0.3, 0.35)]
colors = ['r', 'g', 'b', 'c', 'm']
for i in range(len(example_data)):
    plt.scatter(example_data[i][0]/example_data[i][1], example_data[i][2]/example_data[i][1], color=colors[i], s=50)

# 显示图表
plt.xlabel('C/H')
plt.ylabel('O/H')
plt.show()

