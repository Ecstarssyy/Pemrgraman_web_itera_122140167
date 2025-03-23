function toggleSecondInput() {
    const operation = document.getElementById('operation').value;
    const num2Group = document.getElementById('num2-group');

    if (operation === 'sqrt') {
        num2Group.style.display = 'none';
    } else {
        num2Group.style.display = 'block';
    }
}

function calculate() {
    const num1 = parseFloat(document.getElementById('num1').value);
    const num2 = parseFloat(document.getElementById('num2').value);
    const operation = document.getElementById('operation').value;
    let result;

    if (isNaN(num1) || (operation !== 'sqrt' && isNaN(num2))) {
        document.getElementById('result').innerText = " Masukkan angka yang valid!";
        return;
    }

    switch (operation) {
        case 'add':
            result = num1 + num2;
            break;
        case 'subtract':
            result = num1 - num2;
            break;
        case 'multiply':
            result = num1 * num2;
            break;
        case 'divide':
            result = num2 !== 0 ? num1 / num2 : "Tidak bisa dibagi dengan nol!";
            break;
        case 'power':
            result = Math.pow(num1, num2);
            break;
        case 'sqrt':
            result = num1 >= 0 ? Math.sqrt(num1) : " Akar kuadrat dari bilangan negatif tidak valid!";
            break;
        case 'modulus':
            result = num1 % num2;
            break;
        default:
            result = " Operasi tidak valid!";
    }

    document.getElementById('result').innerText = `Hasil: ${result}`;
}

// Atur tampilan awal
toggleSecondInput();
