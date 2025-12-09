from flask import Flask, render_template, request, Response
import requests
app = Flask(__name__)


@app.route("/")
def index():
    return render_template('home.html')

@app.route("/Home")
def home():
    return render_template('home.html')

@app.route("/About")
def about():
    return render_template('About.html')

@app.route("/Contact")
def contact():
    return render_template('Contact.html')

@app.route('/Services/pdf')    
def page():
    return render_template('pdf.html')
   

@app.route('/Services/pdf/Url')    
def services():
    try:
        # Get the URL parameter from the request
        url = request.args.get("url")

        if not url:
            return Response("Think ? is something missing", status=400)

        # Send a GET request to the provided URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Set response headers (optional)

            # Return the content of the URL as a response
            return Response(response.content, status=200)

        # Handle other status codes (e.g., 404, 500)
        else:
            return Response("Error: Request to URL failed with status code " + str(response.status_code), status=response.status_code)

    except Exception as e:
        # Handle exceptions (e.g., network errors, invalid URLs)
        return Response("Error: " + str(e), status=500)





# while making EC2 make sure instance metadata is available and imdsv2 is optional
# securitygroup all traffic allowing instance
# sudo yum install -y git
# git clone https://github.com/anuragmishr06/ec2-app-lab.git
# cd seasides-cloud-ec2-lab/
# python3 -m venv lab-venv 
# source lab-venv/bin/activate
# pip3 install -r requirements.txt
# curl http://169.254.169.254/latest/meta-data/local-ipv4| grep -E '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}' > p-ip
# python3 -m flask run --host=0.0.0.0 --port=8001
# nohup python3 -m flask run --host=0.0.0.0 --port=8001 &
# ps aux | grep "python3 -m flask run"
# kill <PID>


# url=http://169.254.169.254/latest/meta-data/identity-credentials/ec2/security-credentials/ec2-instance"
