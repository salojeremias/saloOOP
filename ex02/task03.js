const convertToMinutesFormat = (hoursInHunderdths) => {
    const hours = Math.floor(hoursInHunderdths)
    const minutes = Math.round((hoursInHunderdths % 1) * 60);
    return '${hours}:${minutes.toString().padStart(2, "0")}'
};