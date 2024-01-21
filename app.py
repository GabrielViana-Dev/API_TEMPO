from flask import Flask, request, render_template
from api_temp import query_api
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results/', methods =['GET','POST'] )
def results():

    city = request.form['city']
    
    try: 
        data_api = query_api(city)

        description = data_api['weather'][0]['description']

        temp = round((data_api['main']['temp'] - 273.15),2)
        temp_max = round((data_api['main']['temp_max'] - 273.15),2)
        temp_min = round((data_api['main']['temp_min'] - 273.15),2)

        date = (datetime.date.today()).strftime("%d/%m/%Y")
    except Exception:
        return render_template('erro.html')

    return render_template('results.html', city = city.upper(), description = description ,temp = temp, temp_max = temp_max, temp_min = temp_min, date = date)

if __name__ == '__main__':
    app.run(debug=True)
