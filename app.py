from splitio.exceptions import TimeoutException
from splitio import get_factory
from flask import Flask, render_template
import logging
logging.getLogger('splitio').setLevel(logging.DEBUG)
app = Flask(__name__)

factory = get_factory('6go42qijm6c548p47q4sjbrv756mvbbpej19', sdk_api_base_url='https://sdk.split-stage.io/api',
                      events_api_base_url='https://events.split-stage.io/api', auth_api_base_url='https://auth.split-stage.io/api')
try:
    factory.block_until_ready(5)  # wait up to 5 seconds
except TimeoutException:
    # Now the user can choose whether to abort the whole execution, or just keep going
    # without a ready client, which if configured properly, should become ready at some point.
    pass


@app.route("/")
def index():
    client = factory.client()
    treatment = client.get_treatment(
        'test@split.io', 'the_queens_gambit_menu')
    if treatment == 'on':
        return render_template('index.html')
    else:
        return render_template('error.html')


@app.route("/lunch")
def lunch():
    return render_template('lunch_menu.html')


@app.route("/happyhour")
def happyhour():
    return render_template('happy_hour_menu.html')
