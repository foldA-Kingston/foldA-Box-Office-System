<script>
  import { onMount } from "svelte";

  let paymentForm;

  onMount(() => {
    // Create and initialize a payment form object
    paymentForm = new SqPaymentForm({
      // Initialize the payment form elements

      //TODO: Replace with your sandbox application ID
      applicationId: "sandbox-sq0idb-n3DTC2UoLHrNI5aM_JfqhQ",
      inputClass: "sq-input",
      autoBuild: false,
      // Customize the CSS for SqPaymentForm iframe elements
      inputStyles: [
        {
          fontSize: "16px",
          lineHeight: "24px",
          padding: "16px",
          placeholderColor: "#a0a0a0",
          backgroundColor: "transparent"
        }
      ],
      // Initialize the credit card placeholders
      cardNumber: {
        elementId: "sq-card-number",
        placeholder: "Card Number"
      },
      cvv: {
        elementId: "sq-cvv",
        placeholder: "CVV"
      },
      expirationDate: {
        elementId: "sq-expiration-date",
        placeholder: "MM/YY"
      },
      postalCode: {
        elementId: "sq-postal-code",
        placeholder: "Postal"
      },
      // SqPaymentForm callback functions
      callbacks: {
        /*
         * callback function: cardNonceResponseReceived
         * Triggered when: SqPaymentForm completes a card nonce request
         */
        cardNonceResponseReceived: (errors, nonce, cardData) => {
          if (errors) {
            // Log errors from nonce generation to the browser developer console.
            console.error("Encountered errors:");
            errors.forEach(error => {
              console.error("  " + error.message);
            });
            alert(
              "Encountered errors, check browser developer console for more details"
            );
            return;
          }
          alert(`The generated nonce is:\n${nonce}`);
          //TODO: Replace alert with code in step 2.1
        }
      }
    });
    paymentForm.build();
  });

  $: onGetCardNonce = event => {
    // Don't submit the form until SqPaymentForm returns with a nonce
    event.preventDefault();
    // Request a nonce from the SqPaymentForm object
    paymentForm.requestCardNonce();
  };
</script>

<div id="form-container">
  <div id="sq-card-number" />
  <div class="third" id="sq-expiration-date" />
  <div class="third" id="sq-cvv" />
  <div class="third" id="sq-postal-code" />
  <button
    id="sq-creditcard"
    class="button-credit-card"
    on:click={onGetCardNonce}>
    Pay $1.00
  </button>
</div>
