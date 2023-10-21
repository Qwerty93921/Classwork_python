function camelizeCssProperty(cssProperty) {
    return cssProperty.replace(/-([a-z])/g, function (match, letter) {
      return letter.toUpperCase();
    });
  }

  const cssProperty1 = "font-size";
  const cssProperty2 = "background-color";
  const cssProperty3 = "text-align";
  
  const camelCase1 = camelizeCssProperty(cssProperty1);
  const camelCase2 = camelizeCssProperty(cssProperty2);
  const camelCase3 = camelizeCssProperty(cssProperty3);
  
  console.log("Task 4")
  console.log("---------------------------------------------------------------")
  console.log(camelCase1);
  console.log(camelCase2);
  console.log(camelCase3);
  console.log("---------------------------------------------------------------")
