from sqlalchemy import create_engine, text

# using postgresql
engine = create_engine('postgresql://postgres@localhost:5432/techpulse')

#engine = create_engine("sqlite://") creates an in memory database

# engine doesn't connect until we call connect
# engine is a factory that creates new connections when used
# engine stores a connection pool for reusing connections
# the with keyword is the python context manager pattern, it will handle releasing connections 
with engine.connect() as conn: # .connect() implicit begin, vs engine.begin() which has implicit commit
    # here is how we create a textual statement like a select
    query = text("SELECT 'Hello, World!' AS message")
    #query = text("SELECT 15 as id_, 'Hello, World!' as message")
    # connections allow you to run queries
    result = conn.execute(query)
    for row in result:
        print(row.message)
    
    # if you want a list, just do result.all()

    # you can also do tuple assignment with iteration
    #for id_, message in result:
    #    print(f'id: {id_}, message: {message}')

    # or, you could say row = result.first()
    # then look at the mapping... row.message
    #row = result.first()
    #print (row)

    # can also do row._mapping["message"]
    #row = result.first()
    #print(row._mapping["message"])

    #conn.commit() is required if you're not just selecting

