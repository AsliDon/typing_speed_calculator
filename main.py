from time import*
import random as r

def mistake(partest,usertest):
    error=0
    for i in range(len(partest)):
        try:
            if partest[i]!= usertest[i]:
                error+=1

        except:
            error+=1
    return error

def speed_time(time_s,time_e,userinput):
    time_delay = time_e - time_s
    time_R = round(time_delay,2)
    speed = len(userinput)/ time_R
    return round(speed)

while True:
    
    ck = input("ready to type(yes / no) : ")
    if ck=="yes":
        test=["A paragraph has been set to test the typing speed of the user",
              "my name is sahil","Welcome to my python project"]
        test1= r.choice(test)
        print("            ********** typing speed calculator **********")
        print(test1)
        print()
        print()
        time_1=time()
        testinput=input("Enter : ")
        time_2= time()

        print('speed:', speed_time(time_1,time_2,testinput),"w/sec")
        print("error: " , mistake(test1,testinput))
    elif ck== "no":
        print("thank you")
        break
    else:
        print ("wrong input")
        




