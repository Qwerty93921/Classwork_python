function createAbbreviation(phrase) {
    const words = phrase.split(" ");
    let abbreviation = "";
  
    for (let i = 0; i < words.length; i++) {
      const word = words[i];
      abbreviation += word[0].toUpperCase();
    }
  
    return abbreviation;
  }

  const phrase1 = prompt("Введите слова: ");
  const phrase2 = prompt("Введите другие слова: ");
  
  const abbreviation1 = createAbbreviation(phrase1);
  const abbreviation2 = createAbbreviation(phrase2);
  
  console.log("Task 5")
  console.log("---------------------------------------------------------------")
  console.log("Аббревиатура первой фразы: " + abbreviation1);
  console.log("Аббревиатура второй фразы: " + abbreviation2);
  console.log("---------------------------------------------------------------")
