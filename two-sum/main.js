/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target, map = new Map()) {
    for (let current = 0; current < nums.length; current ++){
const prevCombos = target - nums[current]
const combinations = map.get(prevCombos)
const validCombos = map.has(prevCombos)

if (validCombos){
    return [current, combinations]
}
map.set(nums[current], current)
    }
    return [-1, -1]
};