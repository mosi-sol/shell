import { web3Provider } from './web3Provider.js';

async function signMessage(message, privateKey) {
  try {
    // Sign the message with the private key
    const signature = await web3Provider.provider.eth.accounts.sign(message, privateKey);

    // Return the signature
    return signature;
  } catch (error) {
    console.error(error);
    throw new Error(`Failed to sign message: ${error.message}`);
  }
}

export { signMessage };

// to use:
// import { signMessage } from './signMessage.js';
