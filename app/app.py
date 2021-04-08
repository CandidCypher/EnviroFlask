"""
Source for WebApp
"""
from flask import Flask
from flask import render_template
from envirophat import weather

app = Flask(__name__)

@app.route("/")
def home():
    temperature = weather.temperature() *1.8 + 32
    pressure = weather.pressure(unit="Pa")
    altitude = weather.altitude(qnh=1020) * 3.28084
    return render_template("home.html", temperature=temperature, pressure=pressure, altitude=altitude)

@app.route("/history")
def history():
    return render_template("history.html")


@app.route("/diagnostics")
def diagnostics():
    return render_template("diagnostics.html")


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8000, debug=True)
