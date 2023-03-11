import random
class game():
   pass 

class content():
    print ("Tom & Jerry - Ver 1.0")

class toss():
    print("Choose \"1\" for Head , \"2\" for Tail")
    def __init__(self,choose):
        self.choose=choose
        
    def toss_time(self):
        option_for_toss = ('1','2')
        print(random.choice(option_for_toss))
        i=1
        while i==1:
            if random.choice(option_for_toss) == self.choose:
                toss_won_opt = input("You won the toss,choose \"1\" for Bat first \"2\" for not : ")
            
                if toss_won_opt== '1':
                    print("You Choose to bat")
                    batting()  
                    break
                
                elif toss_won_opt=='2':
                    print("You Choose to Bowl")
                    bowling()
                    
                else:
                    self.choose= input("Please Choose \"1\" for Batting , \"2\" for Bowling: ")
                    #toss_input.toss_time()
                        #not looping..
            elif  self.choose not in option_for_toss:
                print("Please Choose \"1\" for Head , \"2\" for Tail") 
                                
            else:
                if random.choice(option_for_toss)=='1':
                        print("Computer has Choose to bat")
                        batting()  
                else :
                        print("Computer has Choose to Bowl")
                        bowling()

class playerdetails():
    pass

class Computer_Player():
    pass

class batting():
    pass

class bowling():
     pass


class scoreboard():
    pass

class fall_of_wickets():
    pass

class result():
    pass

toss_input = toss(input("Enter a Input : "))
toss_input.toss_time()