from scrapy import Field, Item

class Product(Item):
    name = Field()
    price = Field()
    stock = Field()
    tags = Field()
    last_updated = Field(serializer=str)
