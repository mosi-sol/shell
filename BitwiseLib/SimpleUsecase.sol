pragma solidity 0.8;

contract SafeTransaction {
    uint256 constant FLAG_APPROVED = 1;
    uint256 constant FLAG_LOCKED = 2;

    uint256 private flags;

    // Modifier to check if the transaction is allowed
    modifier onlyAllowed() {
        require(isFlagSet(FLAG_APPROVED), "Transaction not approved");
        require(!isFlagSet(FLAG_LOCKED), "Transaction is locked");
        _;
    }

    // Set the approved flag
    function approveTransaction() public {
        setFlag(FLAG_APPROVED);
    }

    // Lock the transaction
    function lockTransaction() public {
        setFlag(FLAG_LOCKED);
    }

    // Unlock the transaction
    function unlockTransaction() public {
        clearFlag(FLAG_LOCKED);
    }

    // Perform a safe transaction
    function performTransaction() public onlyAllowed {
        // Perform the desired actions here
        // ...
    }

    // Utility functions for bitwise operations
    function setFlag(uint256 flag) private {
        flags |= flag;
    }

    function clearFlag(uint256 flag) private {
        flags &= ~flag;
    }

    function isFlagSet(uint256 flag) private view returns (bool) {
        return (flags & flag) != 0;
    }
}
