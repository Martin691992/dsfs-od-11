<script>
	let { data } = $props();
	const { infos } = data;
	$inspect(infos);
</script>

<div>
	<h1>Prédisez le revenue de la location de votre voiture</h1>
	<select name="" id="">
		{#each infos.colors as couleur}
			<option value="">{couleur}</option>
		{/each}
	</select>
	<select name="" id="">
		{#each infos.car_type as type}
			<option value="">{type}</option>
		{/each}
	</select>
    <select name="" id="">
        {#each infos.models as model}
            <option value="">{model}</option>
        {/each}
	</select>
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
