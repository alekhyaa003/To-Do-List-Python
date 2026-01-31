from flask import Flask, render_template, request, redirect, url_for
import todo

app = Flask(__name__)

@app.route("/")
def index():
    tasks = todo.load_tasks()
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add():
    task = request.form.get("task")
    if task:
        todo.add_task(task)
    return redirect(url_for("index"))

@app.route("/delete/<int:task_id>")
def delete(task_id):
    todo.delete_task(task_id)
    return redirect(url_for("index"))

@app.route("/complete/<int:task_id>")
def complete(task_id):
    todo.complete_task(task_id)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)


