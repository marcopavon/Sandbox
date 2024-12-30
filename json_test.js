  // Create a JSON object
  const jsonData = {
    name: 'John Doe',
    age: 25,
    city: 'Example City',
    cordinate: {
        west: 100,
        nord: 5,
    }
  };
  // Create a JSON object
  const jsonData2 = {
    name: 'John Doe',
    age: 25,
    city: 'Example City',
    cordinate: {
        west: 100,
        nord: 5,
    }
  };

  // Convert the JSON object to a string
  const jsonString = JSON.stringify(jsonData, null, 2);

  // Log the JSON string to the console
  console.log('JSON data:');
  console.log(jsonString);

  class Person {
    constructor(name, age, city) {
      this.name = name;
      this.age = age;
      this.city = city;
    }
  
    sayHello() {
      console.log('Hello!');
    }
  }

  const person = new Person('Hans Muller', 25, 'New York City');
  const person2 = new Person('John Doe', 25, 'Example City');
console.log(person.city)
//console.log(person)

const group = {...jsonData, ...person};

console.log(group);