### Trade in forex, using **corda**
- **disclaimer**: this is just "proof of concept", so first your research and not use this example on product.

```js
const corda = require('corda-js');
const { CordaClient } = corda;
const { CordaNodeAPI } = corda.nodeapi;

const client = new CordaClient();
const api = new CordaNodeAPI(client);

// Define the necessary variables for the forex transaction
const buyer = "O=Buyer,L=London,C=GB";
const seller = "O=Seller,L=New York,C=US";
const baseCurrency = "USD";
const quoteCurrency = "EUR";
const amount = 1000;
const exchangeRate = 1.20;

// Define the transaction proposal
const proposal = {
  buyer: buyer,
  seller: seller,
  baseCurrency: baseCurrency,
  quoteCurrency: quoteCurrency,
  amount: amount,
  exchangeRate: exchangeRate
};

// Send the proposal to the relevant parties for review and approval
const buyerResponse = await sendProposal(proposal, buyer);
const sellerResponse = await sendProposal(proposal, seller);

// Sign the transaction using our private key
const privateKey = "1234567890abcdef";
const signature = signTransaction(proposal, privateKey);

// Submit the signed transaction to the Corda network for processing and verification
const result = await api.submitTransaction(signature);

// Verify that the transaction was successful
const transaction = await api.getTransaction(result.id);

if (transaction.status == 'COMMITTED') {
  console.log('Transaction was successful!');
} else {
  console.log('Transaction failed. Please check the logs for details.');
}

// Helper function to send the transaction proposal to a party
async function sendProposal(proposal, party) {
  const builder = api.createTransactionBuilder();
  const proposalState = new ProposalState(proposal);
  builder.addOutputState(proposalState);
  builder.addCommand("com.example.proposal.commands.Propose", [party]);
  const signedTx = await api.signTransaction(builder.toTransaction());
  const result = await api.submitTransaction(signedTx);
  return result;
}

// Helper function to sign the transaction using a private key
function signTransaction(proposal, privateKey) {
  const builder = api.createTransactionBuilder();
  const proposalState = new ProposalState(proposal);
  builder.addInputState(proposalState);
  builder.addOutputState(new ForexState(buyer, seller, baseCurrency, quoteCurrency, amount, exchangeRate));
  builder.addCommand("com.example.forex.commands.Execute", [buyer, seller]);
  const unsignedTx = builder.toTransaction();
  const signedTx = unsignedTx.signWithPrivateKey(privateKey);
  return signedTx;
}

// Define the proposal state for the forex transaction
class ProposalState {
  constructor(proposal) {
    this.proposal = proposal;
  }
}

// Define the forex state for the completed transaction
class ForexState {
  constructor(buyer, seller, baseCurrency, quoteCurrency, amount, exchangeRate) {
    this.buyer = buyer;
    this.seller = seller;
    this.baseCurrency = baseCurrency;
    this.quoteCurrency = quoteCurrency;
    this.amount = amount;
    this.exchangeRate = exchangeRate;
  }
}
```

#### the result:
```js
// Verify that the transaction was successful
const transaction = await api.getTransaction(result.id);

if (transaction.status == 'COMMITTED') {
  console.log('Transaction was successful!');
  console.log('Transaction ID:', result.id);

  // Log the details of the completed forex transaction
  const outputState = transaction.outputs[0].data;
  console.log('Completed Forex Transaction Details:');
  console.log('Buyer:', outputState.buyer);
  console.log('Seller:', outputState.seller);
  console.log('Base Currency:', outputState.baseCurrency);
  console.log('Quote Currency:', outputState.quoteCurrency);
  console.log('Amount:', outputState.amount);
  console.log('Exchange Rate:', outputState.exchangeRate);
} else {
  console.log('Transaction failed. Please check the logs for details.');
}
```
