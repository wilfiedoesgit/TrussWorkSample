import csv

def updateDate(date):
    #input 4/1/11, go to next day
    nonLeapMonths = {"1": 31,
                     "3": 31,
                     "4": 30,
                     "5": 31,
                     "6": 30,
                     "7": 31,
                     "8": 31,
                     "9": 30,
                     "10": 31,
                     "11": 31,
                     "12": 31
    }
    month, day, year = date.split("/")
    if month not in nonLeapMonths:
        leapYear = int(year) % 4 == 0
        if leapYear:
            if day == "28":
                day = "29"
            elif day == "29":
                day = "1"
                month = "3"
            else:
                day = str(int(day) + 1)
        else:
            #only 28 days if not on a leap year
            if day == "28":
                day = "1"
                month = "3"
            else:
                newDay = int(day) + 1
                if newDay < 10:
                    day = str(newDay)
                else:
                    day = str(newDay)
    else:
        #check also if it's the last day of the year
        if month == "12" and day == "31":
            day = "1"
            month = "1"
            nextYear = int(year) + 1
            if nextYear < 10:
                year = "0" + str(nextYear)
            elif nextYear == 100:
                year = "00"
            else:
                year = str(nextYear)
        #otherwise check if its last day of any other month
        elif int(day) == nonLeapMonths[month]:
            day = "1"
            month = str(int(month) + 1)
        else:
            day = str(int(day) + 1)
    return month + "/" + day + "/" + year



def easternTimeConverter(pacificTime):
    #input 4/1/11 11:00:00 AM
    
    date, time, midday = pacificTime.split(" ")
    
    timeArray = time.split(":")
    hour = int(timeArray[0])
    #case when AM, added time goes over 12, still current day
    if midday == "AM" and hour == 12:
        timeArray[0] = str((hour + 3) % 12)
        time = ":".join(timeArray)
    elif midday == "PM" and hour == 12:
        timeArray[0] = str((hour + 3) % 12)
        time = ":".join(timeArray)
    elif midday == "AM" and hour + 3 >= 12:
        #we only need to update the time and the midday sign
        if hour + 3 == 12:
            timeArray[0] = str(12)
        else:
            timeArray[0] = str((hour + 3) % 12)
        time = ":".join(timeArray)
        midday = "PM"
    elif midday == "AM" and hour + 3 < 12:
        #just update the hour
        timeArray[0] = str(hour + 3)
        time = ":".join(timeArray)
    #when we go to next day
    elif midday == "PM" and hour + 3 >= 12:
        #update time, midday sign, and day
        #we only need to update the time and the midday sign
        if hour + 3 == 12:
            timeArray[0] = str(12)
        else:
            timeArray[0] = str((hour + 3) % 12)
        time = ":".join(timeArray)
        midday = "AM"
        #update date
        date = updateDate(date)
        
    #stay in the night
    elif midday == "PM" and hour + 3 < 12:
        #just need to update the hour
        timeArray[0] = str(hour + 3)
        time = ":".join(timeArray)
    return date + " " + time + " " + midday

def updateZipCode(number):
    #if zip code length is under 5, add prefix zeros to make zip code a lenght of 5
    if len(number) < 5:
        return "0" * (5 - len(number)) + number
    else:
        return number

def updateName(name):
    #makes all letters uppercase
    return name.upper()

def totalSeconds(time):
    #converts time in HH:MM:SS.MS to seconds
    hours, minutes, seconds = time.split(":")
    total = 0.0
    total += int(hours) * 60 * 60
    total += int(minutes) * 60
    total += float(seconds)
    return total

def clean(note):
    #removes non UTF-8 characters
    note = note.encode("utf-8", "ignore").decode()
    return note

with open('sample.csv', 'r') as csvFile:
    #preferred using dictionary reader to improve variable name readability
    input = csv.DictReader(csvFile)
    
    with open('output.csv', 'w') as newFile:
        #sets up csvWriter to output a csv
        fieldNames = ['Timestamp', 'Address', 'ZIP', 'FullName', 'FooDuration', 'BarDuration', 'TotalDuration', 'Notes']
        csvWriter = csv.DictWriter(newFile, fieldnames = fieldNames)
        csvWriter.writeheader()

        #go through each line to calculate "normalized" values
        for line in input:
            pacificTime = line['Timestamp']
            easternTime = easternTimeConverter(pacificTime)

            inputZipCode = line['ZIP']
            newZip = updateZipCode(inputZipCode)
            
            inputFullName = line['FullName']
            newFullName = updateName(inputFullName)

            inputAddress = line['Address']
            
            inputFooDuration = line['FooDuration']
            newFooDuration = totalSeconds(inputFooDuration)

            inputBarDuration = line['BarDuration']
            newBarDuration = totalSeconds(inputBarDuration)
            #total duration is sum of foo and bar
            newTotalDuration = newFooDuration + newBarDuration

            inputNotes = line['Notes']
            newNotes = clean(inputNotes)
            newRow = {'Timestamp' : easternTime,
                        'Address' : inputAddress,
                        'ZIP' : newZip,
                        'FullName' : newFullName,
                        'FooDuration' : newFooDuration,
                        'BarDuration' : newBarDuration,
                        'TotalDuration' : newTotalDuration,
                        'Notes' : newNotes}
            csvWriter.writerow(newRow)

            


    
        
