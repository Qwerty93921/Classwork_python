const loginForm = document.getElementById('loginForm');
        const greeting = document.getElementById('greeting');

        loginForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const username = document.getElementById('username').value;
            const remember = document.getElementById('remember').checked;

            if (remember) {
                greeting.textContent = `Привет, ${username}! Я тебя запомнил.`;
            } else {
                greeting.textContent = `Привет, ${username}! Я тебя не запомнил.`;
            }
        });
