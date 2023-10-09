alert("Task 1")

let a = Number(prompt("Введите начало диапозона"));
let b = Number(prompt("Введите конец диапозона"));
let sum = 0

// prompt = input в python

while (a <= b) {
    sum = sum + a;
    a++;
}

console.log("Task 1")
console.log("Сумма чисел = " + sum)
alert("Сумма чисел = " + sum)
