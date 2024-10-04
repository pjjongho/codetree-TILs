score = list(map(float,input().split()))
n = len(score)
avg_score = sum(score)/n
print(f'{avg_score:.1f}')