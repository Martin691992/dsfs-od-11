<script>
	import favicon from '$lib/assets/favicon.svg';

	let { children } = $props();
</script>

<nav>
	<ul>
		<li>
			<a href="/">Acceuil</a>
		</li>
	</ul>
	<ul>
		<li>
			<a href="/docs">Documentation</a>
		</li>
		<li>
			<a href="/predictions">Prédire votre revenue</a>
		</li>
		<li>
			<a href="/infos">Informations</a>
		</li>
		<!-- <li>
			<a target="_blank" href="https://bonnardconsulting.fr">Bonnard Consulting</a>
		</li> -->
	</ul>
</nav>

{@render children?.()}
<footer>
	<p>2025 - Tous droits réservés BONNARD CONSULTING &copy</p>
</footer>

<style>
	nav {
		width: 100%;
		display: flex;
		padding: 2em 4em;
		box-shadow: 0px 3px 8px rgba(0, 0, 0, 0.10);
		margin-bottom: 2em;
		justify-content: space-between;
		ul {
			display: flex;
			gap: 2em;
			list-style: none;
			li {
				a {
					text-decoration: none;
					font-family: 'Poppins';
					color: rgba(0, 0, 0, 0.7);
					font-size: clamp(1em, 1.4em, 3vw);
					&:hover {
						color: brown;
					}
				}
			}
		}
	}
	footer{
		margin-top: auto;
		display: flex;
		justify-content: center;
		padding: 1em;
		p{
			font-family: "Poppins";
		}
	}
</style>
