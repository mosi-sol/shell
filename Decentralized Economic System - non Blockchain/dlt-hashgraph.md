### Decentralized Economic System using a *Distributed Ledger Technology (DLT)* called Hashgraph and JavaScript:

1. Install the `@hashgraph/sdk` package:

```javascript
npm install @hashgraph/sdk
```

2. Import the necessary libraries:

```javascript
const { Client, Ed25519PrivateKey, AccountCreateTransaction } = require('@hashgraph/sdk')
```

3. Connect to the Hashgraph network using a client:

```javascript
const client = new Client({
  network: {
    address: 'https://api.testnet.myhbarwallet.com',
    // Replace `testnet` with `mainnet` for the main network
    networkName: 'testnet',
  },
})
```

4. Create a new account for the buyer:

```javascript
const buyerPrivateKey = await Ed25519PrivateKey.generate()
const buyerPublicKey = buyerPrivateKey.publicKey
const buyerAccount = await new AccountCreateTransaction()
  .setInitialBalance(0)
  .setKey(buyerPublicKey)
  .execute(client)
const buyerAddress = buyerAccount.accountId.toString()
```

5. Fund the buyer's account with some initial balance:

```javascript
await client.transferCryptoTo(buyerAddress, 1000)
```

6. Create a new account for the seller:

```javascript
const sellerPrivateKey = await Ed25519PrivateKey.generate()
const sellerPublicKey = sellerPrivateKey.publicKey
const sellerAccount = await new AccountCreateTransaction()
  .setInitialBalance(0)
  .setKey(sellerPublicKey)
  .execute(client)
const sellerAddress = sellerAccount.accountId.toString()
```

7. Fund the seller's account with some initial balance:

```javascript
await client.transferCryptoTo(sellerAddress, 0)
```

8. Create a new transaction:

```javascript
const txData = { item: 'Item for sale', price: 500 }
```

9. Sign the transaction using the seller's private key:

```javascript
const transaction = sellerPrivateKey.signTransaction({
  to: buyerAddress,
  amount: txData.price,
  data: JSON.stringify(txData),
})
```

10. Verify the transaction using the buyer's public key:

```javascript
const verified = buyerPublicKey.verifyTransaction(transaction)
if (verified) {
  await client.submitTransaction(transaction)
}
```

- Additional features: user authentication, rating systems, and dispute resolution.
