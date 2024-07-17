import os
def main():
    #user instructions
    print("Enter a category of projects to summarize from the following: 'Ongoing', 'Completed', or 'Backlog'.")
    #add try and except statements to catch errors
    
    #uniform input andto function
    total(input("").strip().casefold())


def total(s):
    #define variables for counting project types
    Ad = 0
    NP = 0
    O = 0
    Val = 0
    WP = 0
    U = 0

    #identifiy correct path
    #path = os.getcwd()
    if s == "ongoing":
        file_list = os.listdir("R:\Quality\Quality_Control\QC Scientist\Projects_Ongoing")
    elif s =="backlog":
        file_list = os.listdir("R:\Quality\Quality_Control\QC Scientist\Project_Backlog")
    elif s =="completed":
        file_list = os.listdir("R:\Quality\Quality_Control\QC Scientist\Archived\Projects_Completed")

    #iterate over list to add to categories
    for file in file_list:
        if file.count("Addendum") > 0:
            Ad += int(file.count("Addendum"))
        elif file.count("New Product") > 0:
            NP += int(file.count("New Product"))
        elif file.count("Other") > 0:
            O += int(file.count("Other"))
        elif file.count("Validation") > 0:
            Val += int(file.count("Validation"))
        elif file.count("White Paper") > 0:
            WP += int(file.count("White Paper"))
        else:
            U += 1
    print(f"Addendum {Ad}, New Product {NP}, Other {O}, Validation {Val}, White Paper {WP}, Unknown {U}")

if __name__ == "__main__":
    main()