#Programmers: Leo Kopec
#Course: CS151, Prof. Mehri
#Date: September 23, 2021
#Lab Number: #1
#Program Inputs: volume_mL
#Program Outputs: table_spoon, tea_spoon



#Start
#volume_mL:float
#tea_spoon:int
#table_spoon:int
#tea_spoon = volume_mL // 5
#table_spoon = tea_spoon // 3
#adjust tea_spoon
#input: "Enter a volume in mL:", volume_mL
#output: "table spoons =", table_spoon, "tea spoons =", tea_spoons
#End

volume_mL = float(input("Enter a volume in mL: "))
#print(volume_mL)
tea_spoon = int(volume_mL/5)
#print(tea_spoon)
table_spoon = int(tea_spoon/3)
#print(table_spoon)
tea_spoon = tea_spoon - (table_spoon * 3)
#print(tea_spoon)
print("table spoons =", table_spoon, "tea spoons =", tea_spoon)