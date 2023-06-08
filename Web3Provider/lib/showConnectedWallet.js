import { web3Provider } from './web3Provider.js';

async function getConnectedWallet() {
  try {
    // Request accounts from the connected wallet
    const accounts = await web3Provider.requestAccounts();

    // Return the first account
    return accounts[0];
  } catch (error) {
    console.error(error);
    throw new Error(`Failed to get connected wallet: ${error.message}`);
  }
}

function showConnectedWallet() {
  // Get the connected wallet
  const connectedWallet = getConnectedWallet();

  // Display the connected wallet
  console.log(`Connected wallet: ${connectedWallet}`);
}

export { showConnectedWallet };

// to use:
// import { showConnectedWallet } from './showConnectedWallet.js';
