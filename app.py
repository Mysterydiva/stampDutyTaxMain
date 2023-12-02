from flask import Flask, render_template, request
from SDLT import Solution
from waitress import serve

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/price')
def get_price():
    price = request.args.get('price')
    price =(int(price))
    print(type(price))
    tax = Solution.calculatelbtt(price)
    return render_template(
        "price.html", tax = tax
    )

if __name__ == "__ main__":
    #waitress-serve --host 127.0.0.1 --call hello:create_app
    serve(app, host="0.0.0.0", port=8000)