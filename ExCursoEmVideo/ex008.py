#Desenvolva um programa que leia uma distância em metros e mostre os valores
#relativos em outras medidas.
#Ex:
#Digite uma distância em metros: 185.72
#A distância de 85.7m corresponde a:
#0.18572Km
#1.8572Hm
#18.572Dam
#1857.2dm
#18572.0cm
#185720.0mm

print('        CONVERSOR DE MEDIDAS/metro\n            ')

metro = float(input('Digite uma distancia em metros: '))
print('A distancia de {}m corresponde a:')

km = metro/1000
hm = metro/100
dam = metro/10
dm = metro*10
cm = metro*100
mm = metro*1000

print('{} Km\n{} Hm \n{} Dam \n{} Dm \n{} Cm \n{} Mm'.format(km,hm,dam,dm,cm,mm))

