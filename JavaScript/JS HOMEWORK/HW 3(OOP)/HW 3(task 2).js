class CssClass {
    constructor(className) {
      this.className = className;
      this.styles = {};
    }
  
    setStyle(property, value) {
      this.styles[property] = value;
    }
  
    removeStyle(property) {
      if (property in this.styles) {
        delete this.styles[property];
      }
    }
  
    getCss() {
      let cssString = `.${this.className} {`;
      for (const property in this.styles) {
        cssString += `${property}: ${this.styles[property]}; `;
      }
      cssString += '}';
      return cssString;
    }
  }

  const myClass = new CssClass("my-class");

  myClass.setStyle("color", "blue");
  myClass.setStyle("font-size", "16px");

  const cssCode = myClass.getCss();
  console.log(cssCode);
