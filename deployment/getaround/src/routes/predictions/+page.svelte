<script>
	let { data } = $props();
	const { infos } = data;
	async function call() {
		const request = await fetch('/predict', {
			method: 'POST',
			headers: {
				'content-type': 'application/json'
			},
			body: JSON.stringify({input : to_predict})
		});
		console.log(JSON.stringify(to_predict))
		const data = await request.json();

		return data
	}
	let {
		model_car,
		fuel,
		paint_color,
		car_type,
		parking,
		gps,
		air,
		automatic_car,
		connect,
		regul,
		tires
	} = $state("");

	let { mileage, engine_power } = $state(0);

	let to_predict = $derived({
		model_key: model_car,
		mileage: mileage,
		engine_power: engine_power,
		fuel: fuel,
		paint_color: paint_color,
		car_type: car_type,
		private_parking_available: parking,
		has_gps: gps,
		has_air_conditioning: air,
		automatic_car: automatic_car,
		has_getaround_connect: connect,
		has_speed_regulator: regul,
		winter_tires: tires
	});
	let votre_prix = $state()
</script>

<div>
	<h1>Prédisez le revenue de la location de votre voiture</h1>
	{#if votre_prix}
		{#await votre_prix}
			<h3>... calcul de votre prix</h3>
		{:then prix} 
			<h1 class="revenue">Votre revenue serait de {prix} €</h1>
		{/await}
	{/if}
	<div class="container-infos">
		<div class="container-select">
			<h2>Votre modèle :</h2>
			<select bind:value={model_car} name="" id="">
				<option value="">- - -</option>
				{#each infos.models as model}
					<option value="{model}">{model}</option>
				{/each}
			</select>
			<h2>Kilométrage :</h2>
			<input bind:value={mileage} min="1" type="number" name="" id="">
			<h2>Puissance moteur :</h2>
			<input bind:value={engine_power} min="1" type="number" name="" id="">
			<h2>Type de carburant :</h2>
			<select bind:value={fuel} name="" id="">
				<option value="">- - -</option>
				{#each infos.fuel as fuel}
					<option value="{fuel}">{fuel}</option>
				{/each}
			</select>
			<h2>Couleur de votre voiture :</h2>
			<select bind:value={paint_color} name="" id="">
				<option value="">- - -</option>
				{#each infos.colors as couleur}
					<option value="{couleur}">{couleur}</option>
				{/each}
			</select>
			<h2>Type de véhicule :</h2>
			<select bind:value={car_type} name="" id="">
				<option value="">- - -</option>
				{#each infos.car_type as type}
					<option value="{type}">{type}</option>
				{/each}
			</select>
		</div>
		<div class="container-select">
			<h2>Avez-vous une place de parking privée ?</h2>
			<select bind:value={parking} name="" id="">
				<option value="True">Oui</option>
				<option value="False">Non</option>
			</select>
			<h2>Votre voiture a t'elle un GPS ?</h2>
			<select bind:value={gps} name="" id="">
				<option value="True">Oui</option>
				<option value="False">Non</option>
			</select>
			<h2>Votre voiture a t'elle l'air conditionnée ?</h2>
			<select bind:value={air} name="" id="">
				<option value="True">Oui</option>
				<option value="False">Non</option>
			</select>
			<h2>Votre voiture est-elle une automatique ?</h2>
			<select bind:value={automatic_car} name="" id="">
				<option value="True">Oui</option>
				<option value="False">Non</option>
			</select>
			<h2>Avez-vous le getAround Connect ?</h2>
			<select bind:value={connect} name="" id="">
				<option value="True">Oui</option>
				<option value="False">Non</option>
			</select>
			<h2>Votre voiture a t'elle un régulateur de vitesse ?</h2>
			<select bind:value={regul} name="" id="">
				<option value="True">Oui</option>
				<option value="False">Non</option>
			</select>
			<h2>Votre voiture a t'elle des pneus hiver ?</h2>
			<select bind:value={tires} name="" id="">
				<option value="True">Oui</option>
				<option value="False">Non</option>
			</select>
		</div>
	</div>
	<button onclick="{()=>votre_prix = call()}" type="button">Prédire votre revenue</button>
</div>

<style>
	div {
		display: flex;
		flex-direction: column;
		width: 100%;
		margin-top: 4em;
		align-items: center;
		justify-content: center;
		h1 {
			font-family: 'Poppins';
			font-size: clamp(1em, 3em, 3vw);
			color: #b52aad;
			&.revenue{
				color: brown;
				margin-top: 1em;
			}
		}
		h3{
			margin-top: 2em;
			font-family: 'Poppins';
			font-size: clamp(.5em, 1em, 3vw);
		}
		.container-infos {
			max-width: 50%;
			.container-select {
				padding: 1em 2em;
				display: grid;
				grid-template-columns:auto 1fr;
				column-gap: 2em;
				row-gap: 1em;

				border-radius: 8px;
				h2{
					font-family: 'Poppins';
					font-size: clamp(.8em, 1.5em, 3vw);
					color: #b52aad;
				}
				select, input{
					cursor: pointer;
					padding: 0.5em;
					font-family: 'Poppins';
					font-size: clamp(.5em, 1em, 3vw);
					border-radius: 8px;
					background-color: rgba(181, 42, 173, 0.05);
					border: solid 1px #b52aad;
				}
			}
		}
		button{
			padding: 1em 2em;
			margin-top: 3em;
			font-family: 'Poppins';
			font-size: clamp(.5em, 1em, 3vw);
			cursor: pointer;
			border-radius: 8px;
			transition: ease 0.2s;
			&:hover{
				background-color: rgba(0, 0, 0, 0.2);
			}
		}
	}
</style>
