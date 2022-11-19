function multiply(a, b) {
    return a * b
}

function updateLight(current) {

    if (current == "green") {
        return "yellow"
    } else if (current == "yellow") {
        return "red"
    } else {
        return "green"
    }
}

function findOutlier(integers) {
    let even = [];
    let odd = [];
    for (let i = 0; i < integers.length; i++) {
        if (integers[i] % 2 === 0) {
            even.push(integers[i]);
        } else {
            odd.push(integers[i]);
        }
    }
    if (even.length === 1) {
        return even[0];
    } else {
        return odd[0];
    }
}

const quarterOf = (month) => {
    if (month < 4) {
        return 1;
    } else if (month < 7) {
        return 2;
    } else if (month < 10) {
        return 3;
    } else {
        return 4;
    }

}


function noSpace(x) {
    let text = x;
    let result = x.split(" ").join("");
    return result
}


function boolToWord(bool) {
    if (bool === true) {
        return "Yes"
    } else if (bool === false) {
        return "No"
    }
}


const stringToNumber = function (str) {
    const parsed = parseInt(str);
    return parsed;
}


function betterThanAverage(classPoints, yourPoints) {
    let sum = 0
    for (let i = 0; i < classPoints.length; i++) {
        sum += classPoints[i]
    }
    mean = sum / classPoints.length
    if (mean < yourPoints) {
        return true;
    } else {
        return false;
    }
}


var isSquare = function (n) {
    let x = Math.sqrt(n);
    if (x % 1 != 0) {
        return false;
    } else {
        return true;
    }
}


function isTriangle(a, b, c) {
    if (a + b <= c) {
        return false;
    } else if (a + c <= b) {
        return false;
    } else if (b + c <= a) {
        return false;
    } else {
        return true;
    }
} 


function oddOrEven(array) {
    let sum = array.reduce((a, c) => {
        return a + c;
    }, 0);
    if (sum % 2 == 0) {
        return 'even';
    } else {
        return 'odd';
    }
}