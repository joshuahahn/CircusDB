# DEFAULT_FETCH Gives the default information for each employee.
DEFAULT_FETCH = """
    SELECT 
        o.act_number,
        o.email_1,
        o.email_2,
        o.email_3,
        o.email_4,
        o.email_5,
        o.animal_1,
        o.animal_2,
        o.animal_3,
        o.equipment_1,
        o.equipment_2
    FROM 
        onstage o
    WHERE
        o.act_number = o.act_number
"""

# INSERT SQL statement to insert a new row into the onstage table.
INSERT = """
    INSERT INTO onstage VALUES({act_num}, '{email_1}', {email_2}, {email_3}, {email_4}, {email_5},{animal_1},{animal_2},{animal_3},{equipment_1},{equipment_2})
"""

# queryMap stores the potential specifications a user can make about their search.
queryMap = {
    'act' : "AND o.act_number = {}",
    'email' : "AND (o.email_1 LIKE '%%{}%%' OR o.email_2 LIKE '%%{}%%' OR o.email_3 LIKE '%%{}%%' OR o.email_4 LIKE '%%{}%%' OR o.email_5 LIKE '%%{}%%')",
    'animal' : "AND (o.animal_1 = {} OR o.animal_2 = {} OR o.animal_3 = {})",
    'equipment' : "AND (o.equipment_1 = {} OR o.equipment_2 = {})"
}

# Run whenever a user makes a query about acts.
def fetch(args):
    query = DEFAULT_FETCH
    if args['act_number'] != '': # Search by act number
        query += queryMap['act'].format(args['act_number'])
    if args['email']!= '': # Search by email
        query += queryMap['email'].format(args['email'], args['email'], args['email'], args['email'], args['email'])
    if args['animal_id'] != '': # Search by animal ID
        query += queryMap['animal'].format(args['animal_id'], args['animal_id'], args['animal_id'])
    if args['equipment_id'] != '': # Search by equipment ID
        query += queryMap['equipment'].format(args['equipment_id'], args['equipment_id'])  
    return query

# Run whenever a user wants to create a new act.
def add_act(args):
    print(args)
    act_num = args['act_number'] # Act is a primary key; must exist.
    email_1 = args['email_1'] # email_1 is NOT NULL; must exist.
    email_2 = "null" # All other variables are null unless otherwise set.
    email_3 = "null"
    email_4 = "null"
    email_5 = "null"
    animal_1 = "null"
    animal_2 = "null"
    animal_3 = "null"
    equipment_1 = "null"
    equipment_2 = "null"

    if  args['email_2'] != '': # Second performer
        email_2 = "'" + args['email_2'] + "'"
    if  args['email_3'] != '': # Third performer
        email_3 = "'" + args['email_3'] + "'"
    if  args['email_4'] != '': # Fourth performer
        email_4 = "'" + args['email_4'] + "'"
    if  args['email_5'] != '': # Fifth performer
        email_5 = "'" + args['email_5'] + "'"
    if  args['animal_1'] != '': # First animal
        animal_1 = args['animal_1']
    if  args['animal_2'] != '': # Second animal
        animal_2 = args['animal_2']
    if  args['animal_3'] != '': # Third animal
        animal_3 = args['animal_3']
    if  args['equipment_1'] != '': # First equipment
        equipment_1 = args['equipment_1']
    if  args['equipment_2'] != '': # Second equipment
        equipment_2 = args['equipment_2']

    query_act = INSERT.format(act_num=act_num, email_1=email_1, email_2=email_2, email_3=email_3, email_4=email_4, email_5=email_5, animal_1=animal_1, animal_2=animal_2, animal_3=animal_3, equipment_1=equipment_1, equipment_2=equipment_2)
    return query_act
    