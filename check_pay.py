from flask import Flask, request
from db import add_payment
app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def get_notification():
    try:
        try:
            print("request =", request.args, "form", request.form)
        except Exception as e:
            print(e)

        res = request.form.get("MERCHANT_ORDER_ID")

        if request.form.get("MERCHANT_ID") == '230751':
            print("RES =", res)

            add_payment(user_id=request.form.get("MERCHANT_ORDER_ID"),
                        phone=request.form.get("P_PHONE"),
                        email=request.form.get("P_EMAIL"),
                        amount=request.form.get("AMOUNT"),
                        int_id=request.form.get("intid"))

    except Exception as e:
        print("get_notification EX =", e)
    return "<h1 style='color:blue'>Hello There!</h1>"


if __name__ == "__main__":
    app.run(host='0.0.0.0')
