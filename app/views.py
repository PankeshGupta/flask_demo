from flask import request, Response
from . models import upload_file

@dexter_detection.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        file_path = uploaded_file(file)
        json_dump = json.dumps(dict(description=description))
        resp = Response(json_dump, status=200, mimetype='application/json')
        return resp
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''