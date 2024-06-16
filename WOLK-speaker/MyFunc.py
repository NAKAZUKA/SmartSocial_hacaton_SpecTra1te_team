import BD as bd
import CoordMetr as cm


def main(data):
    # data['latitude'] = 59.2780
    # data['longitude'] = 39.713415

    user = bd.get_question('SELECT id_user, nik FROM USERS WHERE nik == "' + data['nik'] + '"')
    print(user)
    if len(user) == 0:
        bd.get_insert('INSERT INTO USERS (nik) VALUES ("' + data['nik'] + '")')
        user = bd.get_question('SELECT id, nik FROM USERS WHERE nik == "' + data['nik'] + '"')

    id_user = user[0]['id_user']
    bd.get_insert(
        'INSERT INTO GPS (id_user, latitude, longitude) VALUES ("' + str(id_user) + ', ' + str(data['latitude']) + ', ' + str(data[
            'longitude']) + '")')

    ot = []
    dd = bd.get_question('SELECT * FROM PLACES')
    for i in range(len(dd)):
        rty = cm.coord_to_metr([data['latitude'], data['longitude']], [dd[i]['latitude'], dd[i]['longitude']])
        if dd[i]['radius'] >= rty:
            ot.append(dd[i])





    return ot
