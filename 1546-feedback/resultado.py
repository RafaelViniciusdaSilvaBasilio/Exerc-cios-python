membros = ['Rolien','Naej', 'Elehcim','Odranoel']
N = int(input())

for i in range(N):
    X = int(input())
    for i in range(X):
        feedback = int(input())
        print(membros[feedback-1])
