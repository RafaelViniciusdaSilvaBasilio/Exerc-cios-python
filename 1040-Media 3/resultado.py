N1,N2,N3,N4 = list(map(float,input().split()))
X = (((N1*2) + (N2*3) + (N3*4) + (N4*1)) /10);
print(f'Media: {X:.1f}')
if X >= 7.0:
    print("Aluno aprovado.")
elif X < 5.0:
    print("Aluno reprovado.")
if X >=5.0 and X <=6.9:
    print("Aluno em exame.")
    N5 = float(input())
    print(f'Nota do exame: {N5:.1f}')
    Y = ((X+N5)/2)
    if Y >=4.9:
        print("Aluno aprovado.")
    if Y <= 4.9:
        print("Aluno reprovado.")
    print(f'Media final: {Y:.1f}')