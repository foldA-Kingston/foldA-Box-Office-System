<svelte:head>
	<title>Day Pass</title>
</svelte:head>

<head>
	<style>
	table, th, td {
  	border: 1px solid black;
		border-collapse: collapse;
	}
	</style>
</head>

<h2>Day Passes</h2>

<body>
	<table>
		<tr>
			<th colspan="5"> <div align="left">Select</div></th>
		</tr>
		<tr>
			<td>
				<form>
					<input type="checkbox" name="Event1" value="Event Name">
				</form>
			</td>
			<td>Event Name 1<br>Artist Name 1</td>
			<td>12:00 PM</td>
			<td>
				<form>
					<input type="button" name="Remove" value="Remove">
				</form>
			</td>
		</tr>
		<tr>
			<td>
				<form>
					<input type="checkbox" name="Event1" value="Event Name">
				</form>
			</td>
			<td>Event Name 1<br>Artist Name 1</td>
			<td>12:00 PM</td>
			<td>
				<form>
					<input type="button" name="Remove" value="Remove">
				</form>
			</td>
		</tr>
		<tr>
			<td>
				<form>
					<input type="checkbox" name="Event1" value="Event Name">
				</form>
			</td>
			<td>Event Name 1<br>Artist Name 1</td>
			<td>12:00 PM</td>
			<td>
				<form>
					<input type="button" name="Remove" value="Remove">
				</form>
			</td>
		</tr>
	</table>
	<table>
		<tr>
			<th colspan="5">Schedule</th>
		</tr>
		<tr>
			<td>Time</td>
			<td>Event</td>
		</tr>
		<tr>
			<td>9:00 AM</td>
			<td>Event No. 1</td>
		</tr>
	</table>
</body>