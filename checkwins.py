import csv, time
from datetime import date, timedelta
import codecs
import us


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

if __name__ == "__main__":
	correctraces = 0
	dem = 0;
	rep = 0;
	false = 0;
	races = 0;
	with codecs.open("formapwithcorrect.csv", "r" ,encoding='utf-8', errors='ignore') as f:
		for row in csv.reader(f):
			#(self,year,state,district,status,percentage,party,name):
			if is_number(row[3]):
				races += 1
				
				if float(row[3]) > float(row[8]) and float(row[4]) > float(row[9]):
					correctraces += 1
					
				elif float(row[3]) < float(row[8]) and float(row[4]) < float(row[9]):
					correctraces += 1
				else:
					# print("actual1")
					# print(row[2])
					# print("actual2")
					# print(row[6])
					# print("perdicted1")
					# print(row[3])
					# print("predicted2")
					# print(row[7])
					false += 1;

				if float(row[4]) > float(row[9]):
					if row[2] == "D":
						dem+=1
					else:
						rep += 1
				elif float(row[4]) < float(row[9]):
					if row[7] == "D":
						dem+=1
					else:
						rep += 1
				else:
					print(float(row[4]))
					print(float(row[9]))
					print(row[2])
					print(row[7])
					print("what")

				# if float(row[6]) > 50 and float(row[7]) > 50:
				# 	correctraces += 1
				# if float(row[6]) < 50 and float(row[7]) < 50:
				# 	correctraces += 1

	print("correct races")
	print(correctraces)
	print("races")
	print(races)
	print("rep")
	print(rep)
	print("dem")
	print(dem)


