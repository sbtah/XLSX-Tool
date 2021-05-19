import pandas as pd

#Declaration of RaportLoader class. The main idea is to load a data from xls file, parse through it and get the data for each ITM_article in each line in of a file.
class RaportLoader:
    #This entire concept might be stupid as fuck.
    def __init__(self, file_name):
        """
        Defines a file_name for an xlsx file to load.
        """
        #this might be stupid.
        self.file_name = file_name
        
 

    def load_file(self):
        """
        Return a variable with file loaded, specified when initialization of RaportLoader class was used.
        """
        file_read = pd.read_excel(self.file_name)
        return file_read
