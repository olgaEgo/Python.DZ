# 5.2 Напишите программу, которая принимает на вход координаты двух точек и
# находит расстояние между ними в 3D пространстве.

xA = int(input('Введите xA: '))
yA = int(input('Введите yA: '))
zA = int(input('Введите xZ: '))
xB = int(input('Введите xB: '))
yB = int(input('Введите yB: '))
zB = int(input('Введите yZ: '))

distance = round(((xB - xA) ** 2 + (yB - yA) ** 2 +(zB - zA) ** 2) ** 0.5, 2)

print(f'Расстояние между точкой A({xA},{yA},{zA}) и точкой B({xB},{yB},{zB}) равно {distance}')
