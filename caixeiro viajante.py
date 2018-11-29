from math import sqrt

cidades_x = [0, 11003.611100, 11108.611100, 11133.333300, 11155.833300, 11183.333300, 11297.500000, 11310.277800,
             11416.666700, 11423.888900, 11438.333300, 11461.111100, 11485.555600, 11503.055600, 11511.388900,
             11522.222200, 11569.444400, 11583.333300, 11595.000000,
             11600.000000, 11690.555600, 11715.833300, 11751.111100, 11770.277800,
             11785.277800, 11822.777800, 11846.944400, 11963.055600, 11973.055600, 12058.333300, 12149.444400,
             12286.944400, 12300.000000, 12355.833300, 12363.333300, 12372.777800,
             12386.666700, 12421.666700, 12645.000000]   #Todas as distâncias do eixo X

cidades_y = [0, 42102.500000, 42373.888900, 42885.833300, 42712.500000, 42933.333300, 42853.333300, 42929.444400,
             42983.333300, 43000.277800, 42057.222200, 43252.777800,
             43187.222200, 42855.277800, 42106.388900, 42841.944400, 43136.666700, 43150.000000, 43148.055600,
             43150.000000, 42686.666700, 41836.111100, 42814.444400, 42651.944400,
             42884.444400, 42673.611100, 42660.555600, 43290.555600, 43026.111100, 42195.555600, 42477.500000,
             43355.555600, 42433.333300, 43156.388900, 43189.166700, 42711.388900,
             43334.722200, 42895.555600, 42973.333300]  #Todas as distâncias do eixo Y

cidades_faltando = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
                    29, 30, 31, 32, 33, 34, 35, 36, 37, 38]  #Lista de cidades pelas quais o caixeiro não passou

ordem, trajeto, controle = [1], 1, 1

print()
print('{:^80}'.format(' Algoritmo do Caixeiro Viajante - Maximiliano Meyer '))
print('-' * 80)
print('{:^5}{:^20}{:^25}{:^30}'.format('Trajeto', 'Cidade origem', 'Cidade destino', 'Distância'))
print('-' * 80)

while controle >= 1:                                        #Enquanto a lista de cidades faltando tiver mais que 1 item fica no while
    y = 2
    x, distancia, temp = ordem[-1], 0, 0                    #X recebe o último valor da lista "Ordem" e funcionará como cidade a qual as demais
                                                            #serão comparadas (variável Y no while abaixo)
    while y <= 38:
        if y in ordem and len(ordem) == 1 or y == x or y in ordem:   #Trata casos especiais como valor comparado já ordenado ou primeira execução
            y += 1
        else:
            temp = sqrt((cidades_x[y] - cidades_x[x]) ** 2 + (cidades_y[y] - cidades_y[x]) ** 2) #Calcula distância através da fórmula
            if temp < distancia or distancia == 0:          #Se a distância for menor do que a atual ou estiver zerada o programa
                distancia = temp                            #salva a cidade da verificação como a mais próxima até aqui
                cidade = y
            y += 1
    print('Nº{:^5}{:^15}{:^2}{:>15}{:^10}{:>15.3f} quilômetros'.format(trajeto, 'Cidade', x, 'Cidade', cidade, distancia))
    ordem.append(cidade)                                    #A cidade mais próxima na verificação é adicionada na lista de ordenados
    cidades_faltando.remove(cidade)                         #e removida da lista de cidades desordenadas
    controle = len(cidades_faltando)                        #variável de controle é atualizada para controle do while
    trajeto += 1

print()
print(f'A menor distância é através do caminho {ordem}')    #Printa o caminho final (a ordem dos nodos) obtido
