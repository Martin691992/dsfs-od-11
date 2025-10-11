<script>
	let { data } = $props();
	const { infos } = data;

	async function call() {
		const request = await fetch('/predict', {
			method: 'POST',
			headers: {
				'content-type': 'application/json'
			},
			body: JSON.stringify({
				model_key: 'Renault',
				mileage: 45000,
				engine_power: 90,
				fuel: 'diesel',
				paint_color: 'black',
				car_type: 'hatchback',
				private_parking_available: "True",
				has_gps: "True",
				has_air_conditioning: "True",
				automatic_car: "False",
				has_getaround_connect: "False",
				has_speed_regulator: "True",
				winter_tires: "False"
			})
		});
		const data = await request.json();
		console.log(data);
	}
</script>

<div>
	<h1>Bienvenue sur votre dashboard</h1>
	<button
		type="button"
		onclick={() => {
			call();
		}}>Requete</button
	>
</div>

<style>
	div {
		display: flex;
		flex-direction: column;
		width: 100%;
		margin-top: 4em;
		align-items: center;
		h1 {
			font-family: 'Poppins';
			font-size: clamp(1em, 3em, 3vw);
			color: rgba(0, 0, 0, 0.7);
		}
	}
</style>
