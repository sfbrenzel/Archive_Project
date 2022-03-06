# Archive_Project

---Overview---

This repo contains some of the finding aids of the many archives belonging to the New Thinkers--a group of influental philosophers during the Weimar Republic in Germany 


---Scope--- 

The New Thinkers have been called "professional letter writers"--their six or so archives containing thousands of letters written to each other and other notable thinkers during this era (including Freud, Benjamin, Tillich, Whitehead etc.). The aim of this project is to create a master list of all their correspondence so that researchers can search, track and visualize this unique correspodence  


---Instructions---

The Archive Project was built with (Python version and pip version). It contains two programs: a search program and a visualization program. 
To run the search and visualization program: 

---Install prerequisites---

1) pip install pandas (search and visualization)

2) pip install tabulate (search)


Run Program 

1) git clone link: 

2) cd Archive_Project

3) New_Thinking_Search_Program.py

4) New_Thinking_Data_Analysis_Program.py



---Code Louisville Requirements--- 

Category 1: Python Programming Basics:
Implement a “master loop” console application where the user can repeatedly enter commands/perform actions, including choosing to exit the program.

    New_Thinking_Search Program 

Category 2: Utilize External Data:
Read data from an external file, such as text, JSON, CSV, etc, and use that data in your application.

    This project uses the finding aids of the Eugen Rosenstock-Huessy Digital Archive (excel sheets that have been converted to csv files) and the Universität Kassel's Rosenzweig Teilnachlass(pdf that has been converted to csv file). This data has been cleaned and merged into one new table using pandas in New_Thinking_Table.py

Category 3: Data Display
Visualize data in a graph, chart, or other visual representation of data.
Display data in tabular form

Category 4: Best Practices
The program should utilize a virtual environment and document library dependencies in a requirements.txt file.

Stretch Feature List 
Use pandas, matplotlib, and/or numpy to perform a data analysis project. Ingest 2 or more pieces of data, analyze that data in some manner, and display a new result to a graph, chart, or other display.
