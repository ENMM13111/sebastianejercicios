from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/comparador_numeros', methods=['GET', 'POST'])
def formulario():
    mayor = None
    menor = None
    if request.method == 'POST':
        try:
            a = int(request.form['a'])
            b = int(request.form['b'])
            c = int(request.form['c'])
            
            if a != b and a != c and b != c:
                if a > b and a > c:
                    mayor = a
                elif b > a and b > c:
                    mayor = b
                else:
                    mayor = c

                if a < b and a < c:
                    menor = a
                elif b < a and b < c:
                    menor = b
                else:
                    menor = c
            else:
                return render_template('comparador_numeros.html', error="Los valores deben ser distintos.")
        except ValueError:
            return render_template('comparador_numeros.html', error="Por favor, ingrese solo números enteros.")

    return render_template('comparador_numeros.html', mayor=mayor, menor=menor)

@app.route('/calificacion', methods=['GET', 'POST'])
def calificacion():
    letra = None
    if request.method == 'POST':
        try:
            nota = int(request.form['nota'])
            if 1 <= nota <= 20:
                if 19 <= nota <= 20:
                    letra = 'A'
                elif 16 <= nota <= 18:
                    letra = 'B'
                elif 13 <= nota <= 15:
                    letra = 'C'
                elif 10 <= nota <= 12:
                    letra = 'D'
                else:  # Si está entre 1 y 9
                    letra = 'E'
            else:
                return render_template('calificacion.html', error="La nota debe estar entre 1 y 20.")
        except ValueError:
            return render_template('calificacion.html', error="Por favor, ingrese un número entero válido.")

    return render_template('calificacion.html', letra=letra)

@app.route('/calculo_ventas', methods=['GET', 'POST'])
def ventas():
    total_pesos = None
    if request.method == 'POST':
        try:
            precios = [float(request.form[f'precio{i}']) for i in range(1, 6)]
            total_dolares = sum(precios)
            tipo_cambio = 400
            total_pesos = round(total_dolares * tipo_cambio)
        except ValueError:
            return render_template('calculo_ventas.html', error="Por favor, ingrese solo números válidos.")

    return render_template('calculo_ventas.html', total_pesos=total_pesos)

@app.route('/doble_triple', methods=['GET', 'POST'])
def doble_triple():
    doble = None
    triple = None
    if request.method == 'POST':
        try:
            numero = float(request.form['numero'])
            doble = round(numero * 2)
            triple = round(numero * 3)
        except ValueError:
            return render_template('doble_triple.html', error="Por favor, ingrese un número válido.")
    
    return render_template('doble_triple.html', doble=doble, triple=triple)

@app.route('/calculo_area', methods=['GET', 'POST'])
def area():
    figura = None
    area_calculada = None
    if request.method == 'POST':
        figura = request.form['figura']
        try:
            if figura == 'circulo':
                radio = float(request.form['radio'])
                area_calculada = round(3.14159 * (radio ** 2))
            elif figura == 'cuadrado':
                lado = float(request.form['lado'])
                area_calculada = round(lado ** 2)
            elif figura == 'rectangulo':
                largo = float(request.form['largo'])
                ancho = float(request.form['ancho'])
                area_calculada = round(largo * ancho)
            elif figura == 'triangulo':
                base = float(request.form['base'])
                altura = float(request.form['altura'])
                area_calculada = round(0.5 * base * altura)
            else:
                return render_template('calculo_area.html', error="Figura no válida.")
        except ValueError:
            return render_template('calculo_area.html', error="Por favor, ingrese valores válidos.")

    return render_template('calculo_area.html', figura=figura, area=area_calculada)

if __name__ == '__main__':
    app.run()
