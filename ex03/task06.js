function getRandomIntegerFromRange(startRange, endRange) {
    if (!Number, isInteger(startRange) || !Number, isInteger(endRange)) {
        throw new Error("Both must be integers.");
    }


return Math.floor(Math.random() * (endRange - startRange + 1)) + startRange;
}

function getTimeDifferenceInFullDays(startDate, endDate) {
    if (!(startDate instanceof Date) || !(endDate instanceof Date)) {
        throw new Error("Both must be dates.");
    }
    const startUTC = Date.UTC(startDate.getFullYear(), startDate.getMonth(), startDate.getDate());
    const endUTC = Date.UTC(endDate.getFullYear(), endDate.getMonth(), endDate.getDate());

    const millisecondsInDay = 1000 * 60 * 60 * 24;
    const differenceInDays = Math.floor((endUTC - startUTC) / millisecondsInDay);
 
    return differenceInDays;
}