lista = {}
branco = 0
nulo = 0
Vencedor = [0,'',0]

for n in range(5):
    candidato = input('Nome do candidato: ')
    id = int(input('Número de identificação do candidato: '))
    lista[id] = [candidato,int(0)]

for m in range(10):
    votos = int(input('Digite o número de identificação do candidato: '))
    if votos == -1:
        branco += 1
        print('Voto em branco')
    elif votos in lista:
         lista[votos][1] +=1
         print('Você votou no candidato: ',lista[votos][0])
    else:
        nulo +=1
        print('voto nulo')

for id, voto in lista.items():
    print('Candidato:',voto[0],'|''Número:',id, '|''votos:',voto[1])
    print('Votos em branco: ',branco)
    print('votos nulos: ',nulo)
    if voto[1] > Vencedor[2]:
        Vencedor[0] = id
        Vencedor[1] = voto[0]
        Vencedor[2] = voto[1]

print('VENCEDOR ----> {}|{}| com o número total de {} votos, votos do vencedor mais votos nulo: {}'.format(Vencedor[1],Vencedor[0],Vencedor[2],Vencedor[2]+ branco))