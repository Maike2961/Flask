from flask import Flask, render_template,request

app = Flask(__name__)

frutas=[]
registros=[]

@app.route("/", methods=["GET", "POST"])
def principal():
	#nome= 'maike abromowitz'
	#idade=15
	
	#frutas =[" morango","uva","laranja","mamao","maçã"]
	
	#Tratando a requisição

	#metodo é igual a post
	if request.method =="POST":
		#esta checando se o input do name fruta foi preenchido
		if request.form.get("fruta"):
			#capturando e incluindo na lista
			frutas.append(request.form.get("fruta"))
	return render_template("index.html",frutas=frutas)

	#nome=nome, idade=idade parametros para capturar as variaveis

@app.route("/sobre", methods=["GET", "POST"])
def sobre():
	#dicionario
	#notas = {"Fulano":5.0, "beltrano":6.0, "aluno":7.0,"sicrano":8.9}

	if request.method == "POST":
		if request.form.get("aluno") and request.form.get("nota"):
			#colocando em um dicionario
			registros.append({"aluno":request.form.get("aluno"), "nota": request.form.get("nota")})

	return render_template("sobre.html", registros=registros)

if __name__ == '__main__':
	app.run(debug=True)

#no prompt quando terminar use o codigo set FLASK_APP= nome do arquivo-app.py

#use set FLASK_ENV=development para atualizar alterações