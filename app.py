from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  


@app.route('/about')
def about():
    return render_template('about.html') 


@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    return jsonify(message=f'Hello, {name}!')  


if __name__ == "__main__":
   
    app.run(host='0.0.0.0', port=5000, debug=True)  

#http://chargewave:5000
#http://172.18.76.189:5000
