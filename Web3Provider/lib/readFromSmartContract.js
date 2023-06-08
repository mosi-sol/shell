import { web3Provider } from './web3Provider.js';

async function readFromSmartContract(contract, methodName, ...args) {
  try {
    // Call the specified contract method with the given arguments
    const result = await contract.methods[methodName](...args).call();

    // Return the result
    return result;
  } catch (error) {
    console.error(error);
    throw new Error(`Failed to read from smart contract: ${error.message}`);
  }
}

export { readFromSmartContract };

// to use:
// import { connectToSmartContract } from './connectToSmartContract.js';
// import { readFromSmartContract } from './readFromSmartContract.js';
