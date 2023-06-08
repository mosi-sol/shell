import { web3Provider } from './web3Provider.js';

async function callContractFunction(contractAddress, functionName, functionArguments) {
  try {
    // Get the contract instance
    const contractInstance = new web3Provider.provider.eth.Contract(contractAbi, contractAddress);

    // Call the function on the contract
    const result = await contractInstance.methods[functionName](...functionArguments).call();

    // Return the result
    return result;
  } catch (error) {
    console.error(error);
    throw new Error(`Failed to call contract function: ${error.message}`);
  }
}

export { callContractFunction };

// to use:
// import { callContractFunction } from './callContractFunction.js';
