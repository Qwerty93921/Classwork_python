alert("Task 2")

let number_1 = Number(prompt("Введите первое число для НОД"))
let number_2 = Number(prompt("Введите второе число для НОД"))
let NOD;

while (number_1 != number_2) {
  if (number_1 > number_2) {
    number_1 = number_1 - number_2;
  }
  else {
    number_2 = number_2 - number_1;
  }
}
NOD = number_1;

alert("НОД = " + NOD)
console.log("Task 2")
console.log("НОД = " + NOD)

// 90 и 84 будет 6
