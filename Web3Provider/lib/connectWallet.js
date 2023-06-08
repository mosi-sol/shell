import { web3Provider } from './web3Provider.js';

async function connectWallet() {
  try {
    // Request accounts from the connected wallet
    const accounts = await web3Provider.requestAccounts();

    // Return the first account
    return accounts[0];
  } catch (error) {
    console.error(error);
    throw new Error(`Failed to connect to wallet: ${error.message}`);
  }
}

export { connectWallet };

// to use:
// import { connectWallet } from './connectWallet.js';
