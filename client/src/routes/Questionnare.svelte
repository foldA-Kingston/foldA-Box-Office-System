<script>
	let ans1 = 'urdhbvfhkdu';
	let ans2 = 'kdjvn,dfjrf';
	let ans3 = 'lkdejfhinvdhjf';
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
    .question{
        display: flex;
        font-style: italic;
    }
    .answer{
        flex: 1;
        align-items: left;
    }

</style>

<div>
    <h1>Thank you for your purchase!</h1>
    <h3>Please take a moment to fill out this form</h3>
    <div class="panel">
        <div class="question">
            <h4>*Q1</h4>
        </div>
        <div class="answer">
            <input value={ans1}>
        </div>
        <div class="question">
            <h4>*Q2</h4>
        </div>
        <div class="answer">
            <input value={ans2}>
        </div>
    </div>
</div>