<script>
	let firstname = 'barry';
	let lastname = 'liu';
	let email = '15ml81@queensu.ca';
</script>

<style>
	.panel{
		width: 40%;
		border-radius: 4px;
		border: 1px solid #333;
		overflow: hidden;
		margin: 1rem 0.5rem;
		padding: 0.5rem;
	}
	.name{
		display: flex;
	}
	.left{
		flex: 1;
		padding: 1rem;
	}
	.right{
		flex: 1;
		padding: 1rem;
	}
	.emails{
		padding: 1rem;
	}
	.passwordsetting{
		padding: 1rem;
	}
	.password{
		background: transparent;
		color: #4045ed;
		font-style: italic;
	}
	.saveandlogout{
		padding: 1rem;
	}
	.savechange{
		margin-right: 2rem;
	}

</style>
<svelte:head>
	<title>Account</title>
</svelte:head>

<div>
<h1>Account</h1>
</div>
<div class="panel">
	<div class="name">
		<div class="left">
			<h3>First Name</h3>
			<input value={firstname}>

		</div>
		<div class="right">
			<h3>Last Name</h3>
			<input value={lastname}>
		</div>
	</div>
	<div class ="emails">
		<h3>Email</h3>
		<input value={email}>
	</div>
	<div class ="passwordsetting">
		<button class="password">
			<h3>Change Password</h3>
		</button>
	</div>
	<div class ="saveandlogout">
		<button class="savechange">
			<h3>Save Changes</h3>
		</button>
		<button class="logout">
			<h3>Logout</h3>
		</button>
	</div>
</div>
