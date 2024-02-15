for (let key in musician) {
    console.log('${key} = ${musician{key}}');
}

const musician1 = {name: 'Jimi', instrument: 'guitar'}
const musician2 = {name: 'Frank', instrument: 'guitar'}
const musiciansArray = [musician1, musician2]

console.log(Object.entries(musiciansArray));
console.log(Object.keys(musiciansArray));
console.log(Object.values(musiciansArray));
