import os

from flask import Flask, render_template
from apscheduler.schedulers.background import BackgroundScheduler
import atexit
import pandas as pd
import json
import plotly
import plotly.express as px

from .binance_api import binance_api


def create_app():
    # check if csv id exist
    if not(os.path.isfile('./flaskr/db/symbol_ticker.csv')):
        binance_api()

    # create scheduler task
    scheduler = BackgroundScheduler(daemon=True)
    scheduler.add_job(binance_api, trigger='interval', minutes=60)
    scheduler.start()

    # shut down the scheduler when exiting the app
    atexit.register(lambda: scheduler.shutdown())

    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev'
    )

    # a home page for navigation
    @app.route('/')
    def index():
        return render_template('index.html')

    # a chart page for showing first 5 rows from csv
    @app.route('/chart')
    def chart():
        df = pd.read_csv('./flaskr/db/symbol_ticker.csv')
        df = df.head(5)

        fig = px.bar(df, x="symbol", y="price", barmode="group")

        graph = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
        header = "Symbol Price Ticker Chart"
        return render_template('chart/chart.html', graph=graph, header=header)

    # a pie chart page for showing first 10 rows from csv
    @app.route('/pie-chart')
    def pie_chart():
        df = pd.read_csv('./flaskr/db/symbol_ticker.csv')
        df = df.head(10)

        fig = px.pie(df, values="price", names="symbol")

        graph = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
        header = "Symbol Price Ticker Pie Chart"
        return render_template('chart/chart.html', graph=graph, header=header)

    return app
