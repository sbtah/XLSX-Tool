import pandas as pd
from pandas import ExcelWriter, ExcelFile


#Declaration of ITM_article Class. Program will create an instance of ITM_article Class for each article in xls file.
class ITM_article:

    def __init__(self, itm, ean, name, brand, stock, sold, delivery, value_of_sales,value_FIFO):

        self.itm = itm
        self.ean = ean
        self.name = name
        self.brand = brand
        self.stock = stock
        self.sold = sold
        self.delivery = delivery
        self.value_of_sales = value_of_sales
        self.value_FIFO = value_FIFO

    def average_delivery_per(self, period):
        """
        Return a value of average deliveries of unit per period specified.
        """
        average_delivery_calculated = self.delivery / period
        return average_delivery_calculated


    def average_sales_per(self, period):
        """
        Return a value of average sales of unit per period specified.
        """
        average_sales_calculated = self.sold / period
        return average_sales_calculated


    def stock_for_3M(self):
        """
        Return average stock for 3 months, given the xls file was made for a Year.
        """
        average_stock_for_3 = (self.sales / 12) * 3
        return average_stock_for_3


#Declaration of RaportLoader class. The main idea is to load a data from xls file, parse through it and get the data for each ITM_article in each line in of a file.
class RaportLoader(ITM_article):
    #This entire concept might be stupid as fuck.
    def __init__(self, file_name):
        """
        Defines a file_name for an xlsx file to load.
        """
        #this might be stupid.
        self.file_name = file_name
        pass


    def load_file(self):
        """
        Return a variable with file loaded, specified when initialization of RaportLoader class was used.
        """
        file_read = pd.read_excel(self.file_name)
        return file_read


    def get_row(self, index):
        """
        Return a row from xlsx file, specified by index.
        """
        test_row = raport_loaded.loc[index]
        return test_row
    
    
    def make_article(self, index):
        """
        Return a value of ITM_article in specified row.
        """
        #I hope it works as I think it does.
        test_row = raport_loaded.loc[index]
        new_article = ITM_article(test_row[0], test_row[1], test_row[2], test_row[3], test_row[4], test_row[5], test_row[6], test_row[7], test_row[8])
        return new_article


#A Generator of new xls file given the data supplied by RaportLoader Class.
class RaportWriter:
    pass



## TEST unit ITM_Article
# test_article = ITM_article("Farba", 9902121, 5904848764872, 44, "DULUX", 365, 334, 9,34)
# print(f"The stock price for this unit is: {test_article.stock_price_netto()}.")
# print()
# print(test_article.average_sales_per_period(12))
# print()
# print(test_article.stock_for_3_months())
# print("--")


#TEST unit RaportLoader
new_raport = RaportLoader("Raport_Standard.xlsx")
raport_loaded = new_raport.load_file()



#print(raport_loaded) # This prints loaded stuff
#print(raport_loaded.loc[0:]) #This prints rows from index 0 to end.

test_row = raport_loaded.loc[0]
index_of_rows = len(raport_loaded.loc[0:])
print(index_of_rows)

#articile_tuple = tuple(test_article.to_list())#Game breaker!
#print(test_row)

# new_art = ITM_article(test_row[0], test_row[1], test_row[2], test_row[3], test_row[4], test_row[5], test_row[6], test_row[7], test_row[8], test_row[9])
# print(new_art.name)
# print(new_art.stock_for_3_months())



test = new_raport.make_article(2)
print(test.name)
print(test.ean)




