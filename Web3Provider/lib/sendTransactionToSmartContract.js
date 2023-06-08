import { web3Provider } from './web3Provider.js';

async function sendTransactionToSmartContract(contract, methodName, { from, gas, gasPrice, value, ...args }) {
  try {
    // Build the transaction object
    const transactionObject = {
      from,
      gas,
      gasPrice,
      value,
      to: contract.options.address,
      data: contract.methods[methodName](...args).encodeABI(),
    };

    // Send the transaction
    const transaction = await web3Provider.provider.eth.sendTransaction(transactionObject);

    // Return the transaction hash
    return transaction.transactionHash;
  } catch (error) {
    console.error(error);
    throw new Error(`Failed to send transaction to smart contract: ${error.message}`);
  }
}

export { sendTransactionToSmartContract };

// to use:
// import { connectToSmartContract } from './connectToSmartContract.js';
// import { sendTransactionToSmartContract } from './sendTransactionToSmartContract.js';
