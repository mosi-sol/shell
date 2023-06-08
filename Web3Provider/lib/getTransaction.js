import { web3Provider } from './web3Provider.js';

async function getTransaction(transactionHash) {
  try {
    // Get the transaction by hash
    const transaction = await web3Provider.provider.eth.getTransaction(transactionHash);

    // Return the transaction object
    return transaction;
  } catch (error) {
    console.error(error);
    throw new Error(`Failed to get transaction: ${error.message}`);
  }
}

export { getTransaction };

// to use:
// import { getTransaction } from './getTransaction.js';
