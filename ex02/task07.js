const convertOuncesToGrams = (measurements) => {
    return measurements.map((measurement) => {
        if (measurement.unit === "ounce") {
            const grams = measurement.weight * 28;
            return { ...measurement, unit: "gram", weight: grams.toFixed(2)};
        } else {
            return measurement;
        }
    });
};

const measurements = [
    { batchid: 434, unit: "ounce", weight: 12.21 }, 
    {batchid: 414, unit: "gram", weight: 199.54 },
    { batchid: 522, unit: "ounce", weight: 18.88 }
];

const measurementsInGrams = convertOuncesToGrams(measurements);
console.log(measurementsInGrams);