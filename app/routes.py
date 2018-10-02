from app import app
from flask import request, render_template
from app.mainHome import filterURLsHome
from app.mainPd import filterURLsPd
from app.mainDeals import filterURLsDeals

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'GET':
		return render_template('form.html')

	else:
		type_of_page = request.form['type_of_page']
		input_urls = request.form['input_urls']

		OBJs = []
		if type_of_page == 'home':
			OBJs = filterURLsHome(input_urls)
		elif type_of_page == 'pd':
			OBJs = filterURLsPd(input_urls)
		else:
			OBJs = filterURLsDeals(input_urls)
		# print(OBJs[0]['liveHomeDict'])
		# print('\n\n\n')
		# print(OBJs[0]['wipHomeDict'])
		# return str(OBJs[0]['differenceHomeDict'])
		# return str(OBJs)
		return render_template('output.html', OBJs=OBJs, type_of_page=type_of_page)
