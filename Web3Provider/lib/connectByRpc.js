import { web3Provider } from './web3Provider.js';

async function connectByRpc(rpcUrl) {
  try {
    // Set the provider to the RPC URL
    web3Provider.provider.setProvider(rpcUrl);

    // Get the chain ID
    const chainId = await web3Provider.getChainId();

    // Return the chain ID
    return chainId;
  } catch (error) {
    console.error(error);
    throw new Error(`Failed to connect to RPC: ${error.message}`);
  }
}

export { connectByRpc };

// to use:
// import { connectByRpc } from './connectByRpc.js';
