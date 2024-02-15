class Person {
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }

    getName() {
        return this.name;
    }
    getAge() {
        return this.age;
    }

    sayGreeting() {
        return 'Hi, my name is ${this.name} and my age is ${this.age} years old';
    }
}

const person1 = new Person("Pekka", 65);
const person2 = new Person("Eetu", 12);

console.log(person1.getName());
console.log(person2.getAge());
console.log(person1.sayGreeting());