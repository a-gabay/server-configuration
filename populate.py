from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Category, Base, CategoryItem, User

engine = create_engine('sqlite:///catalogapp.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Create dummy user
user1 = User(name="John Paul", email="john.paul@test.com",
             picture='https://cdn1.iconfinder.com/data/icons/user-pictures/100/male3-512.png') # NOQA
session.add(user1)
session.commit()

user2 = User(name="Paulette Smith", email="paulette.smith@test.com",
             picture='https://cdn1.iconfinder.com/data/icons/user-pictures/100/female1-512.png') # NOQA
session.add(user2)
session.commit()

# Add Categories
category1 = Category(name="Category 1", user_id=1)
session.add(category1)
session.commit()

category2 = Category(name="Category 2", user_id=2)
session.add(category2)
session.commit()

# Add Items
item1 = CategoryItem(name="Item 1",
                     user_id=1, description="This is item 1 description.",
                     category=category1)

session.add(item1)
session.commit()

item2 = CategoryItem(name="Item 2",
                     user_id=1, description="This is item 2 description.",
                     category=category1)

session.add(item2)
session.commit()

item3 = CategoryItem(name="Item 3",
                     user_id=2,
                     description="This is item 3 description.",
                     category=category2)

session.add(item3)
session.commit()

item4 = CategoryItem(name="Item 4",
                     user_id=2,
                     description="This is item 4 description.",
                     category=category2)

session.add(item4)
session.commit()


categories = session.query(Category).all()
for category in categories:
    print "Category: " + category.name

newItems = session.query(CategoryItem).all()
for item in newItems:
    print "Item: " + item.name
