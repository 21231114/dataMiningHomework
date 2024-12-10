import pandas as pd

# 读取CSV文件
file_path = './data/road.csv'
data = pd.read_csv(file_path)

# 初始化road数组
road = []

# 遍历每一行数据并提取所需信息
for index, row in data.iterrows():
    road_segment = {
        's_lon': row['s_lon'],
        's_lat': row['s_lat'],
        'e_lon': row['e_lon'],
        'e_lat': row['e_lat'],
        'maxspeed': row['maxspeed']
    }
    road.append(road_segment)

# 输出road数组
print(road)