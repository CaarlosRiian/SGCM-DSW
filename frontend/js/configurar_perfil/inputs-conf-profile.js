const cellphoneInput = document.getElementById('cellphoneInput');
    cellphoneInput.addEventListener('input', (event) => {
      let input = event.target.value;

      const cursorPosition = event.target.selectionStart;

      const onlyNumbers = input.replace(/\D/g, '');

      let formatted = '';
      if (onlyNumbers.length > 0) formatted += `(${onlyNumbers.substring(0, 2)}`;
      if (onlyNumbers.length > 2) formatted += `) ${onlyNumbers.substring(2, 7)}`;
      if (onlyNumbers.length > 7) formatted += `-${onlyNumbers.substring(7, 11)}`;

      event.target.value = formatted;

      const newCursorPosition = cursorPosition + (formatted.length - input.length);
      event.target.setSelectionRange(newCursorPosition, newCursorPosition);
    });