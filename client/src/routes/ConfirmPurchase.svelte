<script>
  import { goto } from "@sapper/app";
  import { onMount } from "svelte";
  import { jwt, userId } from "../stores.js";
  let paymentForm;

  let subtotal = 0;
  let tax = 0;
  let total = 0;

  const refreshCart = async () => {
    const res = await fetch(
      `https://folda-box-office-system.herokuapp.com/users/${$userId}/cart/`,
      {
        mode: "cors",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${$jwt}`
        }
      }
    );
    if (res.ok) {
      const data = await res.json();
      subtotal = data.ticketSubTotal;
      tax = data.tax;
      total = data.totalPrice;
    } else {
      alert("Something went wrong. Please try again in a moment.");
    }
  };

  onMount(() => {
    refreshCart();
    // Create and initialize a payment form object
    paymentForm = new SqPaymentForm({
      // Initialize the payment form elements

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
            alert("Something went wrong. Please try again in a moment.");
            return;
          }
          fetch("https://folda-box-office-system.herokuapp.com/checkout/", {
            method: "POST",
            headers: {
              Accept: "application/json",
              "Content-Type": "application/json",
              Authorization: `Bearer ${$jwt}`
            },
            body: JSON.stringify({
              nonce: nonce
            })
          })
            .catch(err => {
              alert("Network error: " + err);
            })
            .then(response => {
              if (!response.ok) {
                return response
                  .text()
                  .then(errorInfo => Promise.reject(errorInfo));
              }
              return response.text();
            })
            .then(data => {
              goto("/PaymentSuccess");
            })
            .catch(err => {
              console.error(err);
              alert(
                "Payment failed to complete! Please try again in a moment."
              );
            });
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

<style>
  h2 {
    text-align: center;
  }
</style>

<h2>Complete ticket purchase</h2>
<div id="form-container">
  <div id="sq-card-number" />
  <div class="third" id="sq-expiration-date" />
  <div class="third" id="sq-cvv" />
  <div class="third" id="sq-postal-code" />
  <button
    id="sq-creditcard"
    class="button-credit-card"
    on:click={onGetCardNonce}>
    Pay ${total}
  </button>
</div>
