//Ovako se oznacava komentar
console.log('Kako je imenjace?')

let name = 'Marko'; //sa let se deklariraju varijable
console.log(name);

//konstante
const someNumber = 0.3;
console.log(someNumber);

//globalne varijable se deklariraju bez var, let i const

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
let gnijezdoArray = [['crvena', 1], ['bijela', 2], ['plava', 3]];
let odabir = gnijezdoArray[0][1];
console.log(odabir);
gnijezdoArray.push(['crna', 4]); //dodaje na kraj
console.log(gnijezdoArray);
gnijezdoArray.pop(); //izbacuje s kraja
console.log(gnijezdoArray);
//gnijezdoArray.shift(); izbacuje s početka
//gnijezdoArray.unshift(); dodaje na kraj


//Funkcije
function pozdrav(ime, prezime){
    console.log('Kako je ' + ime + ' ' + prezime + '?');
}
pozdrav('Franjo', 'Tudjman');

function kvadrat(broj){
    return broj * broj;
}
console.log(kvadrat(2))

function nextInLine(arr, item) {
    arr.push(item);

    return arr.shift();
}

var testArr = [1,2,3,4,5];

console.log(nextInLine(testArr, 6));
console.log('Red: ' + JSON.stringify(testArr));

// inkrementacija varijabla++;
//dekrementacija varijabla--;

let stringName = Milojko;
//dužina stringa: 
stringName.length;
let zadnjeSlovo = stringName[stringName.length - 1];
let nekoSlovo = stringName[3];

