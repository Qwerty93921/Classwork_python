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

LESSON 7
Массивы(списки)

var arr = [5, true, "stroka", 5.7, 0, -100]

arr[3] = "word"
// ИЗМЕНЕНИЕ индекса 3(5.7 здесь)

console.log(arr[3])

console.log(arr.length)
// Выводит длину списка(тут 6, СЧИТАЕТ НЕ С НУЛЯ, С ЕДИНИЦЫ считает)

----------------------------------------------------------------------

var matrix = [ 
    [4, 6, 8], ["stroka", 5.7], [0, -100] 
]

matrix[1][0] = 90;
// Изменение "stroka"
// 1 - это индекс списка
// 0 - это индекс "stroka" в этом списке внутри

console.log(matrix)

---------------------------------------------------------------------------------------------------

LESSON 8

https://www.youtube.com/watch?v=H39s52IW3bk&list=PLDyJYA6aTY1kJIwbYHzGOuvSMNTfqksmk&index=8

Циклы for, while, do while

-------------------------------------------------------------------

FOR

for(var i = 0; i < 10; i++) {
    console.log(i)
}

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
i++ это увеличение на 1 в каждом цикле

1 выражение это изначальное значение переменной
2 выражение это условие
3 выражение это как будет меняться переменная за каждую итерацию
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

Ответ: от 0 до 9

for(var i = 100; i > 5; i /= 2) {
    console.log(i)
}

i /= 2
Одинаково с:
i = i / 2
Каждый раз она будет делиться на 2

Ответ:
100
50
25
12.5
6.25
-------------------------------------------------------------------
WHILE

В отличии от цикла for, в цикле while нужно СОЗДАВАТЬ переменные ВНЕ ЦИКЛА(вне скобок)

var j = 0;

while(j < 10) {
    console.log(j)
    j++;
}

Ответ: от 0 до 9
-------------------------------------------------------------------
var j = 1000;

while(j > 100) {
    console.log(j)
    j -= 100;
}

j -= 100
Одинаково с:
j = j - 100

Каждый раз j будет уменьшаться на 100

Ответ:
1000
900
800
700
600
500
400
300
200

-------------------------------------------------------------------

var isHasCar = true;

while(isHasCar) {

}

ВЕЧНЫЙ ЦИКЛ!!!!!!!!!!!!!!!!!!!!!!!

-------------------------------------------------------------------

DO WHILE

Он отличается от while тем, что он В ЛЮБОМ СЛУЧАЕ ВЫПОЛНИТ ОДНУ ИТЕРАЦИЮ(даже если она противоречит условию), 
и только потом будет ее выполнять ТОЛЬКО при соблюдении условий

var x = 100;
do {
    console.log(x);
} while( x < 50);

Ответ: 100

var x = 0;
do {
    console.log(x);
    x++;
} while( x < 10);

Ответ: От 0 до 9

-------------------------------------------------------------------

for(var i = 10; i <= 20; i += 2) {
    console.log(i)
}

Начало цикла с числа 10, условие i меньше или равно 20, i меняется на +2 каждый раз

Ответ:
10
12
14
16
18
20

-------------------------------------------------------------------

for(var i = 10; i <= 20; i += 2) {
    if(i > 15)
        break;

    console.log(i)
}

Ответ:
10
12
14

-------------------------------------------------------------------

for(var i = 10; i <= 20; i++) {
    if(i % 2 == 0)
        continue;

    console.log(i)
}

Если при делении на 2, ОСТАТОК после деления будет 0, тогда ПРОПУСКАЕТ определенную итерацию(не выводит в консоль)

Ответ:
11
13
15
17

-------------------------------------------------------------------

var arr = [5, 7, 3, 8, 9, "stroka"];

for(var i = 0; i < arr.length; i++) {
    console.log("Элемент " + (i + 1) + ": " + arr[i])
}

Начало с НУЛЯ, пока i меньше чем ДЛИНА СПИСКА(тут 6) и увеличение на 1 каждую итерацию
(i + 1) - значит чтобы выводилось начиная с 1 а не 0

Ответ:
Элемент 1: 5
Элемент 2: 7
Элемент 3: 3
Элемент 4: 8
Элемент 5: 9
Элемент 6: "stroka"

-------------------------------------------------------------------

var arr = [5, 7, 3, 8, 9, 91];

for(var i = 0; i < arr.length; i++) {
    arr[i] *= 2;

    console.log("Элемент " + (i + 1) + ": " + arr[i])
}
Каждый элемент умножается на 2

Ответ:
Элемент 1: 10
Элемент 2: 14
Элемент 3: 6
Элемент 4: 16
Элемент 5: 18
Элемент 6: 182

---------------------------------------------------------------------------------------------------

for(i = 0; i <= 100; i+=5) {
    console.log(i)
}

Ответ:
0
5
10
15
20
...
100

---------------------------------------------------------------------------------------------------

myList = [1, 3, 5, 7, 9]
for(i in myList) {
    console.log(myList[i])
}

Ответ:
1
3
5
7
9


---------------------------------------------------------------------------------------------------

LESSON 9

Всплывающие окна

alert, prompt, confirm

alert() - выводит окно с сообщением
confirm() - он выводит окно С 2 КНОПКАМИ(ОТМЕНА и ОК)
prompt() - Выводит окно с ТЕКСТОВЫМ ПОЛЕМ ДЛЯ ВВОДА, если написать после запятой что-то, то оно будет НАПИСАНО ЗАРАНЕЕ(можно не писать запятую)

alert("Привет")

var data = confirm("Вы голодны?")
console.log(data)

Ответ:
true(если нажать ОК)
false(если нажать ОТМЕНА)

confirm() - он выводит окно С 2 КНОПКАМИ(ОТМЕНА и ОК)

---------------------------------------------------------------------

var data = confirm("Вы голодны?")
if(data) {
    alert("Вы молодец!");
}

Ответ:
ничего(если нажать ОТМЕНА)
окно "Вы молодец"(если нажать ОК)

---------------------------------------------------------------------

var data = prompt("Скажите сколько вам лет", 20)
prompt() - Выводит окно с ТЕКСТОВЫМ ПОЛЕМ ДЛЯ ВВОДА, если написать после запятой что-то, то оно будет НАПИСАНО ЗАРАНЕЕ(можно не писать запятую)

console.log(data);

Ответ:
null - если нажать ОТМЕНА
пустота - если нажать ОК и ничего не ввести
45 - если нажать ОК и ввести 45 самому

var var1 = null;
null - это ПУСТОТА

---------------------------------------------------------------------

confirm() - выдает TRUE или FALSE

var person = null;
if (confirm("Вы точно уверены? ")) {
    person = prompt("Введите ваше имя: ");
    alert("Привет " + person)
} else {
    alert("Вы нажами на 'Отмена' ")
}

if confirm = true(проверка)

---------------------------------------------------------------------------------------------------

LESSON 10

Функции

https://www.youtube.com/watch?v=yUTwuyfTsOc&list=PLDyJYA6aTY1kJIwbYHzGOuvSMNTfqksmk&index=10

function название(a, b) {
    result = a + b
    return result
}

Вызов функции:
название()

---------------------------------------------------------------------

function info() {
    console.log("Привет!")
    console.log("!")
}

info()

---------------------------------------------------------------------

function summa(a, b) {
    let result = a + b;
    console.log(result);
}

summa(5, 10)

---------------------------------------------------------------------

function summa(array) {
    let sum = 0;

    for(let i = 0; i < array.length; i++) {
        sum += array[i];
    }
    console.log(sum)
}

let array = [6, 8, 1];

summa(array);

---------------------------------------------------------------------

function summa(array) {
    let sum = 0;

    for(let i = 0; i < array.length; i++) {
        sum += array[i];
    }
    console.log(sum)
}

let array = [6, 8, 1];
let array_2 = [6, 8, 1, 7];
let array_3 = [6, 8, 1, 90];

summa(array);
summa(array_2);
summa(array_3);

// Ответ: 15
// Ответ: 22
// Ответ: 105
// Сумма всех чисел внутри списка(массива)

---------------------------------------------------------------------

return нужен в случае если переменную нужно ИСПОЛЬЗОВАТЬ ГДЕ ЛИБО ЕЩЕ

function summa(array) {
    let sum = 0;

    for(let i = 0; i < array.length; i++) {
        sum += array[i];
    }
    
    return sum;
}

let array = [6, 8, 1];
let array_2 = [6, 8, 1, 7];
let array_3 = [6, 8, 1, 90];

let res = summa(array);
// Весь результат функции записан в переменную RES

console.log("Результьтат " + res);

---------------------------------------------------------------------------------------------------

LESSON 11

События и обработчик событий
EVENTS

onclick="getElementById('demo').innerHTML = Date() (текст или функция)"
ondblclick - при двойном нажатии происходит действие
onmouseover - курсор над кнопкой
onmouseout - курсор убрали с кнопки
onchange - изменение HTML документа
onkeydown - при наводке стрелки мыши на кнопку и при нажатии любой кнопки будет действие
oninput - 
onload - срабатывает при загрузке определенного тега(на тег body кидают)
onsubmit - 

!!!!!!!!!!!!
У КНОПКИ МОЖНО МЕНЯТЬ СТИЛЬ ЧЕРЕЗ CSS КЛАСС
!!!!!!!!!!!!

---------------------------------------------------------------------

HTML

<button onclick="alert('Вы нажали на кнопку')"> Click me </button>

<button onclick="funcForButton()"> Click me </button>
САМОПИСНАЯ ФУНКЦИЯ

<p onclick="funcForButton()"> Click me </p>
ФУНКЦИИ можно ПРИВЯЗАТЬ не только к КНОПКАМ(button в html), но и к ЛЮБОМУ ТЕГУ(тег p сверху пример)
p - параграф

<button ondblclick="funcForButton()"> Click me </button>
Происходит действие ТОЛЬКО ПРИ ДВОЙНОМ НАЖАТИИ

---------------------------------------------------------------------

JAVASCRIPT

let counter = 0;
// ОБЯЗАТЕЛЬНО создавать переменную ВНЕ ФУНКЦИИ, то есть ГЛОБАЛЬНУЮ ПЕРЕМЕННУЮ(чтобы считать)

function funcForButton() {
    counter++;
    console.log(counter);
}

Считает сколько раз нажали на кнопку

---------------------------------------------------------------------


*/

let counter = 0;

function funcForButton(element) {
    counter++;
    element.innerHTML = "Вы нажали на кнопку: " + counter + " раз";

    // ИЗМЕНЕНИЕ CSS СТИЛЕЙ

    element.style.background = "green";
    // При нажатии ЗАДНИЙ ФОН становится ЗЕЛЕНЫМ

    element.style.color = "blue";
    // При нажатии кнопки ТЕКСТ становится СИНИМ

    element.style.cssText = "border-radius: 5px; border: 0px; font-size: 20px; background: cyan;"
    // При нажатии МЕНЯЮТСЯ СТИЛИ НА ЭТИ СВЕРХУ
    // При использовании cssText, все ОТДЕЛЬНЫЕ СТРОКИ МЕНЯЮЩИЕ CSS СТИЛИ, они ИГНОРИРУЮТСЯ

    console.log(element.name)
    // element.name - это вывод НАЗВАНИЕ КНОПКИ ИЗ ТЕГА NAME в HTML(mainButton в этом случае)

}

function onInput(element) {
    if(element.value == "Hello" || element.value == "hello") {
        alert("Hello!")
    }

    console.log(element.value);
}

// Любой введенный символ выводится в консоль со прошлыми символами
// Функция onInput принимает объект и выводит его
// value - ЗНАЧЕНИЕ внутри текстового поля

// ---------------------------------------------------------------------------------------------------

/*

LESSON 12

Управление HTML и обработка форм с помощью JavaScript

https://www.youtube.com/watch?v=1nzH6WCEonQ&list=PLDyJYA6aTY1kJIwbYHzGOuvSMNTfqksmk&index=12


*/
