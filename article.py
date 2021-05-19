#Declaration of ITM_article Class. Program will create an instance of ITM_article Class for each article in xls file.
class ITM_article():

    def __init__(self, itm, ean, name, brand, stock, sold, delivery, value_of_sales, value_FIFO):

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


    def end_unit_price(self):
        """
        Return average stock for 3 months, given the xls file was made for a Year.
        """#Change this comm.
        unit_price_calculated = self.value_of_sales / self.sold
        return unit_price_calculated
    
    
    def value_in_buy(self):
        value_in_BUY = (self.value_of_sales - self.value_FIFO)
        return value_in_BUY
    
