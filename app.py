from flask import Flask
import uuid
from datetime import datetime
import pytz

instance_id = uuid.uuid4().hex
dt_now = datetime.now(tz=pytz.timezone('America/Sao_Paulo'))

app = Flask(__name__)

@app.route("/")
def home():
    return f"""<h1>Flask app with Kubernetes</h1>
    <p>Instance ID: {instance_id}</p>
    <p>Created at: {dt_now}</p>
    """