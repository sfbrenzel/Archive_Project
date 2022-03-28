# Archive_Project

## Overview

This repo contains two of the finding aids of the many archives belonging to the New Thinkers--a group of influental philosophers during the Weimar Republic in Germany. 


## Scope 

The New Thinkers have been called "professional letter writers" because their archives contain hundreds of letters written to each other and other notable thinkers during this era (including Freud, Benjamin, Tillich, Whitehead etc.). The ultimate aim of this project is to create a database for all their correspondence so that researchers can search, track and visualize this unique correspondence.  

The Archive Project was built on a MacOS system with python 3.10.1 and pip 22.0.4 in visual studio code. 


**How to run this program in a MacOS system:** 

1. clone repo: https://github.com/sfbrenzel/Archive_Project.git

2. navigate to project: cd Archive_Project 

3. create a virtual environment: python3 -m venv venv

4. activate virtual environment: $ source venv/bin/activate 

5. install requirements: python3 -m pip install -r requirements.txt 

6. Run New_Thinking_Search_Program.py


**How to run this program in a Windows System:**

1. clone repo: https://github.com/sfbrenzel/Archive_Project.git

2. navigate to project: cd Archive_Project

3. create a virtual environment: py -m venv venv

4. activate virtual environment: venv\scripts\activate.bat

5. install requirements: pip install -r requirements.txt

6. run project: py New_Thinking_Search_Program.py


## Code Louisville Requirements

**Category 1: Python Programming Basics:**
Implement a “master loop” console application where the user can repeatedly enter commands/perform actions, including choosing to exit the program.  
- See New_Thinking_Search_Program.py

Create a dictionary or list, populate it with several values, retrieve at least one value, and use it in your program.
- See New_Thinking_Search_Program.py

**Category 2: Utilize External Data:**
Read data from an external file, such as text, JSON, CSV, etc, and use that data in your application.
- See Tables folder: folder contains csv files of two finding aids


**Category 3: Data Display**
Visualize data in a graph, chart, or other visual representation of data.
Display data in tabular form
- See New_Thinking_Search_Program.py: program displays data in both tabular form and in a pie chart 
  

**Category 4: Best Practices**
The program should utilize a virtual environment and document library dependencies in a requirements.txt file.
- See requirements.txt


**Stretch Feature List** 
Use pandas, matplotlib, and/or numpy to perform a data analysis project. Ingest 2 or more pieces of data, analyze that data in some manner, and display a new result to a graph, chart, or other display.
- See New_Thinking_Table.py: it combines the dataframes from ERHF_DArchive_TableEF1914.py, and Kassel_Archive_Table.py

