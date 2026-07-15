from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route("/run")
def run_report():
    # The user's text comes from the web address (?name=...) - untrusted input
    user_input = request.args.get("name")

    # Risky: builds a system command straight from that untrusted input
    subprocess.call("generate_report " + user_input, shell=True)
    return "done"
