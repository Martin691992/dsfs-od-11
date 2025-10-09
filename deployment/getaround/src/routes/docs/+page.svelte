<h1>Documentation</h1>
<div>
	<aside>
		<h3>Site :</h3>
		<ul>
			<li>
				<a href="#infos">Infos</a>
			</li>
			<li>
				<a href="#prediction">Prédiction</a>
			</li>
		</ul>

		<h3>API :</h3>
		<ul>
			<li>
				<a href="#api">/predict</a>
			</li>
		</ul>
	</aside>
	<article>
		<section id="infos">
			<h2>Infos sur la documentation</h2>
			<p>Vous pouvez retrouver ici toutes les informations sur cette application web.</p>
			<p>La rubrique de gauche vous permet de naviguer.</p>
		</section>
		<section id="prediction">
			<h2>Prédire le revenue de votre voiture</h2>
			<p>
				Liens vers la <a href="/predictions">prédiction des revenues de votre voiture</a>
			</p>
			<p>
				Grâce à cette page vous pourrez, en entrant les informations sur votre véhicule découvrir les potentiels revenues que vous pouvez générer.
			</p>
			<p>Liste des informations nécessaire : </p>
			<ul>
				<li>Modèle de votre voiture</li>
				<li>Kilometrage du véhicule</li>
				<li>Motorisation</li>
				<li>Puissance moteur</li>
				<li>Couleur</li>
				<li>Type de voiture</li>
				<li>Place de parking disponible ?</li>
				<li>G.P.S ?</li>
				<li>Climatisation ?</li>
				<li>Transmission ?</li>
				<li>Dispose de "Connect" ?</li>
				<li>Régulateur de vitesse ?</li>
				<li>Pneu Hiver ?</li>
			</ul>
		</section>
		<section id="api">
			<h2>API</h2>
			<h3>/predict</h3>
			<p>Descrition de notre API ouverte qui vous permettra de connaitre le revenue potentiel de votre voiture.</p>
			<div class="parametres">
				<p>Url : https://www.getaround.bonnardconsulting.fr/predict</p>
				<p>Méthode : POST</p>
			</div>
			<div class="parametres">
				<p>Cette route accepte des données au format JSON.</p>
				<p>Exemple d'input data : </p>
				<code>
						{'{'}
						"input": [[7.0, 0.27, 0.36, 20.7, 0.045, 45.0, 170.0, 1.001, 3.0, 0.45, 8.8], [7.0, 0.27, 0.36, 20.7, 0.045, 45.0, 170.0, 1.001, 3.0, 0.45, 8.8]]
						{'}'}
				</code>
			</div>
			<div class="parametres">
				<p>Exemples : </p>
				<span>CURL</span>
			</div>
		</section>

	</article>
</div>

<style scoped>
	h1 {
		font-family: 'Poppins';
		font-size: clamp(1em, 3em, 3vw);
		text-transform: uppercase;
		color: rgba(0, 0, 0, 0.7);
		text-align: center;
		margin-top: .5em;
	}
	div {
		display: grid;
		position: relative;
		width: 100%;
		height: 100%;
		grid-template-columns: 0.25fr 1fr;
		margin-top: 3em;
		aside{
			left: 0;
			display: block;
			padding: 2em;
			overflow-y: scroll;
			scroll-behavior: smooth;
			scrollbar-width: thin;
			height: 75vh;
			background-color: rgba(47, 162, 211, 0.1);
			h3{
				font-size: 2em;
				font-family: 'Poppins';
				margin: 1em 0 0.5em 0;
				color: rgba(0, 0, 0, 0.7);
			}
			ul{
				list-style: none;
				li{
					a{
						text-decoration: none;
						font-family: 'Poppins';
						font-size: clamp(.8em,1.2em,3vw);
						color: blue;
						transition: ease 0.2s;
						&:hover{
							color: red;
						}
					}
				}
			}
		}
		article{
			display: flex;
			flex-direction: column;
			gap: 5em;
			background-color: rgba(14, 147, 204, 0.1);
			padding: 2em;
			height: 75vh;
			overflow-y: scroll;
			scroll-behavior: smooth;
			scrollbar-width: thin;
			section{
				display: flex;
				flex-direction: column;
				gap: 1em;
				margin: 2em 0;
				h2{
					font-family: 'Poppins';
					font-size: clamp(1.5em,2.8em,3vw);
				}
				h3{
					font-family: 'Poppins';
					font-size: clamp(1.2em,1.8em,3vw);
					color: rgba(0, 0, 0, 0.5);
					padding: 0.5em ;
					background-color: rgba(0, 0, 0, 0.1);
					border-radius: 8px;
				}
				ul{
					padding: 0 2em;
					li{
						font-family: 'Poppins';
						font-size: clamp(.8em,1.2em,3vw);
						
					}
				}
				p{
					font-family: 'Poppins';
					font-size: clamp(.8em,1.2em,3vw);
				}
				.parametres{
					display: flex;
					flex-direction: column;
					margin: 0;
					code{
						font-family: "Poppins";
						background-color: #1e2939;
						padding: 1.5em 2em;
						border-radius: 8px;
						color: white;
						letter-spacing: 1.5px;
					}
				}
			}
		}
	}
</style>
