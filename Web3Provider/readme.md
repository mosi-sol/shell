## Web3 Provider | mosi edition
Use all these in "lib" folder - [here](https://github.com/mosi-sol/shell/tree/main/Web3Provider/lib).\
Mint dapp for example in [here](https://github.com/mosi-sol/shell/blob/main/Web3Provider/mint_nft_example.md).\
Mint dapp by signing message [here](https://github.com/mosi-sol/shell/blob/main/Web3Provider/mint_nft_by_signature.md).

#

### lib - provider:

- to use:
```js
import { web3Provider } from './Web3Provider.js';

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

- to use:
```js
import { showConnectedWallet } from './showConnectedWallet.js';

// Display the connected wallet
showConnectedWallet();
```

### connect by rpc:

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

