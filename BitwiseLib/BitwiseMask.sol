pragma solidity ^0.8.0;

library BitwiseMask {
    function setBit(uint256 mask, uint256 bit) internal pure returns (uint256) {
        return mask | (1 << bit);
    }

    function clearBit(uint256 mask, uint256 bit) internal pure returns (uint256) {
        return mask & ~(1 << bit);
    }

    function toggleBit(uint256 mask, uint256 bit) internal pure returns (uint256) {
        return mask ^ (1 << bit);
    }

    function isBitSet(uint256 mask, uint256 bit) internal pure returns (bool) {
        return (mask & (1 << bit)) != 0;
    }
}

// how to use
/*
pragma solidity ^0.8.0;
import "./BitwiseMask.sol";

contract FlagContract {
    using BitwiseMask for uint256;

    uint256 public flags;

    function setFlag(uint256 bit) public {
        flags = flags.setBit(bit);
    }

    function clearFlag(uint256 bit) public {
        flags = flags.clearBit(bit);
    }

    function toggleFlag(uint256 bit) public {
        flags = flags.toggleBit(bit);
    }

    function isFlagSet(uint256 bit) public view returns (bool) {
        return flags.isBitSet(bit);
    }
}
*/
