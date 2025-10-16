<script>
	let { data } = $props();
	const { infos } = data;

</script>

<div>
	<h1>Bienvenue sur votre dashboard</h1>

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
