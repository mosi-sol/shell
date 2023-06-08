import { web3Provider } from './web3Provider.js';

async function sendTransaction({ from, to, value, gas, gasPrice, nonce, data, privateKey }) {
  try {
    // Build the transaction object
    const transactionObject = {
      from,
      to,
      value,
      gas,
      gasPrice,
      nonce,
      data,
    };

    // Sign the transaction with the private key
    const signedTransaction = await web3Provider.provider.eth.accounts.signTransaction(transactionObject, privateKey);

    // Send the signed transaction
    const transaction = await web3Provider.provider.eth.sendSignedTransaction(signedTransaction.rawTransaction);

    // Return the transaction hash
    return transaction.transactionHash;
  } catch (error) {
    console.error(error);
    throw new Error(`Failed to send transaction: ${error.message}`);
  }
}

export { sendTransaction };

// to use:
// import { sendTransaction } from './sendTransaction.js';
