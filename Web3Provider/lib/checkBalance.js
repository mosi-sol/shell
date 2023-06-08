import { web3Provider } from './web3Provider.js';

async function checkBalance(address) {
  try {
    // Get the balance of the address
    const balance = await web3Provider.provider.eth.getBalance(address);

    // Convert the balance to Ether
    const balanceInEther = web3Provider.provider.utils.fromWei(balance, 'ether');

    // Return the balance in Ether
    return balanceInEther;
  } catch (error) {
    console.error(error);
    throw new Error(`Failed to check balance: ${error.message}`);
  }
}

export { checkBalance };

// to use:
// import { checkBalance } from './checkBalance.js';
