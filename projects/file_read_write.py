#!/usr/local/bin/python3

import pandas as pd
import os
#from doltpy.core import Dolt
#import xlsxwriter

def main():
    os.chdir('/home/student/mycode/projects/players/')


    #Create an excel workbook
    #workbook = xlsxwriter.Workbook('nfl_data.xlsx')
    #Add a sheet to workbook
    #worksheet = workbook.add_worksheet()

    url_base = 'https://raw.githubusercontent.com/guga31bb/nflfastR-data/master/'
    roster_path = 'roster-data/roster.csv.gz'

    #repo = Dolt('.')
    
    # Start with rosters CSV
    rosters_url = url_base + roster_path
    rosters_df  = pd.read_csv(rosters_url,compression='gzip',low_memory=False)


    #Grab the Season
    filtercolumn = [col for col in roster_df if col.startswith('season.')]
    season_df = rosters_df[filtercolumn]
    season_df = season_df.rename(columns=lambda x: x.replace('season.', ''))

    #Grab the jerseyNumber
    filtercolumn = [col for col in roster_df if col.startswith('jerseyNumber.')]
    jersey_df = rosters_df[filtercolumn]
    jersey_df = jersey_df.rename(columns=lambda x: x.replace('jerseyNumber.', ''))

    #Write to worksheet
    worksheet.write('A', season_df)
    worksheet.write('B', jersey_df)

if __name__ == "__main__":
    main()
