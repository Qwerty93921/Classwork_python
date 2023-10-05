alert("Task 5")

let positive = [];
let negative = [];
let zeros = [];
let even = [];
let odd = [];

let user_numbers = prompt("Введите числа");
let my_list = user_numbers.split(" ").map(Number);

my_list.forEach(element => {
    if (element > 0) {
        positive.push(element);
    } else if (element < 0) {
        negative.push(element);
    } else if (element === 0) {
        zeros.push(element);
    }

    if (element % 2 === 0) {
        even.push(element);
    } else {
        odd.push(element);
    }
});

console.log("Task 5")
console.log("Положительные числа: " + positive);
console.log("Отрицательные числа: " + negative);
console.log("Нули: " + zeros);
console.log("Четные числа: " + even);
console.log("Нечетные числа: " + odd);

alert("Положительные числа: " + positive);
alert("Отрицательные числа: " + negative);
alert("Нули: " + zeros);
alert("Четные числа: " + even);
alert("Нечетные числа: " + odd);
