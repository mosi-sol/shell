## Web3 Provider | mosi edition
Use all these in "lib" folder.\
Mint dapp for example in [this folder](https://github.com/mosi-sol/shell/blob/main/Web3Provider/mint_nft_example.md).

#

### lib:
```js
class Web3Provider {
  constructor(provider) {
    this.provider = provider;
    this.requestId = 1;
  }

  async sendAsync(payload) {
    const id = this.requestId++;
    const message = {
      id,
      jsonrpc: '2.0',
      ...payload,
    };

    return new Promise((resolve, reject) => {
      this.provider.sendAsync(message, (err, response) => {
        if (err) {
          reject(err);
        } else {
          resolve(response.result);
        }
      });
    });
  }

  async send(method, params) {
    const payload = {
      method,
      params,
    };

    return this.sendAsync(payload);
  }

  async requestAccounts() {
    return this.send('eth_requestAccounts', []);
  }

  async getChainId() {
    return this.send('eth_chainId', []);
  }

  async getBlockNumber() {
    return this.send('eth_blockNumber', []);
  }

  async getBalance(address, blockNumber = 'latest') {
    return this.send('eth_getBalance', [address, blockNumber]);
  }

  async getTransactionCount(address, blockNumber = 'latest') {
    return this.send('eth_getTransactionCount', [address, blockNumber]);
  }

  async sendTransaction(tx) {
    return this.send('eth_sendTransaction', [tx]);
  }

  async getTransactionReceipt(txHash) {
    return this.send('eth_getTransactionReceipt', [txHash]);
  }

  async call(tx) {
    return this.send('eth_call', [tx]);
  }
}

const web3Provider = new Web3Provider(window.ethereum);
```

- example:
```js
async function init() {
  const accounts = await web3Provider.requestAccounts();
  const chainId = await web3Provider.getChainId();
  const blockNumber = await web3Provider.getBlockNumber();
  const balance = await web3Provider.getBalance(accounts[0]);
  const txCount = await web3Provider.getTransactionCount(accounts[0]);
  const txHash = await web3Provider.sendTransaction({
    from: accounts[0],
    to: '0x...',
    value: '1000000000000000000',
  });
  const receipt = await web3Provider.getTransactionReceipt(txHash);
  const result = await web3Provider.call({
    to: '0x...',
    data: '0x...',
  });
}

init();
```

### connect to wallet:
```js
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
```
- to use:
```js
import { connectWallet } from './connectWallet.js';

async function init() {
  try {
    // Connect to the wallet
    const account = await connectWallet();
    console.log(`Connected to wallet with account: ${account}`);
  } catch (error) {
    console.error(error);
  }
}

init();
```

### show connected wallet:
```js
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
```
- to use:
```js
import { showConnectedWallet } from './showConnectedWallet.js';

// Display the connected wallet
showConnectedWallet();
```

### connect by rpc:
```js
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
```
- to use:
```js
import { connectByRpc } from './connectByRpc.js';

async function init() {
  try {
    // Connect to the remote node via RPC
    const chainId = await connectByRpc('https://mainnet.infura.io/v3/YOUR_PROJECT_ID');
    console.log(`Connected to RPC with chain ID: ${chainId}`);
  } catch (error) {
    console.error(error);
  }
}

init();
```

### connect to smartcontract:
```js
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
```
- to use:
```js
import { connectToSmartContract } from './connectToSmartContract.js';

async function init() {
  try {
    // Connect to the smart contract
    const contractAddress = '0x...';
    const contractAbi = [ ... ];
    const contract = await connectToSmartContract(contractAddress, contractAbi);
    console.log(`Connected to smart contract at address: ${contractAddress}`);
    
    // Call a method on the contract
    const result = await contract.methods.methodName().call();
    console.log(`Result of method call: ${result}`);
  } catch (error) {
    console.error(error);
  }
}

init();
```

### read from smartcontract:
```js
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
```
- to use:
```js
import { connectToSmartContract } from './connectToSmartContract.js';
import { readFromSmartContract } from './readFromSmartContract.js';

async function init() {
  try {
    // Connect to the smart contract
    const contractAddress = '0x...';
    const contractAbi = [ ... ];
    const contract = await connectToSmartContract(contractAddress, contractAbi);
    console.log(`Connected to smart contract at address: ${contractAddress}`);
    
    // Read data from the contract
    const result = await readFromSmartContract(contract, 'methodName', arg1, arg2, ...);
    console.log(`Result of read from smart contract: ${result}`);
  } catch (error) {
    console.error(error);
  }
}

init();
```

### transaction on smartcontract:
```js
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
```
- to use:
```js
import { connectToSmartContract } from './connectToSmartContract.js';
import { sendTransactionToSmartContract } from './sendTransactionToSmartContract.js';

async function init() {
  try {
    // Connect to the smart contract
    const contractAddress = '0x...';
    const contractAbi = [ ... ];
    const contract = await connectToSmartContract(contractAddress, contractAbi);
    console.log(`Connected to smart contract at address: ${contractAddress}`);
    
    // Send a transaction to the contract
    const transactionObject = {
      from: '0x...',
      gas: 500000,
      gasPrice: 10000000000,
      value: 0,
    };
    const transactionHash = await sendTransactionToSmartContract(contract, 'methodName', transactionObject);
    console.log(`Transaction hash: ${transactionHash}`);
  } catch (error) {
    console.error(error);
  }
}

init();
```

### sign message:
```js
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
```
- to use:
```js
import { signMessage } from './signMessage.js';

async function init() {
  try {
    // Sign a message with a private key
    const message = 'Hello, world!';
    const privateKey = '0x...';
    const signature = await signMessage(message, privateKey);
    console.log(`Signature: ${signature.signature}`);
  } catch (error) {
    console.error(error);
  }
}

init();
```

### verify signed message
```js
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
```
- to use:
```js
import { signMessage } from './signMessage.js';
import { verifySignedMessage } from './verifySignedMessage.js';

async function init() {
  try {
    // Sign a message with a private key
    const message = 'Hello, world!';
    const privateKey = '0x...';
    const signature = await signMessage(message, privateKey);
    console.log(`Signature: ${signature.signature}`);

    // Verify the signed message with a public key
    const publicKey = '0x...';
    const isVerified = await verifySignedMessage(message, signature, publicKey);
    console.log(`Verification result: ${isVerified}`);
  } catch (error) {
    console.error(error);
  }
}

init();
```

### send transaction:
```js
import { web3Provider } from './web3Provider.js';

async function sendTransaction({ from, to, value, gas, gasPrice, nonce, data, privateKey }) {
  try {
    // Build the transaction object
    const transactionObject = {
      from,
      to,
      value,
      gas,
      gasPrice,
      nonce,
      data,
    };

    // Sign the transaction with the private key
    const signedTransaction = await web3Provider.provider.eth.accounts.signTransaction(transactionObject, privateKey);

    // Send the signed transaction
    const transaction = await web3Provider.provider.eth.sendSignedTransaction(signedTransaction.rawTransaction);

    // Return the transaction hash
    return transaction.transactionHash;
  } catch (error) {
    console.error(error);
    throw new Error(`Failed to send transaction: ${error.message}`);
  }
}

export { sendTransaction };
```
- to use:
```js
import { sendTransaction } from './sendTransaction.js';

async function init() {
  try {
    // Send a transaction to an address
    const transactionObject = {
      from: '0x...',
      to: '0x...',
      value: 1000000000000000000,
      gas: 500000,
      gasPrice: 10000000000,
      nonce: 0,
      data: '',
    };
    const privateKey = '0x...';
    const transactionHash = await sendTransaction({ ...transactionObject, privateKey });
    console.log(`Transaction hash: ${transactionHash}`);
  } catch (error) {
    console.error(error);
  }
}

init();
```

### get transaction:
```js
import { web3Provider } from './web3Provider.js';

async function getTransaction(transactionHash) {
  try {
    // Get the transaction by hash
    const transaction = await web3Provider.provider.eth.getTransaction(transactionHash);

    // Return the transaction object
    return transaction;
  } catch (error) {
    console.error(error);
    throw new Error(`Failed to get transaction: ${error.message}`);
  }
}

export { getTransaction };
```
- to use:
```js
import { getTransaction } from './getTransaction.js';

async function init() {
  try {
    // Get a transaction by hash
    const transactionHash = '0x...';
    const transaction = await getTransaction(transactionHash);
    console.log(`Transaction: ${JSON.stringify(transaction, null, 2)}`);
  } catch (error) {
    console.error(error);
  }
}

init();
```

### check balance:
```js
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
```
- to use:
```js
import { checkBalance } from './checkBalance.js';

async function init() {
  try {
    // Check the balance of an address
    const address = '0x...';
    const balance = await checkBalance(address);
    console.log(`Balance: ${balance} ETH`);
  } catch (error) {
    console.error(error);
  }
}

init();
```

### call:
```js
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
```
- to use:
```js
import { callContractFunction } from './callContractFunction.js';

async function init() {
  try {
    // Call a function on a contract
    const contractAddress = '0x...';
    const functionName = 'myFunction';
    const functionArguments = [1, 2, 3];
    const result = await callContractFunction(contractAddress, functionName, functionArguments);
    console.log(`Result: ${result}`);
  } catch (error) {
    console.error(error);
  }
}

init();
```

