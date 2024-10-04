n = int(input())
score = list(map(float,input().split()))
avg_score = sum(score)/n
print(f'{avg_score:.1f}')
if avg_score >= 4.0:
    print('Perfect')
if avg_score >= 3.0:
    print('Good') 
else:
    print('Poor')