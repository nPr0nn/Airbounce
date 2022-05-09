import csv

# Class that handles reading csv two arbitrary columns and return them in form of two arrays
class CSVReader:
     def __init__(self, directory, file):
          self.directory = directory
          self.file      = file

     def read_csv(self, c_1, c_2, c_3, c_4):
          print(self.directory+self.file)
          v1 = []
          v2 = []
          v3 = []
          v4 = []

          # Get Data from the .csv files
          with open(self.directory + self.file, 'r') as csvfile:
               plots = csv.reader(csvfile, delimiter = ';')
               for row in plots:
                    try:
                         v1.append(float(row[c_1]))
                         v2.append(float(row[c_2]))
                         v3.append(float(row[c_3]))
                         v4.append(float(row[c_4]))
                    except:
                         pass

          return v1, v2, v3, v4
