from flask import Flask

app = Flask(__name__)


@app.route("/alarm", methods=["GET"])
def receive_alarm():
    # Обработка запроса от send_alarm
    print("Received alarm!")
    return "Alarm received successfully", 200


if __name__ == "__main__":
    app.run(debug=True)
