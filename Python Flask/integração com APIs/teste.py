from flask import Flask, render_template,request
import urllib.request, json

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



@app.route("/filmes/<propriedade>")
def filmes(propriedade):

	if propriedade == 'populares':
		url = "https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=a0902d62734612f909956e9d4872faba"

	elif propriedade == 'kids':
		url = "https://api.themoviedb.org/3/discover/movie?certification_country=US&certification.lte=G&sort_by=popularity.desc&api_key=a0902d62734612f909956e9d4872faba"

	elif propriedade == '2010':
		url = "https://api.themoviedb.org/3/discover/movie?primary_release_year=2010&sort_by=vote_average.desc&api_key=a0902d62734612f909956e9d4872faba"

	elif propriedade == 'drama':
		url = "https://api.themoviedb.org/3/discover/movie?with_genres=18&sort_by=vote_average.desc&vote_count.gte=10&api_key=a0902d62734612f909956e9d4872faba"
	
	elif propriedade == 'tom':
		url = "https://api.themoviedb.org/3/discover/movie?with_genres=878&with_cast=500&sort_by=vote_average.desc&api_key=a0902d62734612f909956e9d4872faba"


	resposta = urllib.request.urlopen(url)

	dados = resposta.read()

	jsondata = json.loads(dados)

	return render_template('filmes.html', filmes=jsondata['results'])

if __name__ == '__main__':
	
	app.run(debug=True)

#no prompt quando terminar use o codigo set FLASK_APP= nome do arquivo-app.py

#use set FLASK_ENV=development para atualizar alterações
