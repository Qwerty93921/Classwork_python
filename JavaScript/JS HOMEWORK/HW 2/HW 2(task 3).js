function transformString(inputString2) {
    let transformedString = '';
    
    for (let i = 0; i < inputString2.length; i++) {
      const char = inputString2[i];
      
      if (/[A-Z]/.test(char)) {
        transformedString += char.toLowerCase();
      } else if (/[a-z]/.test(char)) {
        transformedString += char.toUpperCase();
      } else if (/[0-9]/.test(char)) {
        transformedString += '_';
      } else {
        transformedString += char;
      }
    }
    
    return transformedString;
  }

  console.log("Task 3")
  console.log("---------------------------------------------------------------")
  const inputString2 = prompt("Введите что-то: ");
  const result = transformString(inputString2);
  console.log(result);
  console.log("---------------------------------------------------------------")
