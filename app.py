from flask import Flask, render_template, request, redirect, url_for
from database import add_student, get_all_students, delete_student, update_student, search_student, get_toppers

app = Flask(__name__)

# ── Homepage ──
@app.route("/")
def index():
    students = get_all_students()
    toppers = get_toppers()
    return render_template("index.html",
                         students=students,
                         toppers=toppers)

# ── Add Student ──
@app.route("/add", methods=["POST"])
def add():
    name = request.form["name"]
    roll_number = request.form["roll_number"]
    maths = int(request.form["maths"])
    science = int(request.form["science"])
    english = int(request.form["english"])
    add_student(name, roll_number, maths, science, english)
    return redirect(url_for("index"))

# ── Delete Student ──
@app.route("/delete/<int:id>")
def delete(id):
    delete_student(id)
    return redirect(url_for("index"))

# ── Update Student ──
@app.route("/update/<int:id>", methods=["POST"])
def update(id):
    name = request.form["name"]
    roll_number = request.form["roll_number"]
    maths = int(request.form["maths"])
    science = int(request.form["science"])
    english = int(request.form["english"])
    update_student(id, name, roll_number, maths, science, english)
    return redirect(url_for("index"))

# ── Search Student ──
@app.route("/search")
def search():
    keyword = request.args.get("keyword", "")
    students = search_student(keyword)
    toppers = get_toppers()
    return render_template("index.html",
                         students=students,
                         toppers=toppers,
                         keyword=keyword)

if __name__ == "__main__":
    app.run(debug=True)