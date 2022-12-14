# 5.1 Напишите программу, которая принимает на вход координаты двух точек и
# находит расстояние между ними в 2D пространстве.
# Пример:
# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21

xA = int(input('Введите xA: '))
yA = int(input('Введите yA: '))
xB = int(input('Введите xB: '))
yB = int(input('Введите yB: '))

distance = round(((xB - xA) ** 2 + (yB - yA) ** 2) ** 0.5, 2)

print(f'Расстояние между точкой A({xA},{yA}) и точкой B({xB},{yB}) равно {distance}')
