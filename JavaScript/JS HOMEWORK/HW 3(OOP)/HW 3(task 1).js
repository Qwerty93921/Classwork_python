class Circle {
    constructor(radius) {
      this._radius = radius;
    }
  
    get radius() {
      return this._radius;
    }
  
    set radius(newRadius) {
      if (newRadius >= 0) {
        this._radius = newRadius;
      } else {
        console.log("Радиус не может быть отрицательным.");
      }
    }
  
    get diameter() {
      return 2 * this._radius;
    }
  
    calculateArea() {
      return Math.PI * this._radius ** 2;
    }
  
    calculateCircumference() {
      return 2 * Math.PI * this._radius;
    }
  }

  const myCircle = new Circle(5);
  
  console.log("Радиус окружности:", myCircle.radius);
  console.log("Диаметр окружности:", myCircle.diameter);
  console.log("Площадь окружности:", myCircle.calculateArea());
  console.log("Длина окружности:", myCircle.calculateCircumference());
  
  myCircle.radius = 7;
  console.log("Новый радиус окружности:", myCircle.radius);
