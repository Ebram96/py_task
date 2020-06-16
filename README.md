
This is a sample output of running main.py:


    ***********Trying get_attendance('EMP01', '2020-04-01')*************
    {
        "attended": true,
        "duration": "11:55"
    }
    *********************************Done*******************************
    
    ********************Trying get_history('EMP01')*********************
    {
        "days": [
            {
                "date": "2020-03-31",
                "actions": [
                    {
                        "action": "CheckIn",
                        "time": "2020-03-31T22:00:00"
                    }
                ]
            },
            {
                "date": "2020-04-01",
                "actions": [
                    {
                        "action": "CheckOut",
                        "time": "2020-04-01T10:00:00"
                    },
                    {
                        "action": "CheckIn",
                        "time": "2020-04-01T22:05:00"
                    }
                ]
            },
            {
                "date": "2020-04-02",
                "actions": [
                    {
                        "action": "CheckOut",
                        "time": "2020-04-02T09:50:00"
                    },
                    {
                        "action": "CheckIn",
                        "time": "2020-04-02T21:50:00"
                    }
                ]
            },
            {
                "date": "2020-04-03",
                "actions": [
                    {
                        "action": "CheckOut",
                        "time": "2020-04-03T10:05:00"
                    }
                ]
            }
        ]
    }
    *********************************Done*******************************
