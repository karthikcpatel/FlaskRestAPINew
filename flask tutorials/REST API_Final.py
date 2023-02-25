from flask import Flask, request
app = Flask(__name__)

in_memory_datastore = {
   "COBOL" : {"ExternalRecommendation": 0.25, "WorkHours": 0.50, "SurveyResponse": 0.75, "ChatEmail": 1.0 },
}

@app.route('/')
def hello_mitr():
    """This function will be executed when the server is started.
    """
    return "Welcome MITR!"

@app.get('/emp_data')
def list_programming_languages():
   return {"emp_data":list(in_memory_datastore.values())}


if __name__ == '__main__':
    app.run(debug=True)