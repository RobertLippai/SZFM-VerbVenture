import json

from flask import Blueprint

progress_handler = Blueprint("progress_handler", __name__)


def fetch_data(username):
    with progress_handler.open_resource("static/json/userinfo.json") as f:
        userdata = json.load(f)
        for entry in userdata:
            if username == entry["userName"]:
                return entry


def calculate_scores(username):
    userdata = fetch_data(username)
    szokirako = userdata["scores"]["Szokirako"] / userdata["tries"]["Szokirako"]
    szokartyak = userdata["scores"]["Szokartyak"] / userdata["tries"]["Szokartyak"]
    egeszitsdki = userdata["scores"]["EgeszitsdKi"] / userdata["tries"]["EgeszitsdKi"]
    listening = userdata["scores"]["Listening"] / userdata["tries"]["Listening"]
    parositas = userdata["scores"]["Szoparositas"] / userdata["tries"]["Szoparositas"]

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
