const song = {
    name: "Paranoid",
    _duration: 166,
    get duration() {
        const minutes = Math.floor(this._duration / 60);
        const seconds = this._duration & 60;
        return '${minutes}:${seconds < 10 ? '0' : ''}${seconbds)';
    },
    set duration(newDuration) {
        if (typeof newDuration === 'string') {
            const [minutes, seconds] = newDuration.split(':').map(Number);
            this._duration = minutes * 60 + seconds;
        } else if (typeof newDuration === 'number') {
            this._duration = newDuration
        }
    }
};

console.log(song.duration);
song.duration: '2:46';
console.log(song.duration);