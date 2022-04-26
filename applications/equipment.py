# DEFAULT_FETCH Gives the default information for each equipment.
DEFAULT_FETCH = """
    SELECT 
        e.equipment_id,
        e.item,
        e.quantity,
        e.wear_status,
        e.date_purchased
    FROM 
        equipment e
    WHERE
        e.equipment_id = e.equipment_id
"""

# COST_FETCH Gives the default information for equipment, as well as its cost.
COST_FETCH = """
    SELECT 
        e.equipment_id,
        e.item,
        e.quantity,
        e.cost,
        e.wear_status,
        e.date_purchased
    FROM 
        equipment e
    WHERE
        e.equipment_id = e.equipment_id
"""

# INSERT SQL statement to insert a new row into equipment table.
INSERT = """
    INSERT INTO equipment VALUES({id}, '{item}', {quantity}, {cost}, '{status}', '{date_purchased}')
"""

# queryMap stores the potential specifications a user can make about their search.
queryMap = {
    'id' : "AND e.equipment_id  = {}",
    'status' : "AND e.status LIKE '%%{}%%'",
    'item' : "AND e.item LIKE '%%{}%%'",
    'sort_by_quantity': "ORDER BY e.quantity",
    'sort_by_status' : "ORDER BY e.status",
}

# Run whenever a user wants to search for an equipment.
def fetch(args):
    query = DEFAULT_FETCH

    if 'cost' in args: # If we want to show cost:
        query = COST_FETCH

    if  args['id'] != '': # Search by equipment id
        query += queryMap['id'].format(args['id'])
    if  args['status'] != '': # Search by wear status
        query += queryMap['status'].format(args['status'])
    if args['item'] != '': # Search by item
        query += queryMap['item'].format(args['item'])
    if  'sort_by_quantity' in args: # Sort by quantity
        query += queryMap['sort_by_quantity']
    if  'sort_by_status' in args: # Sort by status
        query += queryMap['sort_by_status']
    
    return query

# Run whenever a user wants to create a new equipment.
def add_equipment(args):
    id = args['id'] # ID is a primary key, it must be entered.
    item = args['item'] # Item is not null, it must be entered.
    quantity = args['quantity'] # Quantity is not null, it must be entered.
    cost = "null"
    wear_status = "null"
    date_purchased = "null"

    if args['cost'] != '':
        cost = args['cost']
    if args['status'] != '':
        wear_status = args['status']
    if args['date_purchased'] != '':
        date_purchased = args['date_purchased'] 

    query_equipment = INSERT.format(id=id, item=item, quantity=quantity, cost=cost, status=wear_status, date_purchased=date_purchased)
    return query_equipment
    