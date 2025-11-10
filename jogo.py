import random
from os import system, name


#Função para limpar a tela a cada execução
def limpa_tela():
  #Windows
  if name == 'nt':
    _=system('cls')


#Função que desenha a forca na tela
def display_hangman(chance):

  #Lista de estágios da forca
  stages = [ #Estagio 6 (final)
            """
              _____________
             |            |
             |            0
             |           \\|/
             |            |
             |           / \\
             |
           """,

             #Estagio 5
             """
              _____________
             |            |
             |            0
             |           \\|/
             |            |
             |           /
             |
           """,
             #Estagio 4
             """
              _____________
             |            |
             |            0
             |           \\|/
             |            |
             |
             |
           """,
             #Estagio 3
             """
              _____________
             |            |
             |            0
             |           \\|
             |            |
             |
             |
           """,
             #Estágio 2
             """
              _____________
             |            |
             |            0
             |            |
             |            |
             |
             |
           """,
             #Estágio 1
             """
              _____________
             |            |
             |            0
             |
             |
             |
             |
           """,
             #Estágio 0
             """
              _____________
             |            |
             |
             |
             |
             |
             |
           """
  ]
  return stages[chance]


#Função do Jogo
def game():
  limpa_tela()

  print("Bem-vindo(a) ao jogo da forca! \n")
  print("Adivinhe a palavra abaixo: \n")

  palavras = ['abacate', 'banana', 'laranja', 'melancia', 'morango']

  #Escolhe randomicamente uma palavra
  palavra = random.choice(palavras)

  #List Comprehension
  letras_descobertas = ['_' for letra in palavra]

  #Número de chance
  chance = 6

  #Letras que errou
  letras_erradas = []

  # Exibe o primeiro desenho (vazio)
  print(display_hangman(chance))

  #Loop enquanto o número de chances for maior do que zero
  while chance > 0:
    #Join faz uma junção do que está no lado esq. com o lado direito ele vai juntar os espaços com as letras descobertas
    print(" ".join(letras_descobertas))
    print("\n Chances restantes: ", chance)
    print("Letras erradas:", " ".join(letras_erradas))

    tentativa = input("\nDigite uma letra: ").lower()

    if tentativa in palavra:
      index = 0

      for letra in palavra:
        if tentativa == letra:
          letras_descobertas[index] = letra
        index += 1

    else:
      chance -= 1
      letras_erradas.append(tentativa)

    limpa_tela()    
    print(display_hangman(chance)) 
      
      
    #Condicional- Se tiver completado todas as letras da palavra
    if "_" not in letras_descobertas:
      print("Você venceu, a palavra era: ", palavra)
      break

  #Condicional de depois que acabou o loop while, e não completou a palavra
  if "_" in letras_descobertas:
    print("Você perdeu, a palavra era: ", palavra)

#Bloco main
#Para dizer ao interpretador que este é um módulo Python, é um programa Python
if __name__ == "__main__":
   while True:
        game()
        again = input("\nQuer jogar novamente? (sim/nao): ").lower()
        if again != 'sim':
            print("\nObrigado por jogar! Até a próxima!")
            break
        else:
            limpa_tela()
            chances=6

