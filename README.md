## Setup

### db.py
Ändra **DATABASE_URL** i db.py-filen: 

```py
DATABASE_URL = 'postgresql+psycopg2://username:password@localhost:your_port/database_schema'
```

Ändra:
- username
- password
- your_port 
- database_schema

Till dinna inställningar.


### alembic.ini

I alembic.ini ändra:

```py
sqlalchemy.url = postgresql+psycopg2://username:password@localhost:your_port/database_schema
```
Så att den matchar den vi skrev i **DATABASE_URL** i db.py-filen.

