<script>
	let firstname = '';
	let lastname = '';
	let email = '';
	let password = '';
	let confirmpassword ='';
	function handleCreate(){
		alert('Account saved')
	}
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
	.confirmpassword{
		padding: 1rem;
	}
	.createandsignin{
		padding: 1rem;
	}
	.signin{
		background: transparent;
		color: #4045ed;
		font-style: italic;
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
		<h3>Password</h3>
		<input value={password}>
	</div>
	<div class ="confirmpassword">
		<h3>Confirm Password</h3>
		<input value={confirmpassword}>
	</div>
	<div class ="createandsignin">
		<button class="create" on:click={handleCreate}>
			<h3>Create Account</h3>
		</button>
		<button class="signin" onclick="location='Signin'">
			<h3>Sign in</h3>
		</button>
	</div>
</div>
