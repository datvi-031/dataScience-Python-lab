# CS20B1031 -Daathwinaagh
# Lab 8: DIABETES DATA AND PROBABLITY COMPUTATION
import pandas as pd

def displayOptions2():
	print("\n----- COMPUTE DIABETES PROBABLITY BASED ON AGE -----")
	print("choose '1' for probability of diabetes Age above 50")
	print("choose '2' for probability of diabetes Age between 40 and 50")
	print("choose '3' for probability of diabetes Age between 30 and 40")
	print("choose '4' for probability of diabetes Age below 30")
	print("choose '5' for exit")

def displayOptions():
	print("\n----- DIABETES DATA COMPUTATION -----")
	print("CHOOSE '1' for finding probability of diabetes.")
	print("CHOOSE '2' for finding the probability of diabetes with \n\t > a glucose level of more than 120\n\t > blood pressure of more than 90\n\t > skin thickness of more than 30\n\t > insulin above 150\n\t > BMI above 25.")
	print("CHOOSE '3' for Exit")

def age_above_50(allDiabetic, df):
	"""probability of diabetes Age above 50"""
	num_age_above_50 = len(df[df["Age"]>50])
	ageAbove_50_diabetic = allDiabetic[allDiabetic["Age"]>50]
	num_ageAbove_50_diabetic = len(ageAbove_50_diabetic)
	p_ageAbove_50_diabetic = num_ageAbove_50_diabetic/num_age_above_50
	print("Probablity of diabetes with (age > 50) : {}".format(p_ageAbove_50_diabetic))

def ageBetween_40_50(allDiabetic, df):
	"""probability of diabetes Age between 40 and 50"""
	num_between_40_50 = len(df[(df["Age"]>=40) & (df["Age"]<=50)])
	ageBetween_40_50_diabetic = allDiabetic[(allDiabetic["Age"]>=40) & (allDiabetic["Age"]<=50)]
	num_ageBetween_40_50_diabetic = len(ageBetween_40_50_diabetic)
	p_ageBetween_40_50_diabetic = num_ageBetween_40_50_diabetic/num_between_40_50
	print("Probablity of diabetes with (40<= age <=50) : {}".format(p_ageBetween_40_50_diabetic))

def ageBetween_30_40(allDiabetic, df):
	"""c) probability of diabetes Age between 30 and 40"""
	num_between_30_40 = len(df[(df["Age"]>=30) & (df["Age"]<=40)])
	ageBetween_30_40_diabetic = allDiabetic[(allDiabetic["Age"]>=30) & (allDiabetic["Age"]<=40)]
	num_ageBetween_30_40_diabetic = len(ageBetween_30_40_diabetic)
	p_ageBetween_30_40_diabetic = num_ageBetween_30_40_diabetic/num_between_30_40
	print("Probablity of diabetes with (30<= age <=40) : {}".format(p_ageBetween_30_40_diabetic))

def age_below_30(allDiabetic, df):
	"""d) probability of diabetes Age less than 30"""
	num_below_30 = len(df[df["Age"]<30])
	ageLess_30_diabetic = allDiabetic[allDiabetic["Age"]<30]
	num_ageLess_30_diabetic = len(ageLess_30_diabetic)
	p_ageLess_30_diabetic = num_ageLess_30_diabetic/num_below_30
	print("Probablity of diabetes with (age < 30): {}".format(p_ageLess_30_diabetic))

def probDiabetes(df):
	"""Find the probability of diabetes given the dataset. Also, calculate the probability of diabetes given"""
	allDiabetic = df[df["Outcome"]==1]
	num_allDiabetic = len(allDiabetic)
	num_total = len(df)
	p_diabetic = num_allDiabetic/num_total
	print("Probablity of diabetes: {}".format(p_diabetic))

	a = True
	while a:
		displayOptions2()
		choice = int(input("Enter your choice: "))

		if choice == 1:
			age_above_50(allDiabetic, df)
		elif choice == 2:
			ageBetween_40_50(allDiabetic, df)
		elif choice == 3:
			ageBetween_30_40(allDiabetic, df)
		elif choice == 4:
			age_below_30(allDiabetic, df)
		elif choice == 5:
			a = False
		else:
			print("Wrong choice.. Try again")

def selection(df):
	"""Find the probability of diabetes with 
		a glucose level of more than 120 + 
		blood pressure of more than 90 + 
		skin thickness of more than 30 + 
		insulin above 150 + 
		BMI above 25 """

	allDiabetic = df[df["Outcome"]==1]
	total = df[
				(df["Glucose"]>120) & 
				(df["BloodPressure"]>90) & 
				(df["SkinThickness"]>30) & 
				(df["Insulin"]>150) & 
				(df["BMI"]>25)
	]
	df1 = allDiabetic[
				(allDiabetic["Glucose"]>120) & 
				(allDiabetic["BloodPressure"]>90) & 
				(allDiabetic["SkinThickness"]>30) & 
				(allDiabetic["Insulin"]>150) & 
				(allDiabetic["BMI"]>25)
	]
	prob = len(df1)/len(total)
	print("Probablity: {}".format(prob))

def main():
	df = pd.read_csv("diabetes.csv")
	
    # Dropping the unrequired column from the dataset ["Type"]
	df.drop(["Type"], axis=1, inplace=True)
	b = True
	while b:
		displayOptions()
		choice1 = int(input("Enter your choice: "))

		if choice1 == 1:
			probDiabetes(df)
		elif choice1 == 2:
			selection(df)
		elif choice1 == 3:
			b = False
		else:
			print("Wrong choice.. Try again")

if __name__ == '__main__':
	main()