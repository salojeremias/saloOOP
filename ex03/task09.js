class SuperHero extends Person {
    constructor(name, age, superpower) {
        super(name, age)
        this.superpower = superpowers;
    }
    useSuperPower() {
        console.log('Using superpower: ${this.superpower}');
    }
}

const superhero1 = new SuperHero("Batman", 30, "Rich");
const superhero2 = new SuperHero("Hulk", 25, "Strong");

superhero1.useSuperPower();
superhero2.sayGreeting();