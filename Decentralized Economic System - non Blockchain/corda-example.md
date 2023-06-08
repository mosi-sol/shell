### Trade in forex, using *Corda*
- **disclaimer**: this is just "proof of concept", so first your research and not use this example on product.
- more info about the **corda** [here](https://github.com/mosi-sol/shell/blob/main/Decentralized%20Economic%20System%20-%20non%20Blockchain/corda-example.md#corda-start-from-2016)
- "**const corda = require('corda-js');**" : this is fake, not valid.

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

---

#### Corda start from 2016
Corda is a **distributed ledger technology (DLT)** platform that is specifically designed for use in **business** and **financial applications**. It was developed by **R3**, a consortium of _over 200 financial institutions_, in collaboration with the _open-source community_.

Corda is designed to be a secure and efficient platform for managing complex financial agreements and transactions. It uses a unique approach to DLT called "shared ledger technology" that allows multiple parties to share a single, authoritative source of truth without requiring a global consensus mechanism.

Corda is built on top of a secure and scalable peer-to-peer network that enables secure communication and data exchange between nodes. It uses a "notary" service to provide transaction finality, which ensures that once a transaction has been committed to the ledger, it cannot be reversed or modified.

One of the key features of Corda is its support for "smart contracts", which are programmable agreements that can be executed automatically when certain conditions are met. Corda's smart contract language, called "Kotlin", is designed to be easy to use and allows developers to express complex financial logic in a simple and intuitive way.

Corda also provides a range of tools and APIs to make it easy to develop, deploy, and manage Corda networks. These include a command-line interface, a web-based user interface, and a range of developer tools and libraries.

Corda is a powerful and flexible platform for managing complex financial agreements and transactions. Its unique approach to DLT and support for smart contracts make it an ideal platform for use in a wide range of business and financial applications.
