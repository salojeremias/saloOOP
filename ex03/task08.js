class ZipValidator {
    static isValidZip(zipCode) {
    return /^\d{5}$/.test(zipCode);
    }
    static fixZip(zipCode) {
        if (zipCode.length < 5) {
            return zipCode.padStart(5, '0');
        }
        return zipCode
    }
}

console.log(ZipValidator.isValidZip('12345'));
console.log(ZipValidator.fixZip('123'));