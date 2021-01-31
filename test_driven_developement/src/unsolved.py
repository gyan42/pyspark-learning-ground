class MovingAverage:
    spark = None
    stockPriceInputDir = None
    size = 0
    def __init__(self, spark, stockPriceInputDir,size):
        self.spark = spark
        self.stockPriceInputDir = stockPriceInputDir
        self.size = size

    def calculate(self):
        pass

class MovingAverageWithStockInfo:
    spark = None
    stockPriceInputDir = None
    stockInfoInputDir = None
    size = 0
    def __init__(self, spark, stockPriceInputDir,stockInfoInputDir,size):
        self.spark = spark
        self.stockPriceInputDir = stockPriceInputDir
        self.stockInfoInputDir = stockInfoInputDir
        self.size = size

    def calculate(self):
        pass

    def calculate_for_a_stock(self,stockId):
        pass