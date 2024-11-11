from config import internlm_gen,client


for choice in internlm_gen("厦门市2021年绿色出行比例是多少"):
    print(choice.message.content) 
