// let music = new Audio('music.mp3');
let turn = new Audio('ting.mp3');
let gameOver = new Audio('gameover.mp3');

const selectBox = document.querySelector(".select-box"),
selectXBtn = selectBox.querySelector(".playerX"),
selectOBtn = selectBox.querySelector(".playerO"),
playBoard = document.querySelector(".play-board"),
players = document.querySelector('.players'),
resultBox = document.querySelector('.result-box'),
wonText = resultBox.querySelector('.won-text'),
newGameBtn = resultBox.querySelector('button'),
boxes = document.querySelectorAll('.box'),
resetBtn = document.querySelector('#reset-btn');

let cnt = 0;

const winPatterns = [
    [0, 1, 2],
    [0, 3, 6],
    [0, 4, 8],
    [1, 4, 7],
    [2, 5, 8],
    [2, 4, 6],
    [3, 4, 5],
    [6, 7, 8],
];

window.onload = () => {
    selectXBtn.onclick = () => {
        selectBox.classList.add('hide');
        playBoard.classList.add('show');
    }
    selectOBtn.onclick = () => {
        selectBox.classList.add('hide');
        playBoard.classList.add('show');
        players.setAttribute('class', 'players active');
    }
}       

boxes.forEach((box) => {
    box.addEventListener('click', () => {
        turn.play();
        if (players.classList.contains('active')) {
            players.classList.remove('active');
            box.innerHTML = '0';
            turn0 = false;
        } else {
            players.classList.add('active');        
            box.innerHTML = 'X';
            turn0 = true;
        }
        box.style.pointerEvents = "none";
        ++cnt;
        checkWinner();
    });
});



const checkWinner = () => {
    if(cnt >= 9) drawGame();
    for (let pattern of winPatterns) {
        let pos1Val = boxes[pattern[0]].innerHTML;
        let pos2Val = boxes[pattern[1]].innerHTML;
        let pos3Val = boxes[pattern[2]].innerHTML;

        if (pos1Val != '' && pos2Val != '' && pos3Val != '') {
            if (pos1Val === pos2Val && pos2Val === pos3Val) {
                showWinner(pos1Val);
                break;
            }
        }
    }
    
};

const showWinner = (winner) => {
    gameOver.play();
    setTimeout(() => {
        playBoard.classList.remove('show');
        resultBox.classList.add('show');
    },800);
    
    wonText.innerHTML = `Player <p>${winner}</p> won the game!`;
    
};

const drawGame = () => {
    gameOver.play();
    setTimeout(() => {
        playBoard.classList.remove('show');
        resultBox.classList.add('show');
    },500);
    
    wonText.innerHTML = `Match has been drawn!`;
    
};

const resetGame = () => {
    boxes.forEach((box) => {
        box.innerHTML = '';
        box.style.pointerEvents = "auto";
        cnt = 0;
    })
}

resetBtn.addEventListener('click', resetGame);

newGameBtn.onclick = () => {
    window.location.reload();
}   