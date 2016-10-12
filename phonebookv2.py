import pg

db = pg.DB(dbname='phonebook_db')

query = db.query('select * from phonebook')
name_search = query.namedresult()

while True:
    print "Electronic Phone Book"
    print "====================="
    print "1\. Look up an entry"
    print "2\. Set an entry"
    print "3\. Delete an entry"
    print "4\. List all entries"
    print "5\. Quit"


    numSelected = int(raw_input("What do you want to do (1-5)? "))

    if numSelected == 1:
        name = raw_input("Who would you like to look up? ")
        for listing in name_search:
            if listing.name == name:
                print listing.phone_number
            else:
                pass

    elif numSelected == 2:
        nameGiven = raw_input("Who would you like to set? ")
        numGiven = raw_input("What is their phone number? ")
        eGiven = raw_input("What is their email address? ")
        result_list = db.query("select id from phonebook where name ilike '%s'" % nameGiven).namedresult()
        if len(result_list) > 0:
            id = result_list[0].id
            db.update('phonebook', {
                'id': id,
                'name': nameGiven,
                'phone_number': numGiven,
                'email': eGiven})
            print "Entry for %s updated." % nameGiven
        else:
            db.insert('phonebook', name=nameGiven, phone_number=numGiven, email=eGiven)
            print "Added entry for %s." % nameGiven


    elif numSelected == 3:
        toDelete = raw_input("Whose entry should be deleted? ")
        result_list = db.query("select id from phonebook where name ilike '%s'" % toDelete).namedresult()
        if len(result_list) > 0:
            id = result_list[0].id
            db.delete('phonebook', {
            'id': id})
            print "Entry deleted."

        else:
            print "Entry for %s does not exist." % toDelete


    elif numSelected == 4:
        query = db.query('select * from phonebook')
        for name in name_search:
            print "Found %s's number: %s." % (name.name, name.phone_number)


    elif numSelected == 5:
        print "Goodbye."
        break

    else:
        print "Invalid input."
