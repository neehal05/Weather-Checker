from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = '2e40f3c1e52d46dc956170311252907'

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    error = None
    if request.method == 'POST':
        location = request.form.get('location')
        if location:
            url = f'http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={location}&aqi=no'
            try:
                response = requests.get(url)
                weather_data = response.json()
                if 'error' in weather_data:
                    error = weather_data['error']['message']
                    weather_data = None
            except Exception as e:
                error = str(e)
    return render_template('index.html', weather=weather_data, error=error)

if __name__ == '__main__':
    app.run(debug=True)