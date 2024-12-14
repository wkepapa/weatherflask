from flask import Flask,render_template,request
from weather import get_curweather
from waitress import serve

app=Flask(__name__)
@app.route('/')
@app.route('/index')
@app.route('/weather')
def gutuweather():
    city=request.args.get('city')
    if not city or not city.strip():
        city="mumbai"

    weauthudata=get_curweather(city)
    if not weauthudata['cod']==200:
        return render_template("citynotfound.html")
    return render_template("weather.html",
    title=weauthudata["name"],
    status=weauthudata["weather"][0]["description"].capitalize(),
    temp=f"{weauthudata['main']['temp']:.1f}" ,       
    feels_like=f"{weauthudata['main']['feels_like']:.1f}"            
    )
    

def index():
    return render_template('index.html')

if __name__=="__main__":
    serve(app,host="0.0.0.0",port=8000)
