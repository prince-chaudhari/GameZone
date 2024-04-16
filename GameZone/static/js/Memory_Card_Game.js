let cardsArray = [
    {
        'name': 'CSS',
        'img': 'https://upload.wikimedia.org/wikipedia/commons/d/d5/CSS3_logo_and_wordmark.svg',
    },
    {
        'name': 'HTML',
        'img': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS1HVNHQmF6XqXS0xqpvfcJFY3cQIAQEB3XmJ_edOZdMQ&s',
    },
    {
        'name': 'jQuery',
        'img': 'https://www.devopsschool.com/blog/wp-content/uploads/2022/03/jquery.png',
    },
    {
        'name': 'JS',
        'img': 'https://upload.wikimedia.org/wikipedia/commons/6/6a/JavaScript-logo.png',
    },
    {
        'name': 'Node',
        'img': 'https://miro.medium.com/v2/resize:fit:800/1*bc9pmTiyKR0WNPka2w3e0Q.png',
    },
    {
        'name': 'Python',
        'img': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Python.svg/1200px-Python.svg.png',
    },
    {
        'name': 'Java',
        'img': 'https://logowik.com/content/uploads/images/731_java.jpg',
    },
    {
        'name': 'C++',
        'img': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR76UcuFZq_9Mf_wKOo0MDZy9lyMzqtpXrJiT2p0rZCwA&s',
    },
    {
        'name': 'React',
        'img': 'https://miro.medium.com/v2/resize:fit:1200/1*y6C4nSvy2Woe0m7bWEn4BA.png',
    },
    {
        'name': 'PostgreSql',
        'img': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRaq3l0n92GEdtCjjeexhagyesPHPytq0FcPzY49sHl8g&s',
    },
];

const parentDiv = document.querySelector('#card-section');

const gameCard = cardsArray.concat(cardsArray);

const myNumbers = (array) => {
    for (let i = array.length - 1; i > 0; i--) {
        let j = Math.floor(Math.random() * (i + 1));
        let temp = array[i];
        array[i] = array[j];
        array[j] = temp;
    }
    return array;
}

const shuffledChild = myNumbers(gameCard);

let clickCount = 0;
let firstCard = "";
let secondCard = "";

const card_matches = () => {
    let card_selected = document.querySelectorAll('.card-selected');

    card_selected.forEach((curEle) => {
        curEle.classList.add('card_match')
    })
}

const resetGame = () => {
    firstCard = "";
    secondCard = "";
    clickCount = 0;

    let card_selected = document.querySelectorAll('.card-selected');

    card_selected.forEach((curEle) => {
        curEle.classList.remove('card-selected');
    })
}

parentDiv.addEventListener('click', (event) => {
    let curCard = event.target;
    if (curCard.id === 'card-section') return false;
    clickCount++;

    if (clickCount < 3) {
        curCard.parentNode.classList.add('card-selected');
        if (clickCount === 1) {
            firstCard = curCard.parentNode.dataset.name;
        } else {
            secondCard = curCard.parentNode.dataset.name;
        }
        if (firstCard !== '' && secondCard !== '') {
            if (firstCard === secondCard) {
                setTimeout(() => {
                    card_matches();
                    resetGame();
                }, 1000);
            }
            else {
                setTimeout(() => {
                    resetGame();
                }, 1000);
            }
        }

    }

})

for (let i = 0; i < shuffledChild.length; i++) {
    const childDiv = document.createElement('div');
    childDiv.classList.add('card');
    childDiv.dataset.name = shuffledChild[i].name;

    const front_div = document.createElement('div');
    front_div.classList.add('front-card');

    const back_div = document.createElement('div');
    back_div.classList.add('back-card');
    back_div.style.backgroundImage = `url(${shuffledChild[i].img})`;

    parentDiv.appendChild(childDiv);

    childDiv.appendChild(front_div);
    childDiv.appendChild(back_div);

}