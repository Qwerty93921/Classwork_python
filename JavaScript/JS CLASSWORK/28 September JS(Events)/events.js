let generatedNumber = 
document.getElementById("generated-number");

console.log(generatedNumber);

function generateRandomNumber() {
    return generatedNumber.innerText = 
    Math.ceil(Math.random(0, 100) * 100);

    // * 100 потому что изначально JavaScript выводит ДЕСЯТИЧНЫЕ числа
    // ceil округляет в большую часть 1.5 выведет 1, 
    // 1.6 выведет 2

    // floor ИГНОРИРУЕТ числа ПОСЛЕ ЗАПЯТОЙ
    // floor только целое число выводит 1.4 сделает 1,
    // 1.9 выведет 1
}

// https://learn.javascript.ru/introduction-browser-events - Введение в браузерные события
// Bootstrap(не ссылка)

// ---------------------------------------------------------------

// Task 2

document.querySelector('.main').onmousemove = function(event) {
    console.log(event);
    document.querySelector(`.x`).innerHTML = event.offsetX;
    document.querySelector(`.y`).innerHTML = event.offsetY;
}

document.querySelector('.main').addEventListener('mouseup', 
function(event) {
    if (event.button == 0) {
        document.querySelector('.click').innerHTML = 'Left';
    }   else if (event.button == 2) {
        document.querySelector('.click').innerHTML = 'Right';
    }   else {
        return;
    }
})

document.querySelector('.main').addEventListener('contextmenu', function(event))
    event.preventDefault();
})

// ---------------------------------------------------------------

// Task 4

let isShown = True;
document.querySelector('.show-hide-btn').addEventListener('click', 
function() {
    if isShown {

    }
    document.querySelector('.Text').hidden = isShown;
})
