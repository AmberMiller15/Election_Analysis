# Election_Analysis
using Python to analyze election results

## Project Overview
A Colorado Board of Elections asked for the following data from a recent local congressional election. 

1. Calculate the total number of votes cast.
2. A complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determin the winner of the election based on popular vote.

## Resources
- Data Source: election_results.csv
- Software: Python 3.10.7, Visual Studio Code, 1.71.2 

## Election Results
The analysis of the election shows that:
- There were 369,711 votes cast in the election. 
- The county statistics were:
    - Jefferson County accounted for 10.5% (38,855) of the 369,711 votes. 
    - Denver County accounted for 82.8% (306,055) of the 369,711 votes. 
    - Arapahoe County accounted for 6.7% (24,801) of the 369,711 votes. 
- The county with the largest vote was:
    - Denver County which accounted for 82.8% (306,055) of the 369,711 votes. 
- The candidates were:
    - Charles Casper Stockham
    - Diana Gette
    - Raymon Anthony Doane
- The candidate results were:
    - Stockham received 23.0% (85,213) of the 369,711 votes. 
    - Gette recieved 73.8% (272,892) of the 369,711 votes. 
    - Doane recieved 3.1% (11,606) of the 369,711 votes. 
- The winner of the election was:
    - Diana Gette who recieved 73.8% (272,892) of the 369,711 votes

## Challenge Summary
- This code can be used to determine the vote count for any election. 
- For a presidential election this can be very helpful where the votes are county by state and by political party as well as by candidate, you can change the county statistics to track the statistics by state. In order to get the political party voting percentage and winning political party by state, can add a section that can loop through the data to pull out political party instead candidate name as well. Can also have this be listed based on state as well. 
