import { web3Provider } from './web3Provider.js';

async function connectToSmartContract(contractAddress, contractAbi) {
  try {
    // Create a new contract instance
    const contract = new web3Provider.provider.eth.Contract(contractAbi, contractAddress);

    // Return the contract instance
    return contract;
  } catch (error) {
    console.error(error);
    throw new Error(`Failed to connect to smart contract: ${error.message}`);
  }
}

export { connectToSmartContract };

// to use:
// import { connectToSmartContract } from './connectToSmartContract.js';
