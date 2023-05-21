def personnel_data():
    employee = {1234:{ "name":"timi", "date_of_birth":"april_5", "branch": "lagos"
        },
        5678: {
        "name": "Jane Smith",
        "date_of_birth": "1990-03-22",
        "office_branch": "London"
    },
    9012: {
        "name": "Michael Johnson",
        "date_of_birth": "1978-11-10",
        "office_branch": "Tokyo"
    }

    }
    return employee


for key, val in personnel_data().items():
    print(key, val)