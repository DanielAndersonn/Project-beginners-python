import random 

while True:
    print('[Welcome Rock,Papper,Sissors Game]')
    print("[Make your choice]")
    print('[ROCK,PAPPER,SISSORS ?]')
    choices = input()
    choices.lower

    print("[USER CHOICE:] ",choices)
    
    choices = ['Rock ', ' Papper' , 'Sissiors']

    computer_choices = random.choices(choices)

    print('[CPU  CHOICE:] ', computer_choices )
    if choices in choices:
        if choices == computer_choices:
            print('[it is a tie ]')
        if choice  == ' Rock':
           
            if computer_choices == 'Papper':
                print('[ GAME OVER.TRY AGAIN ]')
            elif computer_choices == 'Sissors':
                print('[YOU WIN !!!] ')

        if choice  == 'Papper':
            
            if computer_choices == "Rock":
                 print('[ YOU WIN !!! ]')
            elif computer_choices =='Sissors':
                print('[GAME OVER.TRY AGAIN]')
                                              
        if choice == 'Sissors':
           
            if computer_choices =='Papper':
               print('[ YOU WIN !!!  ]')
            elif computer_choices =='Rock':
               print('GAME OVER.TRY AGAIN ')
    
else:
               print(' [Invalide operation ...]')

    




                
          


