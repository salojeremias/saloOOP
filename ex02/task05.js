function color(color = 'Purple') {
    console.log("The color, " + color + "is my favorite")
}

function sum(...numbers) {
    return numbers.reduce((acc, curr) => acc + curr, 0);
}