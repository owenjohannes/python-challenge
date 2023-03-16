# python-challenge (Module 3 Challenge)
## PyBank
The script reads a financial dataset in CSV format to generate a financial analysis.
### Data
The CSV file 'budget_data.csv' is located in 'PyBank/Resources' and contains two columns, 'date' and 'Profits/Losses'. The file's first row is a header row.
### Code Operation
Operating the code only involves running the file 'main.py'. The analysis will be printed out on the terminal and also saved as a text file 'pybank_analysis.txt' in 'PyBank/analysis'.
### Dependencies
This program requires the csv and os libraries
### Analysis Interpretation
The analysis outputs these metrics:
    
Total months: The total number of months included in the dataset   
Total: The net total amount of "Profit/Losses" over the entire period   
Average Change: The changes in "Profit/Losses" over the entire period, and then the average of those changes  
Greatest Increase in profits: The greatest increase in profits (date and amount) over the entire period   
Greatest Decrease in profits: The greatest decrease in profits (date and amount) over the entire period   
    
        
           
           
## PyPoll
The script reads a set of poll data in CSV format to generate electoral results.
### Data
The CSV file 'election_data.csv' is located in 'PyBank/Resources' and contains three columns, 'Voter ID', 'County' and 'Candidate'. The file's first row is a header row.
### Code Operation
Operating the code only involves running the file 'main.py'. The analysis will be printed out on the terminal and also saved as a text file 'pypoll_analysis.txt' in 'PyPoll/analysis'.
### Dependencies
This program requires the csv and os libraries
### Analysis Interpretation
The analysis outputs these metrics:
    
The total number of votes cast  
A complete list of candidates who received votes (Charles Casper Stockham, Diana DeGette, Raymon Anthony Doane)  
The percentage as well as total number of votes each candidate won  
The winner of the election based on popular vote (Diana DeGette)

