from random import choice


def Exercicio_ocioso():
    while True:
        resp = input(("Exercicio: [s] [n]: "))
        #if resp != "s" or "n":
                #print("Dumb ass mothefucker")
        if resp == "s":
            repetição = ['10', '15', '20']
            exercicio = ['Flexão', 'ABD', 'Prancha 1m', 'Agachamento', 'Sumo', 'Panturrilha']

            set_1 = choice(repetição)
            set_2 = choice(exercicio)
            geral = [set_1, set_2]
            print('~'*20)
            print(geral[1], geral[0])
            print('~'*20)
        
        elif resp == "n":
            print('Fim')
            break

    


Exercicio_ocioso()