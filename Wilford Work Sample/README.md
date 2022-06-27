# Wilford’s Truss Work Sample

### How to run the script

- [ ]  Please have python3 installed
- [ ]  Input csv file should be named `sample.csv` , otherwise normalizer will not run
- [ ]  In terminal run

```bash
python3 normalizer.py sample.csv
```

- [ ]  Check your output in `output.csv`

### Approach

My approach was to build a parser in python in order to demonstrate my python skills. The code documentation will give you a better idea of how I approached the data transformations. There were some edge cases that were not in the `sample.csv` that was provided, so I decided to make my own data to test those edge cases (sample input is `wilford-test-sample.csv`  and its output is in `wilford-test-output.csv` for your reference).

### Code Documentation

`easternTimeConverter()` The function’s purpose is to take in the date and time in PST and convert it to EST. Also had to consider the edge case of converting a time at 9:00:00 PM because simply adding 3 hours to get 12:00:00 PM is false, so I wrote an extra elif statement to for this edge case in “AM” and “PM”. One major edge case is if PST time is greater than 9PM, then it will be the next day in EST time so date is going to be updated with `updateDate()`.

`updateDate()`  Input is a string for the current day, output is the next day as a string. We need to update the date to the next day while accounting for whether the date is at the end of the month and whether the month is a February on a leap year. I used a dictionary to store months and their number of days because looking times for a dictionary is constant time and since there are only 11 non leap year months, the space complexity is also constant. 

One thing to consider is that years divisible by 4 and 100 but not by 400 are not leap years, so there might be a potential issue since year data is only represented by two numbers (ie “00”).

`updateZipCode()` Input is a string zip code, output is a string. Purpose of this function is to add leading zeros if input zip code length is less than 5. If I had more time, I could have done a check for each character in the zip code to check if there are non valid character such as letters and symbols.

`totalSeconds()` takes in a string input in HH:MM:SS.MS and output is a float of total seconds. I decided for the output to be a float since we have milliseconds. Multiplying hours by number of seconds and the same for minutes and finally adding seconds, we can calculate the total number of seconds for `FooDuration` and `BarDuration`. Total duration is just the sum of `FooDuration` and `BarDuration` which will be a float.

`updateName()` takes in a string as input and outputs a string. Python’s built in `.upper()` is really helpful since it can change all lower case letters to upper case while considering different languages.

`clean()` takes in input and removes all non UTF-8 characters. I did not have as much time to really flesh out my approach to this. Ideally I can replace all non UTF-8 characters with a unicode replacement but I just decided on using python’s built in `encode()`  and `decode()` to only encode UTF-8 characters so only UTF-8 characters are output.

### Learnings

I was not able to access the slack since the link expired, so I tried my best to account for edge cases by creating additional test data. If I had more time, I would have preferred to create a function that checks for non-UTF-8 character or use the `clean()` function for all the other data transformation functions. I used online resources to account for leap years and raised a potential issue that I discussed in `udpateDate()` . I also ran out of time writing this document, so definitely would have proofread/expanded on my explanations if I had more time.