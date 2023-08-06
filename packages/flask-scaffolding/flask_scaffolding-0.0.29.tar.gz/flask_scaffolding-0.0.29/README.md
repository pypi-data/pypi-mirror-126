# Flask-Scaffolding-Base
- Flask Scaffolding with builtin Authentication & Authorization
- Installation : 
```
pip install flask-scaffolding
```
- Run to create a new flask app with the given name and destination path.
```
python -m scaffold.web <YOUR_APP_NAME> <path/to/destination>
```
- Add your custom model into `<YOUR_APP_NAME>/app/models/`, 
- Run to add a new screen UI on created app above,
```
python -m scaffold.ui <MODEL_NAME> <path/to/model/file/location>
```