<script>
  import { jwt, emailAddress, isAdmin, userId } from "../stores.js";
  /*
  const nodemailer = require("nodemailer").default;

  async function send() {
    console.log("did anything happen");
    // Generate test SMTP service account from ethereal.email
    // Only needed if you don't have a real mail account for testing
    let testAccount = await nodemailer.createTestAccount();

    // create reusable transporter object using the default SMTP transport
    
    var transporter  = {
    host: 'smtp.gmail.com',
    port: 465,
    secure: true, // use SSL
    auth: {
        user: 'cassidyhoulding@gmail.com',
        pass: '4Pinky55**'
    }
};
    var mailOptions = {
      from: '"Cassidy" <15cmh8@queensu.ca>', // sender address
      to: '15cmh8@queensu.ca',
      subject: "foldA Confirmation", // Subject line
      text: "This is your confirmation email", // plain text body
      html: "<b>Hello world?</b>" // html body
    };

    // send mail with defined transport object
    transporter.sendMail(mailOptions, function(error, info){
      if(error){
          return console.log(error);
      }
      console.log('Message sent: ' + info.response);
  });
}
*/
</script>
<style>
  div {
    text-align: center;
    font-size: 1.3rem;
  }
</style>

<div>
  Payment successful! Check your email for your tickets or
  <a href="/MyTickets">view them here</a>
  .
</div>
