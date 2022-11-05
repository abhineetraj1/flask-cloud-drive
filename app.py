from flask import *
from flask import render_template, send_file
import shutil, os, datetime, random

app = Flask(__name__, static_folder="static", template_folder="template")

def rf(a):
	return open(a,"r").read()

@app.route("/",methods=["GET"])
def main():
	return render_template("index.html")

@app.route("/sign_up", methods=["GET","POST"])
def main2():
	if (request.method == "GET"):
		return render_template("signup.html", message="")
	else:
		w = [request.form["username"], request.form["password"], request.form["email"], request.form["name"]]
		if (w[0] in os.listdir("profiles")):
			return render_template("signup.html", message="Account already exists")
		else:
			os.mkdir("profiles/"+w[0])
			open("profiles/"+w[0]+"/password","w").write(w[1])
			open("profiles/"+w[0]+"/email","w").write(w[2])
			open("profiles/"+w[0]+"/name","w").write(w[3])
			os.mkdir("profiles/"+w[0]+"/files")
			return render_template("dashboard.html", name=w[3], files=[], password=w[1], username=w[0], space=0, nf=0)

@app.route("/sign_in", methods=["GET","POST"])
def main3():
	if (request.method == "GET"):
		return render_template("signin.html", message="")
	else:
		w = [request.form["username"], request.form["password"]]
		if (w[0] in os.listdir("profiles")):
			if (w[1] == rf("profiles/"+w[0]+"/password")):
				files = []
				space=0
				for i in os.listdir("profiles/"+w[0]+"/files"):
					files.append({"name":i,"size":str(round(os.path.getsize("profiles/"+w[0]+"/files/"+i)/1024/1024))+" mb"})
					space = space+os.path.getsize("profiles/"+w[0]+"/files/"+i)/1024/1024
				email = rf("profiles/"+w[0]+"/email")
				name = rf("profiles/"+w[0]+"/name")
				password=rf("profiles/"+w[0]+"/password")
				return render_template("dashboard.html", name=name, files=files, password=password, username=w[0], space=round(space), nf=len(files))
			else:
				return render_template("signin.html",message="Wrong password")
		else:
			return render_template("signin.html", message="No such accounts")

@app.route("/upload/<user>/<pas>/file", methods=["POST"])
def main4(user, pas):
	if (request.method == "POST"):
		w = [user,pas]
		if (w[0] in os.listdir("profiles")):
			if (w[1] == rf("profiles/"+w[0]+"/password")):
				fles = request.files.getlist("files[]")
				for i in fles:
					i.save("profiles/"+w[0]+"/files/"+i.filename)
				files = []
				space=0
				for i in os.listdir("profiles/"+w[0]+"/files"):
					files.append({"name":i,"size":str(round(os.path.getsize("profiles/"+w[0]+"/files/"+i)/1024/1024))+" mb"})
					space = space+os.path.getsize("profiles/"+w[0]+"/files/"+i)/1024/1024
				email = rf("profiles/"+w[0]+"/email")
				name = rf("profiles/"+w[0]+"/name")
				password=rf("profiles/"+w[0]+"/password")
				return render_template("dashboard.html", name=name, files=files, password=password, username=w[0], space=round(space), nf=len(files))
			else:
				return ""
		else:
			return ""

@app.route("/delete/<user>/<pas>/name/<name>", methods=["GET"])
def main5(user, pas, name):
	if (request.method == "GET"):
		w = [user,pas]
		if (w[0] in os.listdir("profiles")):
			if (w[1] == rf("profiles/"+w[0]+"/password")):
				if (name in os.listdir("profiles/"+w[0]+"/files")):
					os.remove("profiles/"+w[0]+"/files/"+name)
				files = []
				space=0
				for i in os.listdir("profiles/"+w[0]+"/files"):
					files.append({"name":i,"size":str(round(os.path.getsize("profiles/"+w[0]+"/files/"+i)/1024/1024))+" mb"})
					space = space+os.path.getsize("profiles/"+w[0]+"/files/"+i)/1024/1024
				email = rf("profiles/"+w[0]+"/email")
				name = rf("profiles/"+w[0]+"/name")
				password=rf("profiles/"+w[0]+"/password")
				return render_template("dashboard.html", name=name, files=files, password=password, username=w[0], space=round(space), nf=len(files))
			else:
				return ""
		else:
			return ""
@app.route("/download/<user>/<pas>/name/<name>", methods=["GET"])
def main5(user, pas, name):
	if (request.method == "GET"):
		w = [user,pas]
		if (w[0] in os.listdir("profiles")):
			if (w[1] == rf("profiles/"+w[0]+"/password")):
				if (name in os.listdir("profiles/"+w[0]+"/files")):
					return send_file("profiles/"+w[0]+"/files/"+name)
			else:
				return ""
		else:
			return ""

@app.errorhandler(404)
def main10(e):
	return render_template("404.html")

if __name__ == '__main__':
	app.run()