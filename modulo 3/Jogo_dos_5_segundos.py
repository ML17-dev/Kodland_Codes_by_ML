import time 

print('Bem-vindo ao jogo da "regra dos 5 segundos"!') 
time.sleep(1) 
print('Aqui estão as regras:') 
print('O programa fará uma pergunta e você tem 5 segundos para pensar em uma resposta') 
time.sleep(2) 
print('Pergunta 1') 
time.sleep(1) 
print('Quem era o personagem principal do desenho do Incrivel Mundo de Gumball?') 
time.sleep(2) 
print('A: Gumball') 
print('B: Banana Joe') 
print('1') 
time.sleep(1) 
print('2') 
time.sleep(1) 
print('3') 
time.sleep(1) 
print('4') 
time.sleep(1) 
print('5') 
time.sleep(1) 
q1 = input('Qual é a sua resposta? (A ou B)') 

if q1 == 'a':
    print('Sua resposta está correta!')

else:
    print('Sua resposta está errada! A resposta correta era: A')
