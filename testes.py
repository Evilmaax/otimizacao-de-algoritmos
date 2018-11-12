from math import sqrt

cidades_x = [0, 11003.611100, 11108.611100, 11133.333300, 11155.833300, 11183.333300, 11297.500000, 11310.277800,
             11416.666700, 11423.888900, 11438.333300, 11461.111100, 11485.555600, 11503.055600, 11511.388900,
             11522.222200, 11569.444400, 11583.333300, 11595.000000,
             11600.000000, 11690.555600, 11715.833300, 11751.111100, 11770.277800,
             11785.277800, 11822.777800, 11846.944400, 11963.055600, 11973.055600, 12058.333300, 12149.444400,
             12286.944400, 12300.000000, 12355.833300, 12363.333300, 12372.777800,
             12386.666700, 12421.666700, 12645.000000]

cidades_y = [0, 42102.500000, 42373.888900, 42885.833300, 42712.500000, 42933.333300, 42853.333300, 42929.444400,
             42983.333300, 43000.277800, 42057.222200, 43252.777800,
             43187.222200, 42855.277800, 42106.388900, 42841.944400, 43136.666700, 43150.000000, 43148.055600,
             43150.000000, 42686.666700, 41836.111100, 42814.444400, 42651.944400,
             42884.444400, 42673.611100, 42660.555600, 43290.555600, 43026.111100, 42195.555600, 42477.500000,
             43355.555600, 42433.333300, 43156.388900, 43189.166700, 42711.388900,
             43334.722200, 42895.555600, 42973.333300]

cidades_faltando = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
                    29, 30, 31, 32, 33, 34, 35, 36, 37, 38]
temp, cidade = 0, 0
ordem = [1]
controle = len(ordem)

y, distancia, z = 2, 0, 0

while controle >= 1:
    x = ordem[-1]
    while y <= 38:
        if y in ordem and len(ordem) == 1:
            print('skippei')
            y += 1
        else:
            distancia = sqrt((cidades_x[y] - cidades_x[x]) ** 2 + (cidades_y[y] - cidades_y[x]) ** 2)
            if distancia < temp or temp == 0:
                temp = distancia
                cidade = y
            print("----")
            print(f'foi {x} a {y}')
            print(f'Dist de {cidades_x[x]} a {cidades_y[y]} é de {distancia}')
            y += 1
    ordem.append(cidade)
    cidades_faltando.remove(cidade)

    print(temp)
    print(cidade)
    print(cidades_faltando)
    print(ordem)

    controle = len(ordem)

print(temp)
print(cidade)
print(cidades_faltando)
print(ordem)
