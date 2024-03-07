/*

https://www.youtube.com/watch?v=WLsFBu_15Hw&list=PLDyJYA6aTY1kJIwbYHzGOuvSMNTfqksmk&index=3

LESSON 3 - вывод в консоль

document.write("JavaScript говорит привет!")

console.log("JavaScript говорит привет!")

console.info("JavaScript говорит привет!")
Одинаковый с log

console.error("JavaScript говорит привет!")
Красный текст в консоли

console.warn("JavaScript говорит привет!")
Желтый текст в консоли

// - комментарий однострочный
/* star/ - многострочный комментарий

---------------------------------------------------------------------------------------------------

LESSON 4 - переменные

let, var, const - обозначение переменных

let x
x - в этом случае будет иметь значение undefined

var - МОЖНО переопределить
let, const - НЕЛЬЗЯ переопределить
let, const - БЛОЧНЫЕ переменные
var - ГЛОБАЛЬНАЯ переменная(есть еще локальные переменные)
Если она объявлена ВНУТРИ БЛОКА и к ней обращаются ИЗВНЕ, тогда получится обратиться к ней и наоборот

блок - все что внутри фигурных скобок { asd }

var - нужно для поддержания СТАРЫХ БРАУЗЕРОВ
1995 - 2015 был var

let, const - добавили в 2015

---------------------------------------------------------------------------------------------------

let a = 5
let b = 3
let c = a + b;

console.log(c)

5 + 3 + "2"
82

5 + "3" + 2
532

5 + 3 + "2" + 4
824

Все что ПОСЛЕ числа В КАВЫЧКАХ СЧИТАЕТСЯ STR ФОРМАТОМ

---------------------------------------------------------------------------------------------------

var num = 5;
console.log(num)
console.log("Переменная: " + num)

// будет вывод числа 5 в консоль

---------------------------------------------------------------------------------------------------

LESSON 5

var num_3 = 5;

num_3 = num_3 + 7;
num_3 += 7;
Второй вариант написания

console.log("Result = " + num_3)

Ответ: 12

var num_4 = 4
num_4++;

++ означает число УВЕЛИЧИТЬ НА ЕДИНИЦУ

Ответ: 5

var num_4 = 4
num_4--;

Ответ: 3

-- означает число УМЕНЬШИТЬ НА ЕДИНИЦУ

var str_1 = Number("12");
var str_2 = Number("2");

console.log("Result = " + (str_1 + str_2))

Ответ: 14

Тут идет ТРАНСФОРМАЦИЯ STR формат в INT формат

------------------------------------------------

console.log("Math: " + Math.PI);

Ответ: 3.14

console.log("Math: " + Math.sin())

Это "модуль" который выводит математические формулы

console.log("Math: " + Math.min(4, 6, 8, 2, 0, 5, -8))

Ответ: -8

console.log("Math: " + Math.max(1000, 4, 6, 8, 2, 0, 5, -8))

Ответ: 1000

---------------------------------------------------------------------------------------------------

LESSON 6

https://www.youtube.com/watch?v=TE0S9G3C4vU&list=PLDyJYA6aTY1kJIwbYHzGOuvSMNTfqksmk&index=6

Условные операторы - IF, else, else if

var number = 15;
var isHasHouse = true;

if (number == 5 && !isHasHouse) {
    console.log("Ok")
} else if(number < 10) {
    console.log("Number is lower than 10")
} else if(number > 10) {
    console.log("Number is greater than 10")
} else if(number >= 15) {
    console.log("Number is >= 15")
} else {
    console.log("Else")
}

|| - это ИЛИ
&& - это И
!isHasHouse - проверка на false

------------------------------------------------

switch case - тема

var stroka = "word"

switch(stroka) {
    case "4": 
        console.log("Переменная со значением 4");
        break;
    case "45": 
        console.log("Переменная со значением 45");
        break;
    case "word": 
        console.log("Переменная со значением 'word' ");
        break;
    default:
        console.log("Default")
}

switch - ПРОВЕРКА переменной stroka
case - значит В СЛУЧАЕ если ПЕРЕМЕННАЯ stroka равна 4, ТОГДА выполняются действия
break в конце ОБЯЗАТЕЛЬНО
default = else, он выполняется ЕСЛИ ВСЕ CASE НЕ ПОДОШЛИ
после default слово break можно не ставить(можно и ставить)

switch case - используется для проверки ОДНОЙ ПЕРЕМЕННОЙ на РАЗНЫЕ ЗНАЧЕНИЯ
switch case - проверяет ТОЛЬКО НА РАВЕНСТВО(на БОЛЬШЕ, МЕНЬШЕ он НЕ ПРОВЕРЯЕТ)

---------------------------------------------------------------------------------------------------



*/
