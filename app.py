from flask import Flask , render_template,jsonify
app = Flask(__name__)

JOB =[
  {
  'id':1,
  'title':'data anallyst',
  'salery':'Rs 15,00,000',
  'location':'ncr , india'
    },
    {
      'id':2,
      'title':'ml enginner',
      'location':'ncr , india'
    },
    {
      'id':3,
      'title':'data scientist',
      'salery':'Rs 25,00,000',
      'location':'benguluru , india'
    },
    {
      'id':4,
      'title':'backened developer',
      'salery':'$ 120,000',
      'location':'new york , usa'
    }
]

@app.route('/')
def hello_world():
    return render_template('home.html',jobs=JOB)

@app.route('/api/jobs')
def list_jobs():
  return jsonify(JOB)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
