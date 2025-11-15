<script>
	let { data } = $props();
	const { infos } = data;
</script>

<article>
	<h1>Bienvenue sur votre dashboard</h1>
	<div class="container">
		<h2>Métriques :</h2>
		<div class="line">
			<p>Nombre de réservations afféctées par le retard</p>
			<p>270 réservations</p>
		</div>
		<div class="line">
			<p>Revenus impacté :</p>
			<p>32 130 €</p>
		</div>
		<i>Revenus median des utilisateurs : 119 € par reservations</i>
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
		}
		.container {
			display: flex;
			flex-direction: column;
			width: 100%;
			.line {
				display: flex;
			}
		}
	}
</style>
