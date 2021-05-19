from raport_loader import RaportLoader
from article import ITM_article

#Main tool to initialize new article from provided data.
class MainTool:
    
    def __init__(self):
        pass
    
    def get_row(self, index):
        """
        Return a row from xlsx file, specified by (index).
        """
        test_row = raport_loaded.iloc[index]
        return test_row

    def make_article(self, index):
        """
        Return an instance of ITM_article defined by specified row(index).
        """
        #I hope it works as I think it does.
        test_row = raport_loaded.loc[index]
        new_article = ITM_article(test_row[0], test_row[1], test_row[2], test_row[3], test_row[4], test_row[5], test_row[6], test_row[7], test_row[8])
        return new_article
    

mt = MainTool()#This instanciate MainTool.
new_raport = RaportLoader("Raport_Standard.xlsx")#Provides path to file.
raport_loaded = new_raport.load_file()#Loads the specified file.






