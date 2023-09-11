from flask import Flask, request, jsonify
import datetime
import pytz
import os

app = Flask(__name__)

github_url = "https://github.com/your_username/your_repository/blob/main/your_file.py"

source_code_url = "https://github.com/camby15/Task1"

@app.route('/get_info', methods=['GET'])
def get_info():
    # Slack name
    slack_name = "camby15"

    current_day = datetime.datetime.now(pytz.utc).strftime("%A")

    current_time = datetime.datetime.now(pytz.utc)
    utc_offset_hours = current_time.astimezone(pytz.timezone("Etc/UTC")).hour
    is_within_two_hours = abs(utc_offset_hours) <= 2

    track = "backend"

    # Return the information in JSON format
    if is_within_two_hours:
        status_code = 200
        response_data = {
            "slack_name": slack_name,
            "current_day": current_day,
            "current_utc_time": current_time.strftime("%Y-%m-%d %H:%M:%S"),
            "track": track,
            "github_url_file": github_url,
            "github_url_source_code": source_code_url,
            "status_code": "Success",
        }
    else:
        status_code = 500  # Error status code if UTC time is outside +/-2 hours
        response_data = {
            "error": "UTC time is not within +/- 2 hours from now",
            "status_code": "Error",
        }

    return jsonify(response_data), status_code

if __name__ == '__main__':
    app.run(debug=True)
