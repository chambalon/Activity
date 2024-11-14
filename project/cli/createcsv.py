import csv


# Create a csv file using csv.writer()       
def create_csv():  

    row_list = [["Firstname","Lastname","Date","Division","Points","Summary"],
                ["Terza","Lowton","2017-09-15",1,53,"Defensive Duties"],
                ["Kayle","Trayes","2017-10-23",9,83,"Offensive Duties"],
                ["Reba","Crosi","2017-10-23",6,84,"Offensive Duties"],
                ["Barnett","Dunnico","2018-02-26",5,24,"Offensive Duties"],
                ["Elke","Collete","2017-06-19",6,68,"Oversight Duties"],
                ["Tess","Gosson","2017-12-22",9,22,"Defensive Duties"],
                ["Zedekiah","Miller","2018-04-09",3,89,"Offensive Duties"],
                ["Zelma","Ivatt","2018-01-02",1,72,"Offensive Duties"],
                ["Vivia","Twidell","2017-11-17",9,72,"Offensive Duties"],
                ["Alvira","Elger","2017-05-02",6,58,"Oversight Duties"]]
    

    # Open the records.csv file in writing mode using open() function
    try:
        with open('records.csv', 'w', newline='') as file:
            # Create the writer object using csv.writer()
            csvwriter = csv.writer(file)
            # 2D list is passed to the writer.writerows() function to write the data of the list to the CSV file
            return csvwriter.writerows(row_list)
        
    except Exception as e:
        print("Error",e)
        print("Something went wrong")
        
create_csv()  