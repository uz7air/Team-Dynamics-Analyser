import time
import webbrowser
import matplotlib.pyplot as py

class temp:
    def __init__(self,choice):
        self.choice = choice
    def get_name(self):
        return self.choice
    def choose(self):
        cost = [0,0,0,0,0]#4,6,2,8
        lis = [0,0,0,0,0]
        x = self.choice
        
        while(1):
            if(x == '1'):
                tem = 1
                print("   Available teams are:\n   1. Team 1 with 2y exp\n   2. Team 2 with 4y exp\n   3. Team 3 with 1y exp\n   4. Team 4 with 4y exp\n   5. Exit\n   (Think before you select the team)")
                ch = int(input("   Select Team (Enter only numbers): "))
                print("\n")
                break
            elif(x == '2'):
                tem = 1
                print("   Available teams are:\n   1. Team 1 with 2y exp\n   2. Team 2 with 4y exp\n   3. Team 3 with 1y exp\n   4. Team 4 with 4y exp\n   5. Exit\n   (Think before you select the team)")
                ch = int(input("   Select Team (Enter only numbers): "))
                print("\n")
                break
            elif(x =='3'):
                tem = 1
                print("   Available teams are:\n   1. Team 1 with 2y exp\n   2. Team 2 with 4y exp\n   3. Team 3 with 1y exp\n   4. Team 4 with 4y exp\n   5. Exit\n   (Think before you select the team)")
                ch = int(input("   Select Team (Enter only numbers): "))
                print("\n")
                break
            elif(x == '4'):
                tem = 1
                print("   Available teams are:\n   1. Team 1 with 2y exp\n   2. Team 2 with 4y exp\n   3. Team 3 with 1y exp\n   4. Team 4 with 4y exp\n   5. Exit\n   (Think before you select the team)")
                ch = int(input("   Select Team (Enter only numbers): "))
                print("\n")
                break
            elif(x == '5'):
                break
            else:
                print("   Invalid choice: ",x,"\nTry again...")
        while(1):
            if(tem == 1):
                if(ch == 1):
                    cost[1] = 400
                    print(f"   Selected team is {ch} and cost is {cost[ch]}")
                    lis[1] = 1
                    break
                elif(ch == 2):
                    cost[2] = 600
                    print(f"   Selected team is {ch} and cost is {cost[ch]}")
                    lis[2] = 1
                    break
                elif(ch == 3):
                    cost[3] = 200
                    print(f"   Selected team is {ch} and cost is {cost[ch]}")
                    lis[3] = 1
                    break
                elif(ch == 4):
                    cost[4] = 800
                    print(f"   Selected team is {ch} and cost is {cost[ch]}")
                    lis[4] = 1
                    break
                elif(x == 5):
                    break
                else:
                    print("   Invalid chioce...Try again...")
        #Bill
        total = sum(cost)
        gst = 80.46
        if(total == 0):
            print("   Thank you...Visit again.")
        else:
            t = float(total)
            print("   Cost is: ",t)
            print("   GST is: ",gst)
            print("   Total Amount = ",(t+gst),"\n")
            
            #Payment
            print("   Directing to Browser...Please wait 10 sec")
            for i in range(11):
                time.sleep(1)
                print("   Seconds remaining: ",i)    
            pay_link = 'https://paypal.me/saimaster8660'
            webbrowser.open(pay_link)
            
#Graph
x = [1,2,3,4]
y = [2,4,1,4]
py.plot(x,y,color = '#7deb34',ls = '-.',marker = '*')
py.xlabel("Teams")
py.ylabel("Experience in y")
py.title("Team Dynamics Analyser.")
for i in range(len(x)):
    py.text(x[i],y[i],(x[i],y[i]))
py.show()

#Main   
print("---------------------------------------")
print("   Welcome to Master's organisation    ")
print("---------------------------------------")
print("   The projects available are:\n\n   1. Password checking\n   2. Lift Scenario\n   3. Chatbox\n   4. ATM\n   5. Exit")
choice = input("   Enter your choice: ")
print("\n")       
temp = temp(choice)
temp.choose()
