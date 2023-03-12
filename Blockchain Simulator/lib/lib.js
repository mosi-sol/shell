
const dblog = `
{
    "blockchain": [
        {
            "index": 0,
            "timestamp": 1678623854,
            "data": "0x75e9e4ca9271B8F91F18b548F0F928A12768d92a",
            "previousHash": "0",
            "hash": "3c81c43efdbd35fbc764b8b7d6b02ba9f50dadf31901a1fa3081a5bc551148ae"
        },
        {
            "index": 1,
            "timestamp": 1678623856,
            "data": {
                "sender": "0xa593529F57eeE204587E4690433643A3fd98CC56",
                "recipient": "0xECb6ed5e92B2DACa11fD4E691568f30651C441d9",
                "quantity": 28
            },
            "previousHash": "3c81c43efdbd35fbc764b8b7d6b02ba9f50dadf31901a1fa3081a5bc551148ae",
            "hash": "ec886a267f8986a3bdb944fbd559c54544347e8c1fce6c18b6fe2d09aff56bc8"
        },
        {
            "index": 2,
            "timestamp": 1678623856,
            "data": {
                "sender": "0x51F459c8bC9403DdC0546F7ff7b425cD74f565CC",
                "recipient": "0x0E8727edFe955EED690E0EDc482846FC0f612839",
                "quantity": 12
            },
            "previousHash": "ec886a267f8986a3bdb944fbd559c54544347e8c1fce6c18b6fe2d09aff56bc8",
            "hash": "280b4b581deb0e9c72b84c18ab231b10b0fdcb16e003f5418700df7bb923ab2a"
        },
        {
            "index": 3,
            "timestamp": 1678623856,
            "data": {
                "sender": "0x099B74462665D467D51F54d5C3b3E73a0078651a",
                "recipient": "0xb77cf6da3a24E2E5bc96c99F9b0DC1F2Dd70C8F4",
                "quantity": 8
            },
            "previousHash": "280b4b581deb0e9c72b84c18ab231b10b0fdcb16e003f5418700df7bb923ab2a",
            "hash": "2ce00b46fa67a17fd0966245116291d44d28defd9a2d130849066a75aaeca504"
        },
        {
            "index": 4,
            "timestamp": 1678623856,
            "data": {
                "sender": "0x16257a8c14c9737a9b00Bf24a7ac9FCC6E753E0A",
                "recipient": "0x3c0Daf7dfaBED51c87F1C5c717975Ab49F73AfC8",
                "quantity": 89
            },
            "previousHash": "2ce00b46fa67a17fd0966245116291d44d28defd9a2d130849066a75aaeca504",
            "hash": "d14de984f9c78d7e2ec21a682e0eb6b75fc6ae541cebd8873177aebe05e1dd8b"
        }
    ]
}
`;

const obj = JSON.parse(dblog);
const showCase = document.getElementById("demo");

showCase.innerHTML += `<ul class="">`;
for (let x in obj.blockchain) {
	showCase.innerHTML += `<li class="list-none bg-gray-300 px-2 pt-2">id: <span class="font-normal">${obj.blockchain[x].index}</span></li>`;    
	showCase.innerHTML += `<li class="list-none bg-gray-300 px-2">date: <span class="font-normal">${obj.blockchain[x].timestamp}</span></li>`;  
    if(obj.blockchain[x].index > 0){
        showCase.innerHTML += `<li class="list-none bg-gray-300 px-2">sender: <span class="font-normal">${obj.blockchain[x].data.sender}</span></li>`;
        showCase.innerHTML += `<li class="list-none bg-gray-300 px-2">recipient: <span class="font-normal">${obj.blockchain[x].data.recipient}</span></li>`;
        showCase.innerHTML += `<li class="list-none bg-gray-300 px-2">amount: <span class="font-normal">${obj.blockchain[x].data.quantity}</span></li>`;
        showCase.innerHTML += `<li class="list-none bg-gray-300 px-2">previous block: <span class="font-normal">${obj.blockchain[x].previousHash}</span></li>`;
    } else {
        showCase.innerHTML += `<li class="list-none bg-gray-300 px-2">data: <span class="font-normal">${obj.blockchain[x].data}</span></li>`;
        showCase.innerHTML += `<li class="list-none bg-gray-300 px-2"><s>previous block</s>: <span class="font-normal">GENESIS</span></li>`;
    }
    showCase.innerHTML += `<li class="list-none bg-gray-300 px-2 mb-6 pb-2 shadow-lg">hash: <span class="font-normal">${obj.blockchain[x].hash}</span></li>`;
}
showCase.innerHTML += '</ul>';


// =================== console 

for (let x in obj.blockchain) {
	console.log("id: ", obj.blockchain[x].index);
	console.log("date: ", obj.blockchain[x].timestamp);
	if(obj.blockchain[x].index > 0){ 
		console.log("sender: ", obj.blockchain[x].data.sender);
		console.log("recipient: ", obj.blockchain[x].data.recipient);
        console.log("amount: ", obj.blockchain[x].data.quantity);
        console.log("previous hash: \n", obj.blockchain[x].previousHash);
	} else {
		console.log("data: ", obj.blockchain[x].data);
        console.log("GENESIS BLOCK ");
	}
	console.log("hash: \n", obj.blockchain[x].hash);
	console.log("==============================");
}

