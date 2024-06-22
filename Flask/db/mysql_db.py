
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
username = 'root'
password = 'FRANKWUfrankwu'
# host = '172.18.0.3'
host = '192.168.64.6'
port = '4306'
database = 'test'
url = f"mysql+mysqlconnector://{username}:{password}@{host}:{port}/{database}"
engine = create_engine(url, pool_size=5)
Session=sessionmaker(bind=engine)
