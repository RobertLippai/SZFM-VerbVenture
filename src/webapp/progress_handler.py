import json
import os

from flask import Blueprint

progress_handler = Blueprint("progress_handler", __name__)


def fetch_data():
    with progress_handler.open_resource("static/json/userinfo.json") as f:
        userdata = json.load(f)
        return userdata


def add_starting_entry_of(username):
    userdata = fetch_data()
    new_entry = empty_entry(username)
    userdata.append(new_entry)
    with open(
        os.path.join(progress_handler.root_path, "static/json/userinfo.json"), "w+"
    ) as f:
        json.dump(userdata, f, indent=2)


def empty_entry(username):
    new_entry = {
        "scores": {
            "Szokirako": 15,
            "Szokartyak": 25,
            "EgeszitsdKi": 35,
            "Listening": 40,
            "Szoparositas": 45,
        },
        "tries": {
            "Szokirako": 8,
            "Szokartyak": 15,
            "EgeszitsdKi": 20,
            "Listening": 50,
            "Szoparositas": 70,
        },
    }
    new_entry["userName"] = username
    return new_entry


def fetch_data_of(username):
    userdata = fetch_data()
    for entry in userdata:
        if username == entry["userName"]:
            return entry


def calculate_scores(username):
    userdata = fetch_data_of(username)
    szokirako = (
        userdata["scores"]["Szokirako"] / userdata["tries"]["Szokirako"]
        if userdata["tries"]["Szokirako"] > 0
        else 0
    )
    szokartyak = (
        userdata["scores"]["Szokartyak"] / userdata["tries"]["Szokartyak"]
        if userdata["tries"]["Szokartyak"] > 0
        else 0
    )
    egeszitsdki = (
        userdata["scores"]["EgeszitsdKi"] / userdata["tries"]["EgeszitsdKi"]
        if userdata["tries"]["EgeszitsdKi"] > 0
        else 0
    )
    listening = (
        userdata["scores"]["Listening"] / userdata["tries"]["Listening"]
        if userdata["tries"]["Listening"] > 0
        else 0
    )
    parositas = (
        userdata["scores"]["Szoparositas"] / userdata["tries"]["Szoparositas"]
        if userdata["tries"]["Szoparositas"] > 0
        else 0
    )

    sum = szokirako + szokartyak + egeszitsdki + listening + parositas
    sum /= 5
    return roundnumbers([szokirako, szokartyak, egeszitsdki, listening, parositas, sum])


def get_grade(sum):
    if sum < 30:
        return "F"
    if sum < 50:
        return "D"
    if sum < 70:
        return "C"
    if sum < 90:
        return "B"
    return "A"


def roundnumbers(numberlist):
    roundnumberlist = []
    for number in numberlist:
        roundnumberlist.append(int(number * 100))
    return roundnumberlist


if __name__ == "__main__":
    print(calculate_scores("Bela"))
