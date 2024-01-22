from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, DateTime
from sqlalchemy.orm import relationship

from .database import Base


class Inventory(Base):
    __tablename__ = "inventory"

    productid = Column(String, primary_key=True)
    name = Column(String)
    quantity = Column(Integer)
    category = Column(String)
    subcategory = Column(String)

    # inv = relationship("Orders", back_populates="orders")

# class Orders(Base):
#     __tablename__ = "orders"

#     orderid = Column(String, primary_key=True)
#     productid = Column(String, ForeignKey("inventory.productid"))
#     currency = Column(String)
#     quantity = Column(Integer)
#     shippingcost = Column(Float)
#     amount = Column(Float)
#     channel = Column(String)
#     channelgroup = Column(String)
#     campaign = Column(String)
#     datetime = Column(DateTime)


#     orders = relationship("Inventory", back_populates="inv")
