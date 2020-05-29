# 分開取出留言者的姓名

lines = []
with open('3.txt', 'r', encoding='utf-8-sig') as f: 
    for line in f:
        lines.append(line.strip()) #把換行符號去除

for line in lines:
    s = line.split(' ')
    time = s[0][:5]
    name = s[0][5:]
    print(time, name)
