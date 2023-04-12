import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/')
def get_list():
    return [1,2,3,4]

@app.get('/diccionario')
def get_dict():
    return {'name': 'Platzy'}

@app.get('/html', response_class=HTMLResponse)
def get_html():
    return """
        <h1>Título de la página web</h1>
        <p>Primer parrafo de mi primera web</p>
        """
def run():
    store.get_categories()

if __name__=='__main__':
    run()