// let myVariable
// Переменные

// var
// let
// const

// var - это устаревший вид let, но они отличаются ОБЛАСТЬЮ ВИДИМОСТИ
// let - создание переменной
// typeof - показывает тип данных переменной





// let firstName = "Chingis";  //string
// let age = 25;               //number

// let person = {              //object
//     firstName: "Temirlan",
//     lastName: "Aliyev",
//     salary: 3000000
// }
// // Ключ + значение(как СЛОВАРЬ)

// function sum(a, b) {
//     let sum;

// }

// console.log("Меня зовут - " + firstName);
// console.log("Мой возраст равен = " + age);
// console.log({person});
// console.log(typeof age);
// console.log(typeof firstName);
// console.log(typeof person);

// 12.111 // float
// 12     // integer





// Забирает элемент где встречает chislo1
// let el1 = document.getElementsByClassName("chislo1");
// let el2 = document.getElementsByClassName("chislo2");

// let value1 = el1[0].value
// let value2 = el2[0].value

// function sum() {
//     // alert("Окошко") - выводит сообщение после нажатия кнопки "Сложить"
//     console.log(value1 + value2)
//     console.log(typeof value1)
//     console.log(typeof value2)
//     return value1 + value2;
// }

// console.log(el1)
// console.log(el2)

// console.log(value1)


        // Number + string
console.log(2 + 2)
console.log(2 * 15)
console.log(200 / 5)
console.log(235 - 25)

let fruits = ["apple", "banana", "pineapple", "grape"]

// Выводит элементы
for (item of fruits) {
    console.log(item)
}

// Выводит ИНДЕКСЫ
for (item in fruits) {
    console.log(item)
}

for (let i = 0; i < fruits.length; i++) {
    console.log(i)
}

// a++ // a = a + 1


// task 1
// let myVar = prompt("Наше число: ");
// // const result = myVar ** 2

// const result = Math.pow(5, 2)
// // Первое это ЧИСЛО, второе это СТЕПЕНЬ

// alert(result)


// task 2
let myVar2 = prompt("Введите длину стороны квадрата:");
const result = myVar2 ** 2
alert(result)
