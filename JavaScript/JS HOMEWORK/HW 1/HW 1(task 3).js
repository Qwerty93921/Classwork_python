alert("Task 3")

let numb_1 = Number(prompt("Введите число чтобы вывести его делители"))
let str='';

for (let n = 1; n <= numb_1; n++){
    let e = numb_1 % n
    if(e==0){
    str += n + ', '
    }
}

console.log("Task 3")
console.log(`Делители числа ${numb_1}: ` + str)
alert(`Делители числа ${numb_1}: ` + str)
