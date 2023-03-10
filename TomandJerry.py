class game():
    print ("Tom & Jerry - Ver 1.0")
    

class toss():
    print("Choose \"1\" for Head , \"2\" for Tail")
    def __init__(self,choose):
        self.choose=choose
        
    def toss_time(self):
        y = 'head' 
        n  = 'tail' 
        while True:
            try:
                if self.choose== '1':
                    print("You Choose to bat")
                    batting()  
                elif self.choose=='2':
                    print("You Choose to Bowl")
                    bowling()
                else:
                    print("Please Choose \"1\" for Head , \"2\" for Tail")
                    continue   #not looping..
                
            except:
                print("Error!")
   
class playerdetails():
    pass

class Computer_Player():
    pass

class batting():
    print('You are opt to bat')

class bowling():
     print('You are opt to bowl')


class scoreboard():
    pass

class fall_of_wickets():
    pass

class result():
    pass

toss_input = toss(input())
toss_input.toss_time()