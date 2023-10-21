const inputElement = document.getElementById('nameInput');

        inputElement.addEventListener('input', (event) => {
            const inputText = event.target.value;
            let filteredText = '';

            for (let i = 0; i < inputText.length; i++) {
                const char = inputText[i];
                if (!/\d/.test(char)) {
                    filteredText += char;
                }
            }

            event.target.value = filteredText;
        });
