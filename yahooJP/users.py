users_list = [
    # valid user
    {'name': "Michal",
     'email': 'michalfrompoland1@yahoo.co.jp',
     'id': 'michalfrompoland1',
     'password': 'michal666!',
     'postal code': '102-0072',
     'birth date': '1992/08/07',
     '秘密の質問': 'Zorro'},

    # invalid user
    {'name': "Invalid",
     'email': 'somerandomemail@yahoo.co.jp',
     'id': 'notreallyneeded1',
     'password': 'WorshipMe',
     'postal code': 'either',
     'birth date': '3218/80/77',
     '秘密の質問': 'I have not idea what I\'m doing'
     }
]


def get_email(name):
    for i in users_list:
        if i['name'] == name:
            ind = users_list.index(i)
            return users_list[ind]['id']


def get_password(name):
    for i in users_list:
        if i['name'] == name:
            ind = users_list.index(i)
            return users_list[ind]['password']
