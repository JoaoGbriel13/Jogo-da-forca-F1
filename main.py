import random
from animaçoes import stages
from f1 import word_list
from replit import clear

#lista de palavras

#palavra aleatoria:
palavra = random.choice(word_list)
palavrac = (palavra).lower()


#vidas
vidas = 6


#display:
display = []
for l in palavrac:
 display += "_"



ap = input(
'Bem vindo ao Jogo da forca da F1, nesse jogo você deve advinhar as letras que componhe a palavra final que pode ser um piloto campeão mundial de F1 ou uma equipe que faz ou fez parte do grid,pressione qualquer tecla para iniciar.'
)   
#loop
fdj = False
while not fdj:
    
 #escolha do palpite:
    palpite = input('Escolha uma letra e verifique se ela está na palavra:\n').lower()

    clear()

#palpite existente:
    if palpite in display:
       print(f'Você já usou {palpite}, tente outra letra.')

#palpite correto:
    for p in range(len(palavrac)):
        let = palavrac[p]
        if palpite == let:
            display[p] = let
        elif let == ' ':
            display[p] = ' '

           
 

 #palpite errado:
    if palpite not in palavrac:
        print('Essa letra não está na palavra, você perdeu uma vida.')
        vidas -= 1 
        if vidas == 0:
            fdj = True
            print(f'Você perdeu, a palavra era: {palavra}')
    

        
    print(f"{' '.join(display)}")
    
  
 #fim do jogo:
    
    if "_" not in display:
        fdj = True
        print(f'A palavra é : {palavra}, você venceu.')
    
    print(stages[vidas])
   