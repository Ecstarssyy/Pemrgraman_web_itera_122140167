function validateForm() {
    const name = document.getElementById('name').value.trim();
    const email = document.getElementById('email').value.trim();
    const password = document.getElementById('password').value.trim();
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    if (name.length <= 3) {
        alert('⚠ Nama harus lebih dari 3 karakter');
        return false;
    }

    if (!emailPattern.test(email)) {
        alert('⚠ Email tidak valid');
        return false;
    }

    if (password.length < 8) {
        alert('⚠ Kata sandi harus minimal 8 karakter');
        return false;
    }

    alert('✅ Form valid!');
    return true;
}

function togglePasswordVisibility() {
    const passwordInput = document.getElementById('password');
    passwordInput.type = passwordInput.type === 'password' ? 'text' : 'password';
}
