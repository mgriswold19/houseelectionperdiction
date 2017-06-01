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


class Result(object):
    def __init__(self,state,district):

        self.state = state
        self.district = district
        self.id = makeid(state,district)
        self.status1 = ""
        self.party1 = ""
        self.actual1 = 0
        self.perdicted1 = 0
        self.errors1 = 0
        self.status2 = ""
        self.party2 = ""
        self.actual2 = 0
        self.perdicted2= 0
        self.errors2 = 0;

def makeid(state,district):
    abriv = us_state_abbrev[state]
    number = "";
    if (float(district) <= 9):
        number = "0" + str(district)
    else:
        number = str(district)

    return str.upper(abriv) + "-" + number

if __name__ == "__main__":
    results = []
                    
    with codecs.open("2016percentforresults.csv", "r" ,encoding='utf-8', errors='ignore') as a:
        datareader = csv.reader(a)
        with codecs.open("randomforestresultsformap.csv", "r" ,encoding='utf-8', errors='ignore') as f:
            resultsreader = csv.reader(f)
            for i in range(0,410):
                try:
                    datarow = next(datareader)
                    resultsrow = next(resultsreader)
                
                    
                    if float(resultsrow[1]) == float(datarow[17]):
                        print(datarow[0])
                        print(datarow[1])
                        print(datarow[17])
                        print(resultsrow[1])
                        results.append(Result(datarow[0],datarow[1]))
                        results[i].status1 =  datarow[2]
                        results[i].actual1 = resultsrow[1]
                        results[i].perdicted1 = resultsrow[2]
                        results[i].errors1 = resultsrow[3]
                    else:
                        print("fail-------------")
                        print(datarow[0])
                        print(datarow[1])
                        print(datarow[17])
                        print(resultsrow[1])
                except:
                    print(i)
                
                try:
                    datarow2 = next(datareader)
                    resultsrow2 = next(resultsreader)
                
                    # print("2---------")
                    # print(datarow2[0])
                    # print(datarow2[1])
                    # print(resultsrow2[0])
                    # print("----------")
                    if float(resultsrow2[1]) == float(datarow2[17]):
                        print(datarow2[0])
                        print(datarow2[1])
                        print(datarow2[17])
                        print(resultsrow2[1])
                        #if float(datarow2[1]) != 0:
                        results[i].status2 =  datarow2[2]
                        results[i].actual2 = resultsrow2[1]
                        results[i].perdicted2 = resultsrow2[2]
                        results[i].errors2 = resultsrow2[3]
                        # else:
                        #     results.append(Result(datarow2[0],datarow2[1]))
                        #     results[i].status1 =  datarow2[2]
                        #     results[i].actual1 = resultsrow2[1]
                        #     results[i].perdicted1 = resultsrow2[2]
                        #     results[i].errors1 = resultsrow2[3]
                    else:
                        print("fail-------------")
                        print(datarow2[0])
                        print(datarow2[1])
                        print(datarow2[17])
                        print(resultsrow2[1])
                except:
                    print("except")
                    print(i)
                
                # else:
                #     results.append(Result(datarow[0],datarow[1]))
                #     results[i].status1 =  datarow[2]
                #     results[i].actual1 = resultsrow[1]
                #     results[i].perdicted1 = resultsrow[2]
                #     results[i].errors1 = resultsrow[3]


    with open("formap.csv", "w") as f:
        writer = csv.writer(f, delimiter=',')
        for result in results:
            writer.writerow([str(result.id),str(result.status1),str(result.actual1),str(result.perdicted1),str(result.errors1),str(result.status2),str(result.actual2),str(result.perdicted2),str(result.errors2)])
