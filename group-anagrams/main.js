//**
 //* @param {string[]} strs
 //* @return {string[][]}
 //*/
var groupAnagrams = function(strs, map = new Map())  {
    if (!strs.length) {
        return [];
    }
    
    equalCounts(strs, map);
    return [...map.values()]
};
var equalCounts = (strs, map) => {
for (const char of strs){
    const hash = getHash(char)
    const values = map.get(hash) || [];

    values.push(char)
    map.set(hash, values)
}
}
var getHash = (strs) => {
const counts = new Array(26).fill(0);

for (const letter of strs){
    const charCode = getCode(letter);
    
    counts[charCode]++;
}
return buildHash(counts)
}
const getCode = (letter) => letter.charCodeAt(0) - 'a'.charCodeAt(0);
const buildHash = (counts) => counts.toString();