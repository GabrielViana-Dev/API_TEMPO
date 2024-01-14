from flask import Flask, request, render_template
from api_tempo import consulta_api
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resultados/', methods =['GET','POST'] )
def resultados():

    #Realizar consulta na API externa e armazenas dados em uma variável

    cidade = request.form['cidade']
    
    try: 
        dados_api = consulta_api(cidade)

        description = dados_api['weather'][0]['description']

        temp = round((dados_api['main']['temp'] - 273.15),2)
        temp_max = round((dados_api['main']['temp_max'] - 273.15),2)
        temp_min = round((dados_api['main']['temp_min'] - 273.15),2)

        data = (datetime.date.today()).strftime("%d/%m/%Y")
    except Exception:
        return render_template('erro.html')

    return render_template('resultados.html', cidade = cidade.upper(), description = description ,temp = temp, temp_max = temp_max, temp_min = temp_min, data = data)

if __name__ == '__main__':
    app.run(debug=True)