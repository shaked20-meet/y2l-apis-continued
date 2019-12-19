import json, requests
from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/study_image', methods = ['POST'])
def study_image():
	 # At this point you have the image_url value from the front end
    # Your job now is to send this information to the Clarifai API
    # and read the result, make sure that you read and understand the
    # example we covered in the slides! 
    headers = {'Authorization': 'Key 1755d1e5ec224dcd85e9b3f0c0ed3f35'}

    image_url = request.form['url-input']
    api_url = "https://api.clarifai.com/v2/models/aaa03c23b3724a16a56b629203edc62c/outputs"
    data ={"inputs": [
      {
        "data": {
          "image": {
            "url": image_url
          }
        }
      }
    ]}

    response = requests.post(api_url, headers=headers, data=json.dumps(data))
    
    if(response.content.find("people") >= 0):
    	is_people = "There are people in this photo!"
    else:
    	is_people = "There are no people in this photo!"

    return render_template('home.html', results=response.content, is_people = is_people)

if __name__ == '__main__':
    app.run(debug=True)