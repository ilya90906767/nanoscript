from sqlalchemy import  create_engine,select
from website.models import User,Upload
from sqlalchemy.orm import Session

def check_db():
	engine = create_engine('sqlite:///instance/database.db')
	conn = engine.connect()
	smt = select(Upload).where(Upload.status == 1)
	print(smt)
	r = conn.execute(smt)
	print(r.fetchall())
	return
check_db()
	
