// Базовый класс Film
class FilmC {
    constructor(name, country, genre, duration, budget, poster, description, rating) {
        this.name = name;
        this.country = country; // предположим, что Country это строка
        this.genre = genre; // предположим, что Genre это строка
        this.duration = duration;
        this.budget = budget;
        this.poster = poster;
        this.description = description;
        this.rating = rating;
    }

    getName() {
        return this.name;
    }

    setName(name) {
        this.name = name;
    }

    getCountry() {
        return this.country;
    }

    setCountry(country) {
        this.country = country;
    }

    getGenre() {
        return this.genre;
    }

    setGenre(genre) {
        this.genre = genre;
    }

    getDuration() {
        return this.duration;
    }

    setDuration(duration) {
        this.duration = duration; // можно добавить проверку на мин/макс
    }

    getBudget() {
        return this.budget;
    }

    setBudget(budget) {
        this.budget = budget;
    }

    getPoster() {
        return this.poster;
    }

    setPoster(poster) {
        this.poster = poster;
    }

    getDescription() {
        return this.description;
    }

    setDescription(description) {
        this.description = description;
    }

    getRating() {
        return this.rating;
    }

    setRating(rating) {
        this.rating = rating; // можно добавить проверку на мин/макс
    }

     // метод для отображения всей информации о фильме
    getInfo() {
        return `Name: ${this.name}, Country: ${this.country}, Genre: ${this.genre}, Duration: ${this.duration}, Budget: ${this.budget}, Poster: ${this.poster}, Description: ${this.description}, Rating: ${this.rating}`;
    }
}

// Декоратор, который проверяет, не превышает ли описание максимально допустимую длину
function maxLengthDecorator(film, maxLength) {
    const originalSetDescription = film.setDescription.bind(film);

    film.setDescription = function (description) {
        if (description.length > maxLength) {
            throw new Error(`Description is too long! Maximum length is ${maxLength}.`);
        }
        originalSetDescription(description);
    };

    return film;
}

// Создаем объект фильма
const newFilm = new FilmC('Inception', 'United States', 'Science', 148, 160000000, 'poster.jpg',
    'A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O.',
    8.8);

maxLengthDecorator(newFilm, 500);

// отображаем информацию о фильме при загрузке страницы
window.onload = function() {
    document.getElementById('filmDiv').innerHTML = newFilm.getInfo();
};

function testInput() {
    document.getElementById('errorDiv').innerHTML = '';
    try {
        newFilm.setDescription(document.getElementById('myInput').value);
        document.getElementById('filmDiv').innerHTML = newFilm.getInfo();
    } catch (error) {
        document.getElementById('errorDiv').innerHTML = error.message;
    }
}

function testError() {
    try {
        newFilm.setDescription('A'.repeat(501));
        document.getElementById('filmDiv').innerHTML = newFilm.getInfo();
    } catch (error) {
        document.getElementById('errorDiv').innerHTML = error.message;
    }
}

class AnimatedFilmC extends FilmC {
    constructor(name, country, genre, duration, budget, poster, description, rating, animationStyle, targetAge) {
        super(name, country, genre, duration, budget, poster, description, rating);
        this.animationStyle = animationStyle; // предположим, что animationStyle - это строка
        this.targetAge = targetAge; // предположим, что targetAge - это число
    }
    getAnimationStyle() {
        return this.animationStyle;
    }
    setAnimationStyle(animationStyle) {
        this.animationStyle = animationStyle;
    }
    getTargetAge() {
        return this.targetAge;
    }
    setTargetAge(targetAge) {
        this.targetAge = targetAge;
    }
    infoAnimationStyle() {
        return `This is a ${this.animationStyle} animation.`
    }
    isSuitableForChild(childAge) {
        return childAge >= this.targetAge;
    }
    getInfo() {
        return super.getInfo() + `, Animation Style: ${this.animationStyle}, Target Age: ${this.targetAge}`;
    }
}

// создается объект анимационного фильма
const newAnimatedFilm = new AnimatedFilmC('Toy Story', 'United States', 'Animation', 81, 30000000, 'toystory_poster.jpg',
    'A cowboy doll is profoundly threatened and jealous when a new spaceman figure supplants him as top toy in a boy\'s room.',
    8.3, '3D', 7);
maxLengthDecorator(newAnimatedFilm, 500);

window.onload = function() {
    document.getElementById('filmDiv').innerHTML = newAnimatedFilm.getInfo();
};

function testInput() {
    document.getElementById('errorDiv').innerHTML = '';
    try {
        newAnimatedFilm.setDescription(document.getElementById('myInput').value);
        document.getElementById('filmDiv').innerHTML = newAnimatedFilm.getInfo();
    } catch (error) {
        document.getElementById('errorDiv').innerHTML = error.message;
    }
}

function testError() {
    try {
        newAnimatedFilm.setDescription('A'.repeat(501));
        document.getElementById('filmDiv').innerHTML = newAnimatedFilm.getInfo();
    } catch (error) {
        document.getElementById('errorDiv').innerHTML = error.message;
    }
}

//function FilmC(name, country, genre, duration, budget, poster, description, rating) {
//    this.name = name;
//    this.country = country
//    this.genre = genre;
//    this.duration = duration;
//    this.budget = budget;
//    this.poster = poster;
//    this.description = description;
//    this.rating = rating;
//}
//
//FilmC.prototype.getInfo = function() {
//    return `Name: ${this.name}, Country: ${this.country}, Genre: ${this.genre}, Duration: ${this.duration}, Budget: ${this.budget}, Poster: ${this.poster}, Description: ${this.description}, Rating: ${this.rating}`;
//};
//
//function AnimatedFilmC(name, country, genre, duration, budget, poster, description, rating, animationStyle, targetAge) {
//    FilmC.call(this, name, country, genre, duration, budget, poster, description, rating);
//    this.animationStyle = animationStyle;
//    this.targetAge = targetAge;
//}
//
//AnimatedFilmC.prototype = Object.create(FilmC.prototype);
//AnimatedFilmC.prototype.constructor = AnimatedFilmC;
//
//AnimatedFilmC.prototype.getAnimationStyle = function() {
//    return this.animationStyle;
//};
//
//AnimatedFilmC.prototype.infoAnimationStyle = function() {
//    return `This is a ${this.animationStyle} animation.`;
//};
//
//AnimatedFilmC.prototype.isSuitableForChild = function(childAge) {
//    return childAge >= this.targetAge;
//};
//
//AnimatedFilmC.prototype.getInfo = function () {
//    const filmInfo = FilmC.prototype.getInfo.call(this);
//    return `${filmInfo}, Animation Style: ${this.animationStyle}, Target Age: ${this.targetAge}`;
//};
//
//// И затем создаем наши объекты
//const animatedFilm = new AnimatedFilmC('Toy Story', 'United States', 'Animation', 81, 30000000, 'toystory_poster.jpg',
//    'A cowboy doll is profoundly threatened and jealous when a new spaceman figure supplants him as top toy in a boy\'s room.',
//    8.3, '3D', 7);
