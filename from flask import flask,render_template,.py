from flask import flask,render_template,request


app=flask(_name_)


@app.route('/')
def helloworld():
    return render_template("index.html")

if_name_=='_main_':
    app.run(debug=Flase)