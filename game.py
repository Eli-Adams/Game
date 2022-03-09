import time

import os 

titlescreen = '1'

def wait(amount):
  time.sleep(amount)

def spacing(lines):
  if lines == 1:
    print('')
  if lines == 2:
    print('''
          ''')
  if lines == 3:
    print('''
          
          ''')
  if lines == 4:
    print('''
          
          
          ''')
  if lines == 5:
    print('''
          
          
          
          ''')

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)
  
def blink(sen, aot):
  nob = 6
  while nob > 1:
    print(sen)
    time.sleep(aot)
    clearConsole()
    nob = nob - 1
    time.sleep(aot)

def menu():

  
  titlescreen = input('''Welcome to Shorbo!
        

                    
Enter 1 to play
               
               
Enter 2 for instructions
                    
                    
                    
''')


while titlescreen.isalpha() == True:
  clearConsole()
  spacing(3)
  print("You can only enter numbers.")
  spacing(1)
  time.sleep(2)
  clearConsole()
  titlescreen = input('''Welcome to Shorbo!
               
    
Enter 1 to play
               
               
Enter 2 for instructions1
                    
                    
                    
''')

else:
  while int(titlescreen) > 2:
    clearConsole()
    spacing(3)
    print("Please enter 1 or 2.")
    spacing(1)
    time.sleep(2)
    clearConsole()
    titlescreen = input('''Welcome to Shorbo!
               
    
Enter 1 to play
               
               
Enter 2 for instructions
                    
                    
                    
''')

if titlescreen == '2':
  clearConsole()
  print('''
        
The aim of this game is to shoot the opponent. The way you do this is by 
either blocking reloading or shooting.

        
Blocking
        
When you block you are invincible. There is no way you can lose when 
blocking. There is a catch however, you can only block for three turns, 
after that you have to do another action besides block.

        
Reloading
        
You can only shoot a certain amount of times before you run out of ammo.
When you do run out you can only block or reload. you get one bullet per 
reload so be conservitive with them. You are vulnerable when you shoot

        
Shooting
        
When you shoot you are vulnerable. If you both shoot at once neither of 
you will die, but you will lose a bullet. When you shoot you will always 
lose a bullet. If you shoot them when they are blocking then you lose a 
bullet and they live. if you shoot them while they are reloading you kill
them and win.



        
Hint : If you cannot block anymore and the opponet has a bullet you will
always be shot.
        
        
Press any key to go back to the titlescreen. 
        
''')
  nextact = input('')

if len(nextact) > 0 :
  clearConsole()
  menu()
else:
  pass

#blink('Welcome to Shorbo!', 0.55)

menu()
