'''Faça um programa que leia a largura e o comprimento de um terreno
retangular, calculando e mostrando a sua área em m². O programa também
devemostrar a classificação desse terreno, de acordo com a lista abaixo:
- Abaixo de 100m² = TERRENO POPULAR
- Entre 100m² e 500m² = TERRENO MASTER
- Acima de 500m² = TERRENO VIP'''

largura = float(input("Digite a largurado do terreno: "))
comprimento = float(input("Digite ocomprimento do terreno: "))
area = largura * comprimento

print("A área do seu terreno é de {}".format(area))

if area <= 100:
    print("Seu terreno é POPULAR!")
elif (area > 100) and (area <= 500):
    print("Seu terreno é MASTER")
else:
    print("Seu terreno é VIP!")