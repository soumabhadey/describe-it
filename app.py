from flask import Flask, request
import views









app = Flask(__name__)




# app.config['UPLOAD_FOLDER'] = 'uploads'




@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return views.index()
    else:
        return views.describe()
    



if __name__ == '__main__':
    app.run(debug=True)