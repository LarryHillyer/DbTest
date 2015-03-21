from sqlalchemy import *
from sqlalchemy.sql import select

#engine = create_engine('sqlite:///C:\\Users\\Patrick\\AppData\\Local\\Microsoft\\Microsoft SQL Server Local DB\\Instances\\MSSQLLocalDb\\msdbdata.mdf')



engine = create_engine('sqlite:///C:\\Users\\Patrick\\Source\\Repos\\NewRussBucks2\\LoserPool1_Copy1\\LoserPool1\\App_Data\\LosersPool2.mdf')
conn = engine.connect()
metadata = MetaData()


users = Table ('Users', metadata,
               Column('UserId', Integer, primary_key = True),
               Column('UserName', String, nullable=False),
               Column('Administrator', String, nullable=False),
               Column('OptionState', String, nullable=False))

s = select([users])
result = conn.execute(s)







print print_table











