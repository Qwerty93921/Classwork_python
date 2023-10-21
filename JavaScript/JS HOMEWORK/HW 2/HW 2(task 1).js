function stringAnalysis(inputString) {

    let letterCount = 0;
    let digitCount = 0;
    let otherCount = 0;
  
    for (let i = 0; i < inputString.length; i++) {
      const char = inputString.charAt(i);
      if (/[a-zA-Z]/.test(char)) {
        letterCount++;
      } else if (/[0-9]/.test(char)) {
        digitCount++;
      } else {
        otherCount++;
      }
    }

    console.log("Количество букв: " + letterCount);
    console.log("Количество цифр: " + digitCount);
    console.log("Количество других символов: " + otherCount);

  }

  console.log("Task 1")
  console.log("---------------------------------------------------------------")
  const inputString = prompt("Введите строку на английском языке")
  stringAnalysis(inputString);
  console.log("---------------------------------------------------------------")
