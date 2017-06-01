import csv, time
from datetime import date, timedelta
import codecs
import us

us_state_abbrev = {
    'alabama': 'AL',
    'alaska': 'AK',
    'arizona': 'AZ',
    'arkansas': 'AR',
    'california': 'CA',
    'colorado': 'CO',
    'connecticut': 'CT',
    'delaware': 'DE',
    'florida': 'FL',
    'georgia': 'GA',
    'hawaii': 'HI',
    'idaho': 'ID',
    'illinois': 'IL',
    'indiana': 'IN',
    'iowa': 'IA',
    'kansas': 'KS',
    'kentucky': 'KY',
    'louisiana': 'LA',
    'maine': 'ME',
    'maryland': 'MD',
    'massachusetts': 'MA',
    'michigan': 'MI',
    'minnesota': 'MN',
    'mississippi': 'MS',
    'missouri': 'MO',
    'montana': 'MT',
    'nebraska': 'NE',
    'nevada': 'NV',
    'new hampshire': 'NH',
    'new jersey': 'NJ',
    'new mexico': 'NM',
    'new york': 'NY',
    'north carolina': 'NC',
    'north dakota': 'ND',
    'ohio': 'OH',
    'oklahoma': 'OK',
    'oregon': 'OR',
    'pennsylvania': 'PA',
    'rhode island': 'RI',
    'south carolina': 'SC',
    'south dakota': 'SD',
    'tennessee': 'TN',
    'texas': 'TX',
    'utah': 'UT',
    'vermont': 'VT',
    'virginia': 'VA',
    'washington': 'WA',
    'west virginia': 'WV',
    'wisconsin': 'WI',
    'wyoming': 'WY',
}



class Race(object):
    def __init__(self,year,state,district,status,percentage,party,name):
    	# if status == "N/A":
    	# 	return None
     #    if votes == "N/A":
     #    	return None
        self.year = year
        self.state = str.lower(state)
        self.district = district
        self.reportdistrict = newdistrict(state,district)
        self.status = status
        self.percentage = percentage
        self.win =  win(self.percentage)
        self.party = party
        self.memofpowerparty = ismemofpresidentsparty(self.year,self.party)
        self.name = name
        self.money = moneyspent(self.year,self.state,self.district,self.party)
        self.white = 0 #census3
        self.asian = 0 #census3
        self.black = 0 #census3
        self.hispanic = 0 #census3
        self.averageage = 0; #census3
        self.percentwithbachlors = bachlors(state,district) #row[243]
        self.income = 0 #census2
        self.homeownership = 0 #none
        self.personpersquaremile = 0 #none
        self.laborforceparticipation = 0 #census2
        self.unemployment = 0 #census2
        self.gasprices = gas(year)
        self.sp = sp(year)
        self.presapproal = approval(self.year,self.state);
    def __str__(self):
    	# "+ whtie: " + str(self.white) + '\n' + "labor: " + str(self.laborforceparticipation)
    	returnstring = str("Year: " +str(self.year)  + '\n' + "mem of power party: " + str(self.memofpowerparty) + '\n' + "district: " + str(self.district) + '\n' + "approval: " + str(self.presapproal) + '\n' + "party: " + str(self.party) + '\n')
    	return returnstring
def win(percentage):
	if float(percentage) > 50:
		return 'WIN'
	else:
		return "LOSS"
def ismemofpresidentsparty(year,party):
	if year is 2010 or 2012 or 2014 or 2016:
		if party == "D":
			return True
		else: 
			return False

def newdistrict(state,district):
	if state == "alaska" or state == "delaware" or state == "montana" or state == "north dakota" or state == "south dakota" or state == "vermont" or state == "wyoming":
		return 0
	else:
		return district

def approval(year,state):
	with codecs.open("approval.csv", "r" ,encoding='utf-8', errors='ignore') as f:
		for row in csv.reader(f):
			if str.lower(row[0]) == str.lower(state) and row[1] == year:
				return float(row[4][:-1])/100


def bachlors(state,district):
	with codecs.open("census2015/census1.csv", "r" ,encoding='utf-8', errors='ignore') as f:
		for row in csv.reader(f):
			if "Congressional" in row[2]:
				row_district = -1
				if is_number(str(row[2]).split()[2]):
				#if is_number(row[2]):
					row_district = row[2].split()[2]
				row_state = str.lower(row[2].split()[-1])
				#print("State: " + state + " district: " + str(district))
				#print("row State: " + row_state + "row district: " + str(row_district))
				if row_state == str.lower(state):
					#print("state----------")
					if row_district == district or row_district == -1:
						# print("-------------State: " + row_state + " district: " + str(row_district))
						# print(row[269])
						# print(round(float(row[269])/100,2))
						if (is_number(float(row[269]))):
							return float(round(float(row[269])/100,2))
						else:
							print(row[269])
							return ""
def census2(race):
	with codecs.open("census2015/census2.csv", "r" ,encoding='utf-8', errors='ignore') as f:
		for row in csv.reader(f):
			if "Congressional" in row[2]:
				row_district = -1
				if is_number(str(row[2]).split()[2]):
				#if is_number(row[2]):
					row_district = row[2].split()[2]
				row_state = str.lower(row[2].split()[-1])
				#print("State: " + state + " district: " + str(district))
				#print("row State: " + row_state + "row district: " + str(row_district))
				if row_state == str.lower(race.state):
					#print("state----------")
					if row_district == race.district or row_district == -1:
						#print("-------------State: " + row_state + " district: " + str(row_district))
						#print(row[237])
						race.income = row[247]
						race.unemployment = float(row[21])/100
						race.laborforceparticipation = float(row[9])

def census3(race):
	with codecs.open("census2015/census3.csv", "r" ,encoding='utf-8', errors='ignore') as f:
		for row in csv.reader(f):
			if "Congressional" in row[2]:
				row_district = -1
				if is_number(str(row[2]).split()[2]):
				#if is_number(row[2]):
					row_district = row[2].split()[2]
				row_state = str.lower(row[2].split()[-1])
				#print("State: " + state + " district: " + str(district))
				#print("row State: " + row_state + "row district: " + str(row_district))
				if row_state == str.lower(race.state):
					#print("state----------")
					if row_district == race.district or row_district == -1:
						#print("-------------State: " + row_state + " district: " + str(row_district))
						#print(row[237])
						race.averageage = row[67]
						race.white = float(row[129])/100
						race.black = float(row[133])/100
						race.asian = float(row[158])/100
						race.hispanic = float(row[265])/100


def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def sp(year):
	with codecs.open("sp500.csv", "r" ,encoding='utf-8', errors='ignore') as f:
		for row in csv.reader(f):
			if row[0] == str(year + "10"):
				return row[1]

def gas(year):
	with codecs.open("gasprices.csv", "r" ,encoding='utf-8', errors='ignore') as f:
		for row in csv.reader(f):
			if row[0] == str(year + "10"):
				return row[1]

def unemployment(year,state):
	filename = "unemployment/"+state+".csv"
	if str.lower(state) == 'new hampshire':
		filename = "unemployment/new_hampshire.csv"
	if str.lower(state) == 'new jersey':
		filename = "unemployment/new_jersey.csv"
	if str.lower(state) == 'new mexico':
		filename = "unemployment/new_mexico.csv"
	if str.lower(state) == 'new york':
		filename = "unemployment/new_york.csv"
	if str.lower(state) == 'north carolina':
		filename = "unemployment/north_carolina.csv"
	if str.lower(state) == 'south carolina':
		filename = "unemployment/south_carolina.csv"
	if str.lower(state) == 'south dakota':
		filename = "unemployment/south_dakota.csv"
	if str.lower(state) == 'north dakota':
		filename = "unemployment/north_dakota.csv"
	if str.lower(state) == 'rhode island':
		filename = "unemployment/rhode_island.csv"
	if str.lower(state) == 'west virginia':
		filename = "unemployment/west_virginia.csv"

	with codecs.open(filename, "r" ,encoding='utf-8', errors='ignore') as f:
		for row in csv.reader(f):
			if row[0] == str(year + "10"):
				return row[1]

def moneyspent(year,state,district,party):
	filename = str("CandidateSummaryAction"+str(year)+".csv")
	#mstate = str.upper(us.states.lookup(statestr).ap_abbr)
	mstate = us_state_abbrev[state]
	mparty = ""
	if party is "D":
		mparty = "DEM"
	else:
		mparty = "REP"

	#print(mstate + " " + mparty + " " + district)
	
	with codecs.open(filename, "r" ,encoding='utf-8', errors='ignore') as f:
		returnval = "didnt work"
		for row in csv.reader(f):
			if mstate in row[4] and mparty in row[6]:
				newnumber = row[19][1:]
				newnumber = newnumber.replace(",","")
				newnumber = newnumber.replace(".","")
				if is_number(newnumber):
					returnval = newnumber
				else:
					returnval = ""
		return returnval


if __name__ == "__main__":

	races = []
	#(self,year,state,district,status,percentage,party,name):
	with codecs.open("results.csv", "r" ,encoding='utf-8', errors='ignore') as f:
		for row in csv.reader(f):
			if "House" in row[0]:
				if row[9] != "N/A":
					races.append(Race(row[3],row[1],row[5],row[9],row[21],"R",row[8]))
				if row[12] != "N/A":
					races.append(Race(row[3],row[1],row[5],row[12],row[22],"D",row[11]))

	with codecs.open("results2.csv", "r" ,encoding='utf-8', errors='ignore') as f:
		for row in csv.reader(f):
			if "House" in row[0] and "2010" in row[3]: 
				if row[9] != "N/A":
					races.append(Race(row[3],row[1],row[5],row[9],row[21],"R",row[8]))
				if row[12] != "N/A":
					races.append(Race(row[3],row[1],row[5],row[12],row[22],"D",row[11]))

	# for x in races: 
	# 	print(x)

	for race in races:
		census2(race)
		census3(race)


	with open("20102012014percent.csv", "w") as f:
		writer = csv.writer(f, delimiter=',')
		for race in races:
			writer.writerow([str(race.state),str(race.reportdistrict), str(race.status), str(race.party), str(race.memofpowerparty), str(race.money), str(race.white),str(race.asian),str(race.black),str(race.hispanic),str(race.averageage),str(race.income),str(race.laborforceparticipation),str(race.unemployment),str(race.gasprices),str(race.sp),str(race.presapproal),str(race.percentage)])



