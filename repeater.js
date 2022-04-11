console.log("test")

function Person(first, last, age, eye) {
    this.firstName = first;
    this.lastName = last;
    this.age = age;
    this.eyeColor = eye;
  }


  customer = new Person("fritz69","Müller", 19, "green")

console.log(customer)
console.log(customer.age)

x = 0

while (x<5){
    console.log(x)
    x++
}


customer["age"]= 22
console.log(customer.age)
if (Object.values(customer).indexOf('fritz') > -1) {
    console.log('has age');
 }
else{
    console.log("no Fritz, no party")
}
xx= "hello dolly99"
nameCustomer = customer.firstName

result = nameCustomer.replace(/\d+/g, ", no darling!")
console.log(result)

console.log(nameCustomer)