from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root:HRPHLdZaOSaPwHEYSlLmCaibbCOyuLpA@shinkansen.proxy.rlwy.net:50387/railway")


meta = MetaData()

conn = engine.connect()