// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

contract SimpleStorage {
    uint256 favorateNumber;

    struct People {
        uint256 favorateNumber;
        string name;
    }

    People persion = People({favorateNumber: 2, name: "JoJo"});

    People[] public people;
    mapping(string => uint256) public nameToFavoriteNubmer;

    function store(uint256 _favoreiteNumber) public {
        favorateNumber = _favoreiteNumber;
    }

    function retrieve() public view returns (uint256) {
        return favorateNumber;
    }

    function addPersion(string memory _name, uint256 _favoreiteNumber) public {
        people.push(People(_favoreiteNumber, _name));
        nameToFavoriteNubmer[_name] = _favoreiteNumber;
    }
}
