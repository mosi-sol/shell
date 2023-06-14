// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

import "./Bitwise.sol";
// import "./BitwiseAssembly.sol"; // no different to use

contract MyContract {

    using Bitwise for uint256;

    function testBitwise(uint256 a, uint256 b, uint256 mask) public pure returns (uint256) {
        uint256 result1 = a.and(b);
        uint256 result2 = a.or(b);
        uint256 result3 = a.xor(b);
        uint256 result4 = a.not();
        uint256 result5 = a.mask(mask);
        return result1 + result2 + result3 + result4 + result5;
    }
}
