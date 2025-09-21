function showSignUp() {
    document.getElementById('login-form').classList.add('hidden');
    document.getElementById('signup-form').classList.remove('hidden');
}

function showLogin() {
    document.getElementById('signup-form').classList.add('hidden');
    document.getElementById('login-form').classList.remove('hidden');
}

// Signup function
function signup() {
    const username = document.getElementById('signup-username').value;
    const email = document.getElementById('signup-email').value;
    const phone = document.getElementById('signup-phone').value;
    const password = document.getElementById('signup-password').value;
    const confirm = document.getElementById('signup-confirm').value;

    if (password !== confirm) {
        alert("Passwords do not match!");
        return;
    }

    let users = JSON.parse(localStorage.getItem("users")) || [];

    const userExists = users.some(user => user.email === email || user.phone === phone);
    if (userExists) {
        alert("User with this email or phone already exists!");
        return;
    }

    users.push({ username, email, phone, password });
    localStorage.setItem("users", JSON.stringify(users));
    alert("Signup successful! You can now log in.");
    showLogin();
}

// Login function
function login() {
    const identifier = document.getElementById('login-identifier').value;
    const password = document.getElementById('login-password').value;

    let users = JSON.parse(localStorage.getItem("users")) || [];

    const user = users.find(user =>
        (user.email === identifier || user.phone === identifier) && user.password === password
    );

    if (user) {
        alert(`Welcome, ${user.username}!`);
    } else {
        alert("Invalid email/phone or password.");
    }
}
