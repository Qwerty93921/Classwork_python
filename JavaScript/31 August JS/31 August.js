let amount = 1000
let str = `Строка состоит из ${amount}`
let username = "admin         "
let password = "admin"

// " " ' ' ` ` - 3 вида кавычек

console.log(str.split(','))

console.log(str.toLocaleLowerCase()) // Делает все буквы этой строки прописными(маленькими)
console.log(str.toUpperCase()) // Делает все буквы БОЛЬШИМИ
console.log(str.substring(1, 4)) // Как срез выдает от 1 ИНДЕКСА до 4 НЕвключительно
console.log(str.slice(-2)) // Как substring только в него МОЖНО писать ОТРИЦАТЕЛЬНЫЕ ЧИСЛА
console.log(username.trim()) // как strip убирает все пробелы до и после слова
console.log(username.indexOf("о")) // Показывает индекс 

// https://developer.mozilla.org/ru/docs/Web/JavaScript/Reference/Operators/Conditional_operator - тернарный оператор


// for (let index in str) {
//     console.log(str[index]);
// }

// Цикл



/*

\n - перенос строки
\r - Возврат каретки(Carriage return)
\t - табуляция(tab)
\' - Апостроф или одинарная кавычка
\" - Двойная кавычка
\` - особая кавычка(ё клавиша)
\\ - Обратная кочая черта(Backslash)

*/

// console.log(str[5])
// console.log(typeof str)

// --------------------------------------------------------------------------------------------------------------------------

// Task 1

let str1 = "Первое предложение"
let str2 = "Второе предложение"

function length_compare(str1, str2) {
    let result = 0

    if (str1.length > str2.length) {
        result += 1
        console.log(`result = ${result}`)
    }
    else if (str1.length < str2.length) {
        result -= 1
        console.log(`result = ${result}`)
    }
    else if(str1.length == str2.length) {
        result += 0
        console.log(`result = ${result}`)
    }
    return result

    /*
    if (result == 0) {
        return 0;
    } else if (result == 1) {
        return 1
    } else {
        return false;
    }
    */ //Тернарные операторы
    // Шаблон решения
}

length_compare(str1, str2)

// --------------------------------------------------------------------------------------------------------------------------

// Task 2

let str3 = "рандомное предложение"

function firstBigLetter(str3) {
    console.log(str3[0].toUpperCase() + str3.substring(1, 100))
    return str3
}

firstBigLetter(str3)

// --------------------------------------------------------------------------------------------------------------------------

// Task 6

let word1 = "шалаш"
let word2 = "кабак"
let word3 = "тут"
let word4 = "слово"
let word5 = "монитор"

function isPalindrome(word1) {
    if (word1==word1.split("").reverse().join("")) {
        console.log("Слово является палиндромом")
        return true
    }
    else if (word1!=word1.split("").reverse().join("")) {
        console.log("Слово не является палиндромом")
        return false
    }

}

isPalindrome(word1)
isPalindrome(word2)
isPalindrome(word3)
isPalindrome(word4)
isPalindrome(word5)

// --------------------------------------------------------------------------------------------------------------------------
