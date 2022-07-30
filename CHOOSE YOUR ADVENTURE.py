answer = input('Are you ready to begin your adventure ')
if answer == 'yes':
  answer1 = input('You find yourself in front of a mention you can enter from the front gate,from a broken door in the'
                  ' back of the mention or leave, what do you chose? (front gate,back door,leave) ')
  if answer1 == 'front gate':
      answer2 = input('You enter from the front gate and see a sign on which is written`if you want to pass you have to'
                      ' pay 6 crow feathers`.What do you choose (look for feathers,go without paying,leave) ')
      if answer2 == 'look for feathers':
          answer3 = input('You find 6 feathers and leave them next to the sign.You see an elevator which goes to the'
                          ' basement and the top floor.Where do you go (top floor,basement,leave) ')
          if answer3 == 'top floor':
              answer4 = input('You go to the top floor and there you see an ork with a giant axe. Do you chose to fight'
                              ' him or leave ')
              if answer4 == 'fight him':
                  answer5 = input('What do you choose to fight him with(sword,crossbow) ')
                  if answer5 == 'sword':
                      print('Your sword is to small and does no damage to the ork so you died ')
                      quit()
                  elif answer5 == 'crossbow':
                      print('You shot him with the crossbow once but while reloading the ork caught you and killed you ')
                      quit()
              if answer4 == 'leave':
                  quit()
          elif answer3 == 'basement':
              answer4=input('You go to the basement and see a painting do you steal it or leave ')
              if answer4 == 'steal it':
                  answer5 = input('You steal the painting and go back home (Do you give the painting to a museum or'
                                  ' keep it to yourself) ')
                  if answer5 == 'keep it to yourself':
                      print("You keep it to yourself and after 80 years after you have died the painting has been"
                            " valued""for 1000000000$ but you don't have kids so the painting remains unfound ")
                      quit()
                  elif answer5 == 'give the painting to a museum':
                      print('You give the painting to a museum and they reward you with 1000000$')
                      quit()
              elif answer4 == 'leave':
                  quit()
          elif answer3 == 'leave':
              quit()
      elif answer2 == 'go without paying':
          print('You go without paying and in front of you appears a men with a mask who kills you')
          quit()
      elif answer2 == 'leave':
          quit()
  elif answer1 == 'back door':
      answer2 = input('You go through the back door and find yourself in a maze (do you go left, right or leave) ')
      if answer2 == 'left':
          answer3 = input('Now do you go left, right or do you leave ')
          if answer3 == 'left':
              answer4=input('Now do you go left, right or do you leave ')
              if answer4 == 'left':
                  print('You went left and fall in a endless pit and died ')
                  quit()
              elif answer4 == 'right':
                  answer5 = input('You went right and found a Minotaur with a giant hammer '
                                  '(do you fight him or do you leave) ')
                  if answer5 == 'fight him':
                      answer6 = input('What do you fight him with (axe or machete) ')
                      if answer6 == 'axe':
                          answer7 = input('You cut the Minotaur`s head off do you leave or continue with the maze ')
                          if answer7 == 'continue with the maze':
                              answer8 = input('You see a men who tels you that if you want to continue you have to '
                                              'give him the Minotaur`s head(do you give him the head or not) ')
                              if answer8 == 'give him the head':
                                  print('You give him the head and he gives you whatever you want so for the rest'
                                        ' of your live you have everything')
                              elif answer8 == 'don`t give him the head':
                                  print('You don`t` give him the head so he kill`s you')
                                  quit()
                          elif answer7 == 'leave':
                              quit()
                      elif answer6 == 'machete':
                          answer7 = input('You killed the Minotaur now do you continue with the maze or leave ')
                          if answer7 == 'continue with the maze':
                              print('You see a men who tels you that if you want to continue you have to give him'
                                    ' the Minotaur`s head.How ever you can`t cut the Minotaur`s head so you are kicked'
                                    ' ot of the mention')
                              quit()
                          elif answer7 == 'leave':
                              quit()
                  elif answer5 == 'leave':
                      quit()
              elif answer4 == 'leave':
                  quit()
          elif answer3 == 'right':
              print('You go right and all of a sudden you find yourself trap in the maze and starve to death')
              quit()
          elif answer3 == 'leave':
              quit()
      elif answer2 == 'right':
          print('You go right and fall in lava and die')
          quit()
      elif answer2 == 'leave':
          quit()
  elif answer1 == 'leave':
      quit()
elif answer == 'no':
    quit()
