text = input()
cost = len(text) * 40
rubles = cost // 100
kopecks = cost % 100
print(rubles, 'р.', kopecks, 'коп.')