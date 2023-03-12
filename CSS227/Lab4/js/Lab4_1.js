let reset = document.querySelector("input");
reset.addEventListener("click", function () {
    let table = document.querySelector("table");
    for (let i = 0; i < table.rows.length; i++) {
        for (let j = 0; j < table.rows[i].cells.length; j++) {
            table.rows[i].cells[j].textContent = "";
        }
    }
    turn = 0;
    document.querySelector("#winner").textContent = "";
});

let turn = 0;
let table = document.querySelector("table");
let winner = document.querySelector("#winner");

for (let i = 0; i < table.rows.length; i++) {
    for (let j = 0; j < table.rows[i].cells.length; j++) {
        table.rows[i].cells[j].addEventListener("click", function () {
            if (table.rows[i].cells[j].textContent == "") {
                if (turn % 2 == 0) {
                    table.rows[i].cells[j].textContent = "X";
                    turn++;
                } else if (turn % 2 == 1) {
                    if (checkXnone(i, j) == true) {
                        botPlay();
                    }
                }
                checkDraw();
                checkWinner();
            }
        });
    }
    if (winner == "X is the winner" || winner == "O is the winner") {
        for (let k = 0; k < table.rows.length; k++) {
            for (let l = 0; l < table.rows[k].cells.length; l++) {
                if (checkEmpty(k, l) == true) {
                    table.rows[k].cells[l].textContent = " ";
                }
            }
        }
    }
}

function addEmpty() {
    for (let i = 0; i < table.rows.length; i++) {
        for (let j = 0; j < table.rows[i].cells.length; j++) {
            if (checkEmpty(i, j) == true) {
                table.rows[i].cells[j].textContent = " ";
                table.rows[i].cells[j].removeEventListener("click", function () { });
            }
        }
    }
}

function checkEmpty(i, j) {
    if (table.rows[i].cells[j].textContent == "") {
        return true;
    } else {
        return false;
    }
}

function botPlay() {
    let randomRow = Math.floor(Math.random() * 3);
    let randomColumn = Math.floor(Math.random() * 3);
    if (table.rows[randomRow].cells[randomColumn].textContent == "") {
        table.rows[randomRow].cells[randomColumn].textContent = "O";
        turn++;
    } else {
        botPlay();
    }
}

function checkXnone(i, j) {
    if (table.rows[i].cells[j].textContent == "") {
        return true;
    } else {
        return false;
    }
}

function checkDraw() {
    let count = 0;
    for (let i = 0; i < table.rows.length; i++) {
        for (let j = 0; j < table.rows[i].cells.length; j++) {
            if (table.rows[i].cells[j].textContent != "") {
                count++;
            }
        }
    }
    if (count == 9) {
        winner.textContent = "Draw";
    }
}

function checkWinner() {
    // check row
    for (let i = 0; i < table.rows.length; i++) {
        if (table.rows[i].cells[0].textContent == "X" && table.rows[i].cells[1].textContent == "X" && table.rows[i].cells[2].textContent == "X") {
            winner.textContent = "X is the winner";
            turn = 0;
            addEmpty();
        } else if (table.rows[i].cells[0].textContent == "O" && table.rows[i].cells[1].textContent == "O" && table.rows[i].cells[2].textContent == "O") {
            winner.textContent = "O is the winner";
            turn = 0;
            addEmpty();
        }
    }
    // check column
    for (let i = 0; i < table.rows.length; i++) {
        if (table.rows[0].cells[i].textContent == "X" && table.rows[1].cells[i].textContent == "X" && table.rows[2].cells[i].textContent == "X") {
            winner.textContent = "X is the winner";
            turn = 0;
            addEmpty();
        } else if (table.rows[0].cells[i].textContent == "O" && table.rows[1].cells[i].textContent == "O" && table.rows[2].cells[i].textContent == "O") {
            winner.textContent = "O is the winner";
            turn = 0;
            addEmpty();
        }
    }
    // check diagonal
    if (table.rows[0].cells[0].textContent == "X" && table.rows[1].cells[1].textContent == "X" && table.rows[2].cells[2].textContent == "X") {
        winner.textContent = "X is the winner";
        turn = 0;
        addEmpty();
    } else if (table.rows[0].cells[0].textContent == "O" && table.rows[1].cells[1].textContent == "O" && table.rows[2].cells[2].textContent == "O") {
        winner.textContent = "O is the winner";
        turn = 0;
        addEmpty();
    } else if (table.rows[0].cells[2].textContent == "X" && table.rows[1].cells[1].textContent == "X" && table.rows[2].cells[0].textContent == "X") {
        winner.textContent = "X is the winner";
        turn = 0;
        addEmpty();
    } else if (table.rows[0].cells[2].textContent == "O" && table.rows[1].cells[1].textContent == "O" && table.rows[2].cells[0].textContent == "O") {
        winner.textContent = "O is the winner";
        turn = 0;
        addEmpty();
    }
}