<script>
	import { jwt, userId } from "../stores.js";
	import Panel from "../components/Panel.svelte";
	let newname = "";
	let newpassword = "";
	let newpasswordconfirm = "";
	const saveName = async () => {
		const result = await fetch(`http://localhost:5000/users/${$userId}/`,
		{
			mode: "cors",
			method: "PUT",
			headers: {
				"Content-Type": "application/json",
				Authorization: `Bearer ${$jwt}`
			},
        	body: JSON.stringify({
          		name : newname,
        	})
		})
	}
	const savePassword = async () => {
		const result = await fetch(`http://localhost:5000/users/${$userId}/`,
		{
			mode: "cors",
			method: "PATCH",
			headers: {
				"Content-Type": "application/json",
				Authorization: `Bearer ${$jwt}`
			},
			body: JSON.stringify({
				password : newpassword,
			})
		})
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
	.changename{
		background: transparent;
		color: #4045ed;
		font-style: italic;
	}
	.password{
		display: flex;
	}
	.changepassword{
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
			<h3>Name</h3>
			<input bind:value={newname}>
			<button class="changename" on:click={saveName}>
			<h3>Change name</h3>
			</button>
		</div>
	</div>
	<div class="password">
		<div class="left">
			<h3>New Password</h3>
			<input bind:value={newpassword}>
			<h3>Confirm Password</h3>
			<input bind:value={newpasswordconfirm}>
			{#if newpassword === newpasswordconfirm}
			<button class="changepassword" on:click={savePassword}>
			<h3>Change Password</h3>
			</button>
			{/if}
		</div>
	</div>
</div>
