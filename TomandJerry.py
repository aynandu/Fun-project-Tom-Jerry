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
        
        if random.choice(option_for_toss) == self.choose:
            toss_won_opt = input("You won the toss,choose \"1\" for Bat first \"2\" for not : ")
            
            if toss_won_opt== '1':
                print("You Choose to bat")
                batting()  
                    
                
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
    def __init__(self,score,no_of_balls,wickets):
       self.no_of_balls= no_of_balls = 6
       self.score=score=0
       self.wicket = wickets= 0
       
    def batting_card(self):
       values = (1,2,3,4,5,6)
       i =0
       while self.wicket<2 and  i < self.no_of_balls:
            Batting_value =  int(input("enter value btw 6 : "))
            computer_value = random.choice(values)
            if Batting_value in values :
                if Batting_value!= computer_value:
                    temp = Batting_value 
                    self.score+=temp
                    print(f'runs : {self.score}/{self.wicket} , balls {i}')
                   
                else:
                    wicket +=1
                    print("wicket!")
                    
            else:
                
                print("out of range")
            i+=1
            return self.score

class bowling():
     pass


class scoreboard(batting):
    def __init__(self,score1):
        self.score1=batting
        print()
        

class fall_of_wickets():
    pass

class result():
    pass

toss_input = toss(input("Enter a Input : "))
toss_input.toss_time()