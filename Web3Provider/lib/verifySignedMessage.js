import { web3Provider } from './web3Provider.js';

async function verifySignedMessage(message, signature, publicKey) {
  try {
    // Verify the signed message with the public key
    const recoveredAddress = await web3Provider.provider.eth.accounts.recover(message, signature.signature);

    // Check if the recovered address matches the provided public key
    const isVerified = (recoveredAddress.toLowerCase() === publicKey.toLowerCase());

    // Return the verification result
    return isVerified;
  } catch (error) {
    console.error(error);
    throw new Error(`Failed to verify signed message: ${error.message}`);
  }
}

export { verifySignedMessage };

// to use:
// import { signMessage } from './signMessage.js';
// import { verifySignedMessage } from './verifySignedMessage.js';
