const registrationForm = document.getElementById('registrationForm');
        const confirmationMessage = document.getElementById('confirmationMessage');

        registrationForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const email = document.getElementById('email').value;

            confirmationMessage.textContent = `На почту ${email} отправлено письмо с подтверждением.`;
        });
