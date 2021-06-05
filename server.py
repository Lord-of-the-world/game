from flask import Flask, request
import databases

app = Flask(__name__)
@app.route("/n_r")
def new_room():#5
    id = request.args.get("id")
    c = databases.get_inf("room", "id_room")
    for i in c:
        for j in i:
            if j == int(id):
                print("smth")
                return "1"

    databases.write_in_db("room", "id_room", id)
    return "0"



@app.route("/b_u")
def use_bomb():
    city = request.args.get("city")










@app.route("/sdt_in")
def get_town_information():
    level = request.args.get("level")
    shield = request.args.get("shield")
    num=request.args.get("num")
    login = request.args.get("login")
    id = databases.find_id(login)
    databases.update_t("city"+ num, "shield", shield, "owner", id)
    databases.update_t("city"+ num, "level", level, "owner", id)



@app.route("/n_p")
def new_player():
    login = request.args.get("login")
    z = databases.get_inf("player", "name")
    if z  == []:
        databases.write_in_db("player", "name", login)
        return "0"
    print(z)
    for i in z:
        for j in i:
            if j == login:
                return "1"
    databases.write_in_db("player", "name", login)
    return "0"




@app.route("/c_g")
def connect_room():
    id_room = request.args.get("id_room")
    login = request.args.get("login")
    id_player = databases.find_id(login)
    z = databases.add_player(id_room, id_player)
    if z != 1:
        return "1"
    return "0"







@app.route("/g_p")
def send_player():
    id = request.args.get("id")
    s = databases.get_cor_inf("room", "colvo_players", id )
    return s


def get_information():#2
    money=request.args.get('money')
    bombs=request.args.get("bombs")
    isopen=request.args.get("isopen")
    country = request.args.get("country")


    databases.update("country", "money", money, "country", country)
    databases.update("country", "isopen", isopen,"country", country)
    databases.update("country", "bombs", bombs,"country", country)
