#!/usr/bin/python3
import requests

## Define NEOW URL
NEOURL = "https://api.nasa.gov/planetary/apod?"

# this function grabs our credentials
# it is easily recycled from our previous script
def returncreds():
    ## first I want to grab my credentials
    with open("/home/student/nasa.creds", "r") as mycreds:
        nasacreds = mycreds.read()
    ## remove any newline characters from the api_key
    nasacreds = "api_key=" + nasacreds.strip("\n")
    return nasacreds

# this is our main function
def main():
    ## first grab credentials
    nasacreds = returncreds()

    ## update the date below, if you like
    date = input("What date do you want to see a picture from? (MM-DD-YYYY): ")
    date = date.split('-')
    month = date[0]
    day = date[1]
    year = date[2]
    print(date)
   
    startdate = "start_date=" + year + "-" + month + "-" + day
    enddate = "end_date=" + year + "-" + month + "-" + day
    print(startdate)
    ## the value below is not being used in this
    ## version of the script
    # enddate = "end_date=END_DATE"

    # make a request with the request library
    neowrequest = requests.get(NEOURL + startdate + "&" + enddate + "&" +  nasacreds)

    # strip off json attachment from our response
    neodata = neowrequest.json()

    ## display NASAs NEOW data
    print(neodata)

if __name__ == "__main__":
    main()

