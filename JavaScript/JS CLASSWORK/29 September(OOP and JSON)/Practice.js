// task 1
// При наведении на ячейку меняется задний фон задача

let slot = document.querySelectorAll('td, th')
// Селектор затрагивает (div - селектор, table - селектор)

// slot.onmouseover = slot.onmouseout - не нужно

for (let item of slot) {
    item.addEventListener("mouseover", function() {
        this.style.backgroundColor = 'pink'
    })
    item.addEventListener("mouseout", function() {
        this.style.backgroundColor = null
    })
}

// task 2
// При нажатии на Like увеличивается счетчик

let likes = 0;
for (likes) {
    
}