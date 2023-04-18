// Creating Objects: Object Literals 

let empty = {}; 
let point={x:0,y:0};
let p2 = { x: point.x, y: point.y+1 }; 
let book={
    "main title": "JavaScript",
    "sub-title": "The Definitive Guide",
    for: "all audiences", 
    author: {
        firstname: "David",
        surname: "Flanagan"
    }
};

// Creating Objects with new

let o = new Object(); // Create an empty object: same as {}.
let a = new Array(); // Create an empty array: same as [].
let d = new Date(); // Create a Date object representing the current time
let r = new Map(); // Create a Map object for key/value mapping

// Querying and Setting Properties  

let author = book.author; // Get the "author" property of the book. 
let name = author.surname; // Get the "surname" property of the author. 
let title = book["main title"]; // Get the "main title" property of the book.
book.edition = 7; // Create an "edition" property of book. 
book["main title"] = "ECMAScript"; // Change the "main title" property.

// Property Access Errors

book.subtitle // => undefined: property doesn't exist
let len = book.subtitle.length; // !TypeError: undefined doesn't have length
// A verbose and explicit technique
let surname = undefined; 
if (book) {
    if (book.author) {
        surname = book.author.surname;
    } 
}

// A concise and idiomatic alternative to get surname or null or undefined
surname = book && book.author && book.author.surname;

let surname = book?.author?.surname;

// Deleting Properties 

delete book.author;         // The book object now has no author property. 
delete book["main title"];  // Now it doesn't have "main title", either.

let o={x:1};                // o has own property x and inherits property toString
delete o.x                  // => true: delete property x
delete o.x                  // => true: does nothing (x doesn't exist) but true anyway
delete o.toString           // => true: does nothing (toString isn't an own property) 
delete 1                    // => true: nonsense, but true anyway

// Testing Properties

let o={x:1};
"x" in o // => true: o has an own property "x"
"y" in o // => false: o doesn't have a property "y" 
"toString" in o // => true: o inherits a toString property

let o={x:1};
o.hasOwnProperty("x") // => true: o has an own property x 
o.hasOwnProperty("y") // => false: o doesn't have a property y 
o.hasOwnProperty("toString") // => false: toString is an inherited property

let o={x:1};
o.propertyIsEnumerable("x") // => true: o has an own enumerable property x
o.propertyIsEnumerable("toString") // => false: not an own property 

let o={x:1};
o.x !== undefined // => true: o has a property x
o.y !== undefined // => false: o doesn't have a property y 
o.toString !== undefined // => true: o inherits a toString property

let o = { x: undefined }; // Property is explicitly set to undefined
o.x !== undefined // => false: property exists but is undefined
o.y !== undefined // => false: property doesn't even exist
"x" in o // => true: the property exists
"y" in o // => false: the property doesn't exist
delete o.x; // Delete the property x
"x" in o // => false: it doesn't exist anymore

// Enumerating Properties

let o = {x: 1, y: 2, z: 3};  // Three enumerable own properties
o.propertyIsEnumerable("toString") // => false: not enumerable
for(let p in o) {       // Loop through the properties
    console.log(p);     // Prints x, y, and z, but not toString
}

// Extending Objects 

let target = {x: 1}, source = {y: 2, z: 3}; 
for(let key of Object.keys(source)) {
    target[key] = source[key];
}
target // => {x: 1, y: 2, z: 3}

Object.assign(o, defaults); // overwrites everything in o with defaults
o = Object.assign({}, defaults, o);

// Like Object.assign() but doesn't override existing properties 
// (and also doesn't handle Symbol properties)
function merge(target, ...sources) {
    for(let source of sources) {
        for(let key of Object.keys(source)) {
            if (!(key in target)) { // This is different than Object.assign() 
                target[key] = source[key];
            } 
        }
    }
    return target; 
}
Object.assign({x: 1}, {x: 2, y: 2}, {y: 3, z: 4}) // => {x: 2, y: 3, z: 4} 
merge({x: 1}, {x: 2, y: 2}, {y: 3, z: 4}) // => {x: 1, y: 2, z: 4}

// Serializing Objects 

let o = {x: 1, y: {z: [false, null, ""]}}; // Define a test object
let s = JSON.stringify(o); // s == '{"x":1,"y":{"z":[false,null,""]}}' 
let p = JSON.parse(s); // p == {x: 1, y: {z: [false, null, ""]}}

// Extended Object Literal Syntax 

let x=1,y=2; 
let o={
    x: x,
    y:y 
};

let x=1,y=2; 
let o={x,y}; 
o.x + o.y // => 3

let position={x:0,y:0};
let dimensions = { width: 100, height: 75 };
let rect = { ...position, ...dimensions };
rect.x + rect.y + rect.width + rect.height // => 175

let o={x:1};
let p={x:0,...o};
p.x // => 1: the value from object o overrides the initial value 
let q={...o,x:2};
q.x // => 2: the value 2 overrides the previous value from o.

let square = {
    area: function() { return this.side * this.side; }, 
    side: 10
};
square.area() // => 100

let square = {
    area() { return this.side * this.side; }, 
    side: 10
};
square.area() // => 100

// Creating Arrays

let empty = []; // An array with no elements
let primes = [2, 3, 5, 7, 11]; // An array with 5 numeric elements
let misc = [ 1.1, true, "a", ]; // 3 elements of various types + trailing comma

let a=[1,2,3];
let b = [0, ...a, 4]; // b == [0, 1, 2, 3, 4]

let digits = [..."0123456789ABCDEF"];
digits // => ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]

let letters = [..."hello world"];
[...new Set(letters)] // => ["h","e","l","o"," ","w","r","d"]

let a = new Array();
let a = new Array(10);
let a = new Array(5, 4, 3, 2, 1, "testing, testing");

Array.of() // => []; returns empty array with no arguments
Array.of(10) // => [10]; can create arrays with a single numeric argument
Array.of(1,2,3) // => [1, 2, 3]

let truearray = Array.from(arraylike);

// Reading and Writing Array Elements 

let a = ["world"]; // Start with a one-element array
let value = a[0]; // Read element 0
a[1] = 3.14; // Write element 1
let i=2;
a[i] = 3; // Write element 2
a[i + 1] = "hello"; // Write element 3
a[a[i]] = a[0]; // Read elements 0 and 2, write element 3

let o = {}; // Create a plain object
o[1] = "one"; // Index it with an integer
o["1"] // => "one"; numeric and string property names are the same
a[-1.23] = true; // This creates a property named "-1.23" 
a["1000"] = 0; // This the 1001st element of the array 
a[1.000] = 1; // Array index 1. Same as a[1] = 1;
let a = [true, false]; // This array has elements at indexes 0 and 1 
a[2] // => undefined; no element at this index. 
a[-1] // => undefined; no property with this name.

// Sparse Array
let a = new Array(5); // No elements, but a.length is 5.
a = []; // Create an array with no elements and length = 0. 
a[1000] = 0; // Assignment adds one element but sets length to 1001.
let a1 = [,]; // This array has no elements and length 1
let a2 = [undefined]; // This array has one undefined element
0 in a1 // => false: a1 has no element with index 0
0 in a2 // => true: a2 has the undefined value at index 0

// Array Length
[].length // => 0: the array has no elements 
["a","b","c"].length // => 3: highest index is 2, length is 3
a = [1,2,3,4,5]; // Start with a 5-element array.
a.length = 3; // a is now [1,2,3].
a.length = 0; // Delete all elements.  a is [].
a.length = 5; // Length is 5, but no elements, like new Array(5)

// Adding and Deleting Array Elements
let a = []; // Start with an empty array. 
a[0] = "zero"; // And add elements to it. 
a[1] = "one";
let a = []; // Start with an empty array
a.push("zero"); // Add a value at the end. a = ["zero"] 
a.push("one", "two"); // Add two more values. a = ["zero", "one", "two"]
let a = [1,2,3];
delete a[2]; // a now has no element at index 2
2 in a // => false: no array index 2 is defined
a.length // => 3: delete does not affect array length

// Iterating Arrays 

let letters = [..."Hello world"]; // An array of letters 
let string = "";
for(let letter of letters) {
        string += letter;
}
string // => "Hello world"; we reassembled the original text


let everyother = "";
for(let [index, letter] of letters.entries()) {
    if (index % 2 === 0) everyother += letter; // letters at even indexes 
}
everyother // => "Hlowrd"

let uppercase = "";
letters.forEach(letter => { // Note arrow function syntax here
        uppercase += letter.toUpperCase();
});
uppercase // => "HELLO WORLD"

let vowels = "";
for(let i = 0; i < letters.length; i++) { // For each index in the array
    let letter = letters[i];              // Get the element at that index
    if (/[aeiou]/.test(letter)) {         // Use a regular expression test
        vowels += letter;                 // If it is a vowel, remember it
    } 
}
vowels // => "eoo"

// Create a multidimensional array
let table = new Array(10); // 10 rows of the table
for(let i = 0; i < table.length; i++) {
    table[i] = new Array(10); // Each row has 10 columns
}
// Initialize the array
for(let row = 0; row < table.length; row++) {
    for(let col = 0; col < table[row].length; col++) {
            table[row][col] = row*col;
    }
}
// Use the multidimensional array to compute 5*7 
table[5][7] // => 35

// forEach()

let data = [1,2,3,4,5], sum = 0;
// Compute the sum of the elements of the array data.forEach(value => { sum += value; }); // sum == 15
// Now increment each array element
data.forEach(function(v, i, a) { a[i] = v + 1; }); // data == [2,3,4,5,6]

// map()

let a=[1,2,3];
a.map(x => x*x) // => [1, 4, 9]: the function takes input x and returns x*x

// filter()

let a=[5,4,3,2,1];
a.filter(x => x < 3) // => [2, 1]; values less than 3 
a.filter((x,i) => i%2 === 0) // => [5, 3, 1]; every other value
a = a.filter(x => x !== undefined && x !== null);

// find() and findIndex()

let a = [1,2,3,4,5];
a.findIndex(x => x === 3) // => 2; the value 3 appears at index 2
a.findIndex(x =>x<0) // => -1; no negative numbers in the array
a.find(x => x % 5===0) // => 5: this is a multiple of 5
a.find(x => x % 7===0) // => undefined: no multiples of 7 in the array

// every() and some()

let a = [1,2,3,4,5];
a.every(x => x < 10) // => true: all values are < 10. 
a.every(x => x % 2 === 0) // => false: not all values are even.

let a = [1,2,3,4,5];
a.some(x => x%2===0) // => true; a has some even numbers. 
a.some(isNaN) // => false; a has no non-numbers.

// reduce() and reduceRight()
let a = [1,2,3,4,5];
a.reduce((x,y) => x+y, 0) // => 15; the sum of the values 
a.reduce((x,y) => x*y, 1) // => 120; the product of the values 
a.reduce((x,y) => (x > y) ? x : y) // => 5; the largest of the values

// Compute 2^(3^4).  Exponentiation has right-to-left precedence
let a=[2,3,4];
a.reduceRight((acc,val) => Math.pow(val,acc)) // => 2.4178516392292583e+24

// Flattening arrays with flat() and flatMap() 

[1, [2, 3]].flat() // => [1, 2, 3] 
[1, [2, [3]]].flat() // => [1, 2, [3]]

let a = [1, [2, [3, [4]]]];
a.flat(1) // => [1, 2, [3, [4]]]
a.flat(2) // => [1, 2, 3, [4]]
a.flat(3) // => [1, 2, 3, 4]
a.flat(4) // => [1, 2, 3, 4]

let phrases = ["hello world", "the definitive guide"];
let words = phrases.flatMap(phrase => phrase.split(" ")); 
words // => ["hello", "world", "the", "definitive", "guide"];


// Map non-negative numbers to their square roots
[-2, -1, 1, 2].flatMap(x => x < 0 ? [] : Math.sqrt(x)) // => [1, 2**0.5]

// Adding arrays with concat()

let a = [1,2,3];
a.concat(4, 5) // => [1,2,3,4,5]
a.concat([4,5],[6,7]) // => [1,2,3,4,5,6,7]; arrays are flattened 
a.concat(4, [5,[6,7]]) // => [1,2,3,4,5,[6,7]]; but not nested arrays 
a // => [1,2,3]; the original array is unmodified

// Stacks and Queues with push(), pop(), shift(), and unshift()

let stack = []; // stack == []
stack.push(1,2); // stack == [1,2];
stack.pop(); // stack == [1]; returns 2
stack.push(3); // stack == [1,3]
stack.pop(); // stack == [1]; returns 3
stack.push([4,5]); // stack == [1,[4,5]]
stack.pop() // stack == [1]; returns [4,5]
stack.pop(); // stack == []; returns 1

a.push(...values);

let q=[]; // q == []
q.push(1,2); // q == [1,2]
q.shift(); // q == [2]; returns 1
q.push(3) // q == [2, 3]
q.shift() // q == [3]; returns 2
q.shift() // q == []; returns 3

let a=[]; // a == []
a.unshift(1) // a == [1]
a.unshift(2) // a == [2, 1]
a=[]; // a == []
a.unshift(1,2) // a == [1, 2]

// slice() 

let a = [1,2,3,4,5];
a.slice(0,3); // Returns [1,2,3]
a.slice(3); // Returns [4,5]
a.slice(1,-1); // Returns [2,3,4]
a.slice(-3,-2); // Returns [3]

// splice()

let a = [1,2,3,4,5,6,7,8];
a.splice(4) // => [5,6,7,8]; a is now [1,2,3,4]
a.splice(1,2) // => [2,3]; a is now [1,4] 
a.splice(1,1) // => [4]; a is now [1]

let a = [1,2,3,4,5];
a.splice(2,0,"a","b") // => []; a is now [1,2,"a","b",3,4,5] 
a.splice(2,2,[1,2],3) // => ["a","b"]; a is now [1,2,[1,2],3,3,4,5]

// fill()
let a = new Array(5); // Start with no elements and length 5
a.fill(0) // => [0,0,0,0,0]; fill the array with zeros
a.fill(9, 1) // => [0,9,9,9,9]; fill with 9 starting at index 1
a.fill(8, 2, -1) // => [0,9,8,8,9]; fill with 8 at indexes 2, 3

// copyWithin()
let a = [1,2,3,4,5];
a.copyWithin(1) // => [1,1,2,3,4]: copy array elements up one 
a.copyWithin(2, 3, 5) // => [1,1,3,4,4]: copy last 2 elements to index 2 
a.copyWithin(0, -2) // => [4,4,3,4,4]: negative offsets work, too

// indexOf() and lastIndexOf() 
let a = [0,1,2,1,0];
a.indexOf(1) // => 1: a[1] is 1
a.lastIndexOf(1) // => 3: a[3] is 1
a.indexOf(3) // => -1: no element has value 3

// includes() 
let a = [1,true,3,NaN]; 
a.includes(true) // => true
a.includes(2) // => false
a.includes(NaN) // => true
a.indexOf(NaN) // => -1; indexOf can't find NaN

// sort()
let a = ["banana", "cherry", "apple"]; 
a.sort(); // a == ["apple", "banana", "cherry"]
let a = [33, 4, 1111, 222];
a.sort(); // a == [1111, 222, 33, 4]; alphabetical order 
a.sort(function(a,b) { // Pass a comparator function
    return a-b; // Returns < 0, 0, or > 0, depending on order
}); // a == [4, 33, 222, 1111]; numerical order
a.sort((a,b) => b-a); // a == [1111, 222, 33, 4]; reverse numerical order

let a = ["ant", "Bug", "cat", "Dog"];
a.sort(); // a == ["Bug","Dog","ant","cat"]; case-sensitive sort 
a.sort(function(s,t) {
    let a = s.toLowerCase(); 
    let b = t.toLowerCase(); 
    if (a < b) return -1; 
    if (a>b)return 1; 
    return 0;
}); // a == ["ant","Bug","cat","Dog"]; case-insensitive sort

// reverse()
let a = [1,2,3];
a.reverse(); // a == [3,2,1]

// isArray() 
Array.isArray([]) // => true 
Array.isArray({}) // => false

// Function Declarations

// Print the name and value of each property of o.  Return undefined.
function printprops(o) { 
    for(let p in o) {
        console.log(`${p}: ${o[p]}\n`);
    }
}

 // Compute the distance between Cartesian points (x1,y1) and (x2,y2).
 function distance(x1, y1, x2, y2) { 
     let dx=x2-x1; 
     let dy=y2-y1;
     return Math.sqrt(dx*dx + dy*dy);
}

// A recursive function (one that calls itself) that computes factorials
// Recall that x! is the product of x and all positive integers less than it. 
function factorial(x) {
    if (x <= 1) return 1;
    return x * factorial(x-1); 
}

// Function Expressions 
// This function expression defines a function that squares its argument. 
// Note that we assign it to a variable
const square = function(x) { return x*x; };

// Function expressions can include names, which is useful for recursion.
const f = function fact(x) { if (x <= 1) return 1; else return x*fact(x-1); }; 

// Function expressions can also be used as arguments to other functions:
[3,2,1].sort(function(a,b) { return a-b; });

// Function expressions are sometimes defined and immediately invoked:
let tensquared = (function(x) {return x*x;}(10));

// Nested Functions 
function hypotenuse(a, b) {
    function square(x) { return x*x; } 
    return Math.sqrt(square(a) + square(b));
}

// Arrow Functions 
const sum=(x,y)=>{return x+y;};
const sum=(x,y)=>x+y;
const polynomial = x => x*x + 2*x + 3;
const constantFunc = () => 42;

const f = x => { return { value: x }; }; // Good: f() returns an object
const g = x => ({ value: x }); // Good: g() returns an object
const h = x => { value: x }; // Bad: h() returns nothing
const i = x => { v: x, w: x }; // Bad: Syntax Error

// Make a copy of an array with null elements removed.
let filtered = [1,null,2,3].filter(x => x !== null); // filtered == [1,2,3] 
// Square some numbers:
let squares = [1,2,3,4].map(x => x*x); // squares == [1,4,9,16]
