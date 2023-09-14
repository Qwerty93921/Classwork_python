// Example 1

function clicked() {
    alert("Пример события через атрибут элемента HTML onclick");
}

function clicked2() {
    alert("Пример события через метод addEventListener");
}

function changed() {
    console.log("Сработало событие change")
}

// void означает что функция ничего не возвращает

// Example 2

const btn = document.getElementById('my-btn');
btn.onclick = () => {
    console.log("Пример события через свойства элемента HTML")
}
console.log({btn})

// Example 3

const btn3 = document.getElementById("my-btn3");
btn3.addEventListener("click", clicked2);

btn3.removeEventListener("click", rmclicked2)
