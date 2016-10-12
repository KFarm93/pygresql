import pg

db = pg.DB(dbname='music_db')

query = db.query('select * from album')

result_list = query.namedresult()

for result in result_list:
  print "Album %s released in %s" % (result.name, result.year)

# next script

db.insert('instrument', id='6', name='Bongos')

# next script

db.update('instrument', {
  'id': 6, 'name': 'Bongos'})

# next script
db.delete('instrument', {'id': 6, 'name': 'Bongos'})
