let crypto;
try {
  crypto = require('node:crypto');
  // console.log("instaled! (common js)\n\n");
} catch (err) {
  console.error('crypto support is disabled!');
}

// =============================================

parm2 = 'https://github.com/mosi-sol/Solidity101/blob/main/collection-1/05.PhoneBook_Factory.sol';
parm1 = `
//SPDX-License-Identifier: MIT
pragma solidity 0.8;

/// @title                  {CRUD action} learn in phone-book training lesson - Factory
/// @author                 Mosi-Sol - @github
/// @notice                 You can use this contract for only the most basic simulation
/// @dev                    All function calls are currently implemented without side effects
/// @custom:experimental    this contract just for learning purposes.
/// @custom:detail          deploy -> setValid editor -> PhoneBookDB is address of new phonebook
/// @custom:why-factory     blockchain dev = less gas. factory present less gas...

import "./PhoneBookRefactore.sol";
// import "https://github.com/mosi-sol/Solidity101/blob/main/collection-1/03.PhoneBook_Refactor.sol"; // would same version (0.8)

contract PhoneBookFactory {
    // db of different phone book's
    PhoneBook[] public PhoneBookDB;
    uint id = 0;

    // generate new phonebook
    function CreateNewPhoneBook(string memory _phoneNumber) public {
        PhoneBook phoneBook = new PhoneBook(_phoneNumber);
        PhoneBookDB.push(phoneBook);
        setValid(id);
        id += 1;
    }

    // who can edit which phone book (deployer is the valid owner for edit)
    function setValid(uint256 _phoneBookIndex) private {
        PhoneBook(address(PhoneBookDB[_phoneBookIndex])).validUser(msg.sender); // not view, write
    }

    // same as address(this)
    function addressOwnerFactory(uint256 _phoneBookIndex) public view returns (address) {
        return PhoneBook(address(PhoneBookDB[_phoneBookIndex])).theOwner(); // read
    }

    // is valid to crud?
    function isValidEditor(uint256 _phoneBookIndex, address _user) public view returns (bool) {
        return PhoneBook(address(PhoneBookDB[_phoneBookIndex])).isValidUser(_user); // read
    }

    // i am valid to crud?
    function isValidEditor(uint256 _phoneBookIndex) public view returns (bool) {
        return PhoneBook(address(PhoneBookDB[_phoneBookIndex])).isValidUser(msg.sender); // read
    }
}
`;
// =============================================

function run() {
	console.log('================================== encrypt');
	simpleHash(parm1, parm2);
	console.log('\n================================== finish');
}

run();

// =====================================
function simpleHash(dataText, secText) {
	const data = dataText;
	const sec = secText;
	const secret = sec;  
	const hash = crypto.createHmac('sha256', secret)  
			   .update(data)  
			   .digest('hex');  
	console.log('\n\ncryptography hash: ', '0x'+hash);  
}

// =====================================
