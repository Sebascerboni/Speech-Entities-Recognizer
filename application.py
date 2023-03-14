import json
import os
from flask import Flask, Response, abort, request, send_file

from modelo import modelo

app = Flask(__name__)
root_path = os.getcwd()

#forbidden
forbidden = []

#Load and sending of files
@app.route('/', defaults={'file':'index.html'})
@app.route('/<path:file>')
def file(file):
    full = os.path.join(root_path,'webapp',file)
    #file doesn´t exist
    if not os.path.exists(full):
        return abort(404)
    
    #file is in fact a directory
    if os.path.isdir(full):
        return abort(403)

    if os.path.isfile(full):
        #File exists but it's not meant to be served
        if file in forbidden:
            return abort(403)
        #File exists and it's meant to be served
        return send_file(full)


@app.get('/api/data/<string:id>')
def prueba(id):
    return id


#API resource parsing
@app.post('/api/data')
def send_my_data():
    #Here you preprare your data to be send later
    print(request.full_path)
    
    index = request.form.get("index")
    data = modelo(index)
    #print(data)
    return Response(response=data, content_type='application/json')

@app.get('/procesar')
def procesar_peticion():
    index = request.args.get("index")
    content = ''

    for i in range(0,10):
        content += f'<tr><td>{i}</td><td>{index}</td></tr>'
    
    return render_template('template.html', {'contenido': content}, True)


def render_template(template:str, data = {}, isPath=True):
    '''
    It uses a dict with the values to be rendered with the syntax:
    In template: &{ variable_name }& 
    In dictionary:
            {
                'variable_name': value
            } 
    Spaces between opening and closing braces are mandatory. If you put in your template
    &{variable_name}& it won't be parsed so in the rendered file it will appear as it is.
    '''
    content = template
    if isPath:
        content = open(template,'r',encoding='utf-8').read()

    for value in data:
        content = content.replace("&{ "+value+" }&", str(data[value]))
    return content


def as_json(data: dict):
    return Response(response=json.dumps(data), content_type='application/json')

if __name__ == "__main__":
    app.run(host=('0.0.0.0'),port=80)