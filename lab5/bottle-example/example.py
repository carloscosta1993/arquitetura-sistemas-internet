from bottle import Bottle, run, template, request

class storage:
	def __init__ (self):
		self.data = []
	def store(self, query):
		self.data.append(query)
	def show(self):
		return self.data


app = Bottle()
st = storage()
@app.route('/')
@app.route('/hello')
def hello():
    return "Hello World!"

@app.route('/number/<num:int>')
def num_function(num):
	return template('Number {{value}}, glad to meet you?', value=num) 




temp = """ <ul>
   %for item in list:
    <li>{{item}}</li>
   %end
</ul>"""

@app.route('/query')
def query_function():
	if len(request.query) == 0:
		return template(temp, list=st.show())
	for a in request.query:
		print a, request.query[a]
		st.store(a+"="+request.query[a])
	return "just inserted the query<br>ss"





run(app, host='localhost', port=8080)