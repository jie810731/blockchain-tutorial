# Solidity, Blockchain, and Smart Contract Course – Beginner to Expert Python Tutorial

[youtube 網址](https://www.youtube.com/watch?v=M576WGiDBdQ)

## 建立乙太網測試帳號

建立乙太網測試帳號  
[rinkeby](https://faucet.rinkeby.io)

Faucet: 區塊測試網路
Gas:measure of computation use(計算的單位)  
Gas Price : How much it costs per unit of gas 每單位的價錢  
Gas Limit: max mount of gas in a transaction 最高願意付的 gas 費用  
transaction Fee : gas Used X Gas price  
Genesis Block:The First block in a black chain 區塊鏈中第一個 block

## Solidty

[remix ide](https://remix.ethereum.org)

不產生一個 transaction
view function : 回傳屬性 不改變狀態(no transaction)  
pure function : 計算數學方法不改變狀態(no transaction)

### struct

類似 Object 的資料型態
ex:
People public persion = People({
favorateNumber:2,
name:"JoJo"
});

### memory vs storage

memory:只在 function 執行直存在
storage:function 執行結束也還存在

### mapping

類似 Object 的資料型態,透過 key 找 value
ex:
mapping(string=>uint256) public nameToFavoriteNubmer;
use:
nameToFavoriteNubmer[_name]=\_favoreiteNumber;

### 繼承

is
ex:
contract StorageFacroty is SimpleStorage{}

### payable(付錢)

key word :payable
key word :msg.sender
key word :msg.value
ex:
function fund() public payable{
addressToAmountFunded[msg.sender] += msg.value;
}

### modifire

    modifier onlyOwner{
      require(msg.sender == owner);
      _;
    }

    function withdraw()payable onlyOwner public{

      msg.sender.transfer(address(this).balance);
    }
