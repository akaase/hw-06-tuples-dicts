company_directory = [
    {
        'name': 'Jill Swanson',
        'age': 55,
        'department': 'Management',
        'phone': '555-1234',
        'salary': '$87,000'
    },
    {
        'name': 'Leslie Knope',
        'age': 35,
        'department': 'Middle Management',
        'phone': '555-5678',
        'salary': '$60,000'
    },
    {
        'name': 'Andy Dwyer',
        'age': 25,
        'department': 'Shoe Shining',
        'phone': '555-9012',
        'salary': '$30,000'
    },
    {
        'name': 'April Ludgate',
        'age': 33,
        'department': 'Administration',
        'phone': '555-3456',
        'salary': '$40,000'
    },
]

for employee in company_directory:
    print(employee['name'], 'in', employee['department'], f"can be reached at { employee['phone'] }." )
