<script>
	let emaildefault='15ml81@queensu.ca';
	let passworddefault='abc';
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
	.emails{
		padding: 1rem;
	}
	.password{
		padding: 1rem;
	}
	.createaccount{
		background: transparent;
		color: #4045ed;
		font-style: italic;
	}
	.signinandcreate{
		padding: 1rem;
	}
	.signin{
		margin-right: 2rem;
	}

</style>
<svelte:head>
	<title>Signin</title>
</svelte:head>

<div>
<h1>Sign In</h1>
</div>
<div class="panel">
	<div class ="emails">
		<h3>Email</h3>
		<input value={emaildefault}>
	</div>
	<div class ="password">
		<h3>Password</h3>
		<input value={passworddefault}>
	</div>

	<div class ="signinandcreate">
		<button class="signin" onclick="location='Account'">
			<h3>Sign in</h3>
		</button>
		<button class="createaccount" onclick="location='CreateAccount'">
			<h3>Create Account</h3>
		</button>
	</div>
</div>
