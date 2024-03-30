from flask import Flask, render_template, request, json
from get_result import *

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def hello_world():
   return render_template("home.html")


@app.route('/predict')
def predict():
   return render_template("predict.html")

@app.route('/company')
def company():
   return render_template("company.html")

@app.route('/test')
def test():
   return render_template("index.html")

@app.route("/form", methods=["POST", "GET"])
def form_data():

   if request.method == "POST":
      branch = request.form.get("Branch")
      tenper = request.form.get("tenper")
      tweper = request.form.get("tweper")
      dp = request.form.get("dp")
      sem3 = request.form.get("sem3")
      sem4 = request.form.get("sem4")
      sem5 = request.form.get("sem5")
      sem6 = request.form.get("sem6")
      cgpa = request.form.get("cgpa")
      gaps = request.form.get("gaps")
      ats = request.form.get("variableName")
      inter = request.form.get("Internships")
      certi = request.form.get("certifications")

      inp_list = [branch, float(tenper), float(sem3), float(sem4), float(sem5), float(sem6), float(cgpa), int(gaps), int(ats), float(tweper), float(dp), float(certi), float(inter)]
      inp_list2 = [branch, float(tenper), float(sem3), float(sem4), float(sem5), float(sem6), float(cgpa), float(tweper), float(dp),float(certi), float(inter)]
      
      a = get_result(inp_list)

      if a[0] == 0:
         a = " less chance of getting placed"
         c = "But you can still work hard do some internships and certification and crack a package of"
      else:
         a = " high chance of getting placed"
         c = "You are capabale of cracking atleast a package"


      d = "You have"

      b = get_result2(inp_list2)
      return render_template("result.html",intro = d, res = a,intro2=c, res2 = str(format(b[0], ".2f")) + " lacks")

   return render_template("form.html")


if __name__ == '__main__':
   app.run(debug=True)
