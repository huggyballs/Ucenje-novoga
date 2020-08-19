//Ovako se oznacava komentar
console.log('Kako je imenjace?')

let name = 'Marko'; //sa let se deklariraju varijable
console.log(name);

//konstante
const someNumber = 0.3;
console.log(someNumber);

//Objekti
let osoba = {
    ime: 'Marko',
    godine: 24
};
console.log(osoba);

osoba.ime = 'Franjo';
console.log(osoba.ime);

osoba['ime'] = 'Ivan';
console.log(osoba.ime);

//Array
let boje = ['crvena', 'bijela', 'plava'];
console.log(boje[1])
boje[3] = 'crna';
console.log(boje);

//Funkcije
function pozdrav(ime, prezime){
    console.log('Kako je ' + ime + ' ' + prezime + '?');
}
pozdrav('Franjo', 'Tudjman');

function kvadrat(broj){
    return broj * broj;
}
console.log(kvadrat(2))