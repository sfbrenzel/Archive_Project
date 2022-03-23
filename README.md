# Archive_Project

Overview

This repo contains some of the finding aids of the many archives belonging to the New Thinkers--a group of influental philosophers during the Weimar Republic in Germany. 


Scope 

The New Thinkers have been called "professional letter writers"--their archives containing thousands of letters written to each other and other notable thinkers during this era (including Freud, Benjamin, Tillich, Whitehead etc.). The aim of this project is to create a database for all their correspondence so that researchers can search, track and visualize this unique correspondence.  

The Archive Project was built on a MacOS system with python 3.10.1 and pip 22.0.4 in visual studio code. 

How to run this program: 

1) clone repo: https://github.com/sfbrenzel/Archive_Project.git

2) create a virtual environment: python3 -m venv 

3) activate virtual environment: $ source venv/bin/activate 

4) install requirements: python3 -m pip install -r requirements.txt 

5) Run Tables/New_Thinking_Search_Program.py


Code Louisville Requirements

Category 1: Python Programming Basics:
Implement a “master loop” console application where the user can repeatedly enter commands/perform actions, including choosing to exit the program.

The search program implements a master loop by asking users to input their search paramaters. It also allows them to exit the program.   


Category 2: Utilize External Data:
Read data from an external file, such as text, JSON, CSV, etc, and use that data in your application.

This project uses the finding aids of the Eugen Rosenstock-Huessy Digital Archive (excel sheet that has been converted to a csv file) and the Universität Kassel's Rosenzweig Teilnachlass(pdf that has been converted to csv file). 

Category 3: Data Display
Visualize data in a graph, chart, or other visual representation of data.
Display data in tabular form

This project uses tabulate to create a table of search results. It also produces a pie chart  

Category 4: Best Practices
The program should utilize a virtual environment and document library dependencies in a requirements.txt file.

This program does utilize a viritual environment and has a requirements.txt file. 

Stretch Feature List 
Use pandas, matplotlib, and/or numpy to perform a data analysis project. Ingest 2 or more pieces of data, analyze that data in some manner, and display a new result to a graph, chart, or other display.

Each data set has been cleaned (see ERHF_DArchive_TableEF1914.py and Kassel_Archive_Table.py) and merged into one new table using pandas (see New_Thinking_Table.py). 
