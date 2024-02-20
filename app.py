from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/main", methods=["GET", "POST"])
def main():
    r = request.form.get("name")
    return render_template("main.html", r=r)  # 修正了方法名和文件扩展名

@app.route("/image_gpt", methods=["GET", "POST"])
def image_gpt():
    return render_template("image_gpt.html")  # 修正了文件扩展名

if __name__ == "__main__":
    app.run()
