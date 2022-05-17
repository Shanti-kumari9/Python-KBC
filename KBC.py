name = input("ENTER THE YOUR NAME--")
print("Hi :)"+ name, "--WELCOME TO KBC GAME :)")

play = input("Do you want to play KBC Game (YES/NO) ").lower()

if play =="yes":
    print("\n apka question apki screen ke upar \n")

    question=["1. what is the capital of INDIA ","2. who's won first cricket wold cup ","3. how many times has INDIA won the ICC world cup ",
    "4.which is the national game in INDIA ","5. which is the national tree of india"]

    first_option=["1.Dehradun","1.England","1. three time","1. cricket","1. Mango Tree"]
    second_option=["2.Delhi","2.India","2. one time","2.hockey","2.Neem tree"]
    third_option=["3.Rajsthan","3. pakistan","3.two time","3.Base Ball","3.Ficus bengalensis"]
    forth_option=["4. Mumbai","4. Australia","4. Five time","4. Athletics","4.Banana tree"]

    ans_key=[2,1,3,2,3]

    i=0
    l=(len(question))
    lifeline=0

    life_line_1=["1.delhi","1.india","1.five time","1.cricket","1.ficus bengalenis"]
    life_line_2=["2.Dehradun","2.England","2.two time","Hockey","2.mango tree"]

    life_line_ans=[1,2,2,2,1]
    while i<l:
        print(question[i])
        print(first_option[i])
        print(second_option[i])
        print(third_option[i])
        print(forth_option[i])

        if lifeline<1:
            print("you wants life line so press -5050 ")


        user_answer=int(input("enter answer-- "))
    
        if user_answer==5050:
            if lifeline<1:
                print(life_line_1[i])
                print(life_line_2[i])

                life_line =int(input("\n choose your lifeline option-->"))
                if life_line==life_line_ans[i]:
                    print("\n your ans correct!!! :) \n")
                elif life_line!=life_line_ans[i]:
                    print("\n your ans wrong :(( \n")
                    break
                lifeline+=1
            else:
                print("\nYou already used lifeline 5050 :)\n ")
                print("\nSelect the your answer:) \n")
                i-=1


        
        elif user_answer==ans_key[i]:
            print("\nWow! your ans correct :) \n ")
        elif user_answer!=ans_key[i]:
            print("\nohh!! sad :( your ans wrong \n")
            break
        i+=1
else:
    print("\nTHANK YOU! \n")