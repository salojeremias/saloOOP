const musician = {

    name: 'Sting',
    realName: 'Gordon Matthew Thomas Sumner',
    instrument: {
        type: 'bass'
        }
    };

const {name, instrument} = musician;
console.log(name);
console.log(instrument);

const {name: nameOfArtist, instrument: instrumentOfArtist} = musician;
console.log(nameOfArtist);
console.log(instrumentOfArtist);

const {instrument: {type: instrumentOfArtist}} = musician;
console.log(instrumentOfArtist);

const {instrument: {make: instrumentOfArtist = 'unknown'}} = musician;
console.log(instrumentOfArtist);