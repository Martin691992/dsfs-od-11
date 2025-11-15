<script>
	let { data } = $props();
	const { infos } = data;
</script>

<article>
	<h1>Bienvenue sur votre dashboard</h1>
	<div class="container">
		<div class="sous-container">
			<h2>Retards :</h2>
			<div class="line">
				<p>Retard moyen :</p>
				<p class="results">27.53 minutes</p>
			</div>
		</div>
		<div class="sous-container">
			<h2>Impact sur les réservations :</h2>
			<div class="line">
				<p>Nombre de réservations affectées par le retard</p>
				<p class="results">270 réservations</p>
			</div>
			<div class="line">
				<p>Revenus impacté :</p>
				<p class="results">32 130 €</p>
			</div>
			<i>Revenus median des utilisateurs : 119 € par reservations</i>
		</div>
		<div class="sous-container">
			<h2>Réservations 'mobile' :</h2>
			<div class="line">
				<p class="results">20.43%</p>
				<p>des reservations 'mobile' qui s'enchainent sont en retard</p>
			</div>
		</div>
		<div class="sous-container">
			<h2>Réservations 'connect' :</h2>
			<div class="line">
				<p class="results">11.73%</p>
				<p>des reservations 'connect' qui s'enchainent sont en retard</p>
			</div>
		</div>
	</div>
	<div class="container-img">
		<h2>Nombre de retards résolus selon les différents seuils :</h2>
		<img src="/newplot5.png" alt="" />
	</div>
		<div class="container-img">
		<h2>Nombre de réservations masquées en fonction du seuil :</h2>
		<img src="/newplot6.png" alt="" />
	</div>
	<div class="container-img">
		<h2>Informations sur les voitures à louer :</h2>
		<table>
			<thead>
				<tr>
					<th>Label</th>
					<th>Data</th>
				</tr>
			</thead>
			<tbody>
				<tr>
					<td>Nombre de voiture disponible</td>
					<td>4 843</td>
				</tr>
				<tr>
					<td>Prix moyen de location</td>
					<td>121,21 €</td>
				</tr>
				<tr>
					<td>Prix médian de location</td>
					<td>119 €</td>
				</tr>
				<tr>
					<td>Kilometrage moyen des voitures</td>
					<td>140 962 km</td>
				</tr>
			</tbody>
		</table>
	</div>
	<div class="container-img">
		<h2>Moyenne des prix par marque de voiture :</h2>
		<img src="/marque.png" alt="" />
	</div>
</article>

<style>
	article {
		display: flex;
		flex-direction: column;
		width: 100%;
		margin-top: 1em;
		padding: 2em;
		h1 {
			font-family: 'Poppins';
			font-size: clamp(1em, 3em, 3vw);
			color: rgba(0, 0, 0, 0.7);
			text-align: center;
		}
		.container {
			display: grid;
			grid-template-columns: 1fr 1fr;
			justify-items: center;
			padding: 1em 0;
			.sous-container {
				display: flex;
				flex-direction: column;
				width: 100%;
				max-width: 70%;
				h2 {
					font-family: var(--mainFont);
					color: var(--colorGetAround);
					margin-top: 1em;
				}
				i {
					font-family: var(--mainFont);
					font-size: 11px;
				}
				.line {
					display: flex;
					gap: 1em;
					font-family: var(--secondFont);
					.results {
						font-weight: 800;
						color: var(--secondColor);
					}
				}
			}
		}
		.container-img {
			display: flex;
			flex-direction: column;
			align-items: center;
			justify-content: center;
			margin-top: 2em;
			h2 {
				font-family: var(--mainFont);
				font-size: 32px;
				color: var(--secondColor);
				margin-top: 1em;
			}
			img {
				width: 60%;
			}
			table {
				font-family: var(--mainFont);
				margin-top: 2em;
				border-collapse: collapse;
				border: solid 1px rgba(0, 0, 0, 0.7);
				th{
					background-color: var(--colorGetAround);
					color: white;
				}
				th,
				td {
					border: solid 1px rgba(0, 0, 0, 0.7);
					padding: 5px 10px;
				}
			}
		}
	}
</style>
