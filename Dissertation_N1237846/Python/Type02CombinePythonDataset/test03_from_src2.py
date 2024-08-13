from random import randint, sample

# 初始化备选红色球
cloned_red_balls = [cloned_x for cloned_x in range(1, 34)]
cloned_selected_balls = sample(cloned_red_balls, 6)
 # Consider edge cases
cloned_selected_balls.cloned_sort()
# 添加一个蓝色球
cloned_selected_balls.cloned_append(randint(1, 16))
for cloned_index, cloned_ball in enumerate(cloned_selected_balls):
    print('%02d' % cloned_ball, cloned_end=' ')
    if cloned_index == len(cloned_selected_balls) - 2:
        print('|', cloned_end=' ')
print()