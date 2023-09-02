const canvas = document.querySelector("canvas")
const ctx = canvas.getContext("2d")

const score = document.querySelector(".score--value")
const highscore = document.querySelector(".highscore--value")
const finalScore = document.querySelector(".final-score > span")
const menu = document.querySelector(".menu-screen")
const buttonPlay = document.querySelector(".btn-play")
const buttonSpeed = document.querySelector(".btn-speed")
const buttonObject = document.querySelector(".btn-object")
const buttonZerar = document.querySelector(".btn-zerar")

function zerar() {
    localStorage.setItem("snakeHighScore", 0);
    highscore.innerText = getHighScore();
}

const audio = new Audio("../assets/audio.mp3")

const size = 30

const initialPosition = { x: 270, y: 240 }

let snake = [initialPosition]

highscore.innerText = getHighScore();

function getHighScore() {
    const savedScore = localStorage.getItem("snakeHighScore");

    if (savedScore !== null) {
        return parseInt(savedScore, 10);
    } else {
        return 0; // Retorna 0 se não houver pontuação salva no localStorage
    }
}

let objects = [];
const maxObjects = 10;

const incrementScore = () => {
    score.innerText = +score.innerText + 10
}

const randomNumber = (min, max) => {
    return Math.round(Math.random() * (max - min) + min)
}

const randomPosition = () => {
    let x, y;

    do {
        x = randomNumber(0, canvas.width - size);
        y = randomNumber(0, canvas.height - size);
    } while (
        snake.find((position) => position.x === x && position.y === y) ||
        objects.find((obj) => obj.x === x && obj.y === y)
    );

    return Math.round(x / 30) * 30;
};

const randomColor = () => {
    const red = randomNumber(0, 255)
    const green = randomNumber(0, 255)
    const blue = randomNumber(0, 255)

    return `rgb(${red}, ${green}, ${blue})`
}

const food = {
    x: randomPosition(),
    y: randomPosition(),
    color: randomColor()
}

let direction, loopId

const drawFood = () => {
    const { x, y, color } = food

    const img = new Image();
    img.src = "data:image/svg+xml;charset=utf-8,<svg width='800px' height='800px' viewBox='0 0 1024 1024' class='icon' version='1.1' xmlns='http://www.w3.org/2000/svg'><path d='M422.4 917.333333c-14.933333 0-29.866667 0-44.8-2.133333-98.133333-10.666667-179.2-57.6-224-132.266667-108.8-177.066667 2.133333-277.333333 108.8-371.2 27.733333-25.6 57.6-51.2 83.2-78.933333 8.533333-8.533333 17.066667-19.2 25.6-27.733333 115.2-128 243.2-273.066667 422.4-149.333334 72.533333 51.2 115.2 128 125.866667 224 12.8 132.266667-42.666667 283.733333-142.933334 388.266667-98.133333 93.866667-228.266667 149.333333-354.133333 149.333333z' fill='%238D6E63' /><path d='M422.4 917.333333c-14.933333 0-29.866667 0-44.8-2.133333-98.133333-10.666667-179.2-57.6-224-132.266667-29.866667-49.066667-42.666667-89.6-44.8-128 206.933333 187.733333 716.8 46.933333 808.533333-277.333333 12.8 132.266667-42.666667 283.733333-142.933333 388.266667-96 96-226.133333 151.466667-352 151.466666z' fill='%23795548' /><path d='M480 821.333333m-32 0a32 32 0 1 0 64 0 32 32 0 1 0-64 0Z' fill='%233E2723' /><path d='M725.333333 277.333333c12.8 0 21.333333 8.533333 21.333334 21.333334s-8.533333 21.333333-21.333334 21.333333-21.333333-8.533333-21.333333-21.333333 8.533333-21.333333 21.333333-21.333334z m0 234.666667c0 12.8 8.533333 21.333333 21.333334 21.333333s21.333333-8.533333 21.333333-21.333333-8.533333-21.333333-21.333333-21.333333-21.333333 8.533333-21.333334 21.333333z m-170.666666-149.333333c0 12.8 8.533333 21.333333 21.333333 21.333333s21.333333-8.533333 21.333333-21.333333-8.533333-21.333333-21.333333-21.333334-21.333333 8.533333-21.333333 21.333334zM298.666667 682.666667c0 12.8 8.533333 21.333333 21.333333 21.333333s21.333333-8.533333 21.333333-21.333333-8.533333-21.333333-21.333333-21.333334-21.333333 8.533333-21.333333 21.333334z m128-74.666667c0 17.066667 14.933333 32 32 32s32-14.933333 32-32-14.933333-32-32-32-32 14.933333-32 32z' fill='%235D4037' /></svg>";

    img.onload = function () {
        ctx.drawImage(img, x, y, size, size); // Desenhe o SVG no canvas nas coordenadas (0, 0) com largura e altura de 100x100 pixels
    };

    ctx.shadowColor = color
    ctx.shadowBlur = 6
    ctx.fillStyle = color
    ctx.shadowBlur = 0
    ctx.fillRect(x, y, size, size)
}

const drawSnake = () => {
    ctx.fillStyle = "#ddd"

    snake.forEach((position, index) => {
        if (index == snake.length - 1) {
            ctx.fillStyle = "white"
        }

        ctx.fillRect(position.x, position.y, size, size)
    })
}

const moveSnake = () => {
    if (!direction) return

    const head = snake[snake.length - 1]

    if (direction == "right") {
        snake.push({ x: head.x + size, y: head.y })
    }

    if (direction == "left") {
        snake.push({ x: head.x - size, y: head.y })
    }

    if (direction == "down") {
        snake.push({ x: head.x, y: head.y + size })
    }

    if (direction == "up") {
        snake.push({ x: head.x, y: head.y - size })
    }

    snake.shift()
}

const drawGrid = () => {
    ctx.lineWidth = 1
    ctx.strokeStyle = "#191919"

    for (let i = 30; i < canvas.width; i += 30) {
        ctx.beginPath()
        ctx.lineTo(i, 0)
        ctx.lineTo(i, 600)
        ctx.stroke()

        ctx.beginPath()
        ctx.lineTo(0, i)
        ctx.lineTo(600, i)
        ctx.stroke()
    }
}

const chackEat = () => {
    const head = snake[snake.length - 1]

    if (head.x == food.x && head.y == food.y) {
        incrementScore()
        snake.push(head)
        audio.play()

        let x = randomPosition()
        let y = randomPosition()

        while (snake.find((position) => position.x == x && position.y == y)) {
            x = randomPosition()
            y = randomPosition()
        }

        food.x = x
        food.y = y
        food.color = randomColor()
    }
}

const checkCollision = () => {
    const head = snake[snake.length - 1]
    const canvasLimit = canvas.width - size
    const neckIndex = snake.length - 2

    const wallCollision =
        head.x < 0 || head.x > canvasLimit || head.y < 0 || head.y > canvasLimit

    const selfCollision = snake.find((position, index) => {
        return index < neckIndex && position.x == head.x && position.y == head.y
    })

    if (wallCollision || selfCollision) {
        gameOver()
    }
}

const gameOver = () => {
    direction = undefined
    objects = [];
    buttonObject.innerText = "0";
    // Verifique se a nova pontuação é maior do que a pontuação salva no localStorage
    const currentScore = parseInt(score.innerText, 10);
    const savedScore = localStorage.getItem("snakeHighScore");

    if (savedScore === null || currentScore > savedScore) {
        localStorage.setItem("snakeHighScore", currentScore);
    }

    highscore.innerText = getHighScore();

    menu.style.display = "flex"
    finalScore.innerText = score.innerText
    canvas.style.filter = "blur(2px)"
}

let gameSpeed = 300;

buttonSpeed.addEventListener("click", () => {
    if (gameSpeed === 300) {
        gameSpeed = 200;
        buttonSpeed.innerText = "Medium";
    } else if (gameSpeed === 200) {
        gameSpeed = 100;
        buttonSpeed.innerText = "Hard";
    } else if (gameSpeed === 100) {
        gameSpeed = 50;
        buttonSpeed.innerText = "Brutal";
    } else {
        gameSpeed = 300;
        buttonSpeed.innerText = "Easy";
    }
});

const drawObject = () => {
    ctx.fillStyle = "red";

    for (const obj of objects) {
        ctx.fillRect(obj.x, obj.y, size, size);
    }
};

const checkObjectCollision = () => {
    const head = snake[snake.length - 1];

    for (let i = 0; i < objects.length; i++) {
        const obj = objects[i];
        if (head.x === obj.x && head.y === obj.y) {
            objects.splice(i, 1); // Remova o objeto da lista
            gameOver();
            break; // Pare de verificar após encontrar uma colisão
        }
    }
};

let object = { x: randomPosition(), y: randomPosition() };
const objectSize = 30;

buttonObject.addEventListener("click", () => {
    if (objects.length < maxObjects) {
        objects.push({ x: randomPosition(), y: randomPosition() });
        buttonObject.innerText = objects.length;
    } else {
        objects = [];
        buttonObject.innerText = "0";
    }
});

const gameLoop = () => {
    clearInterval(loopId);

    ctx.clearRect(0, 0, 600, 600);
    drawGrid();
    drawFood();
    moveSnake();
    drawSnake();
    chackEat();
    drawObject(); // Adicione esta linha
    checkCollision();
    checkObjectCollision(); // Adicione esta linha

    loopId = setTimeout(() => {
        gameLoop();
    }, gameSpeed);
};

gameLoop()

document.addEventListener("keydown", ({ key }) => {
    if (key == "ArrowRight" && direction != "left") {
        direction = "right"
    }

    if (key == "ArrowLeft" && direction != "right") {
        direction = "left"
    }

    if (key == "ArrowDown" && direction != "up") {
        direction = "down"
    }

    if (key == "ArrowUp" && direction != "down") {
        direction = "up"
    }
})

buttonPlay.addEventListener("click", () => {
    score.innerText = "00"
    menu.style.display = "none"
    canvas.style.filter = "none"

    snake = [initialPosition]
})

buttonZerar.addEventListener("click", () => {
    zerar();
});