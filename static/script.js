
  function validateForm(event) {
    event.preventDefault(); // Prevent default form submission
    
    // Get form fields
    const title = document.getElementById('title');
    const desc = document.getElementById('desc');
    let isValid = true;

    // Validate Title
    if (!title.value.trim()) {
      title.classList.add('is-invalid');
      isValid = false;
    } else {
      title.classList.remove('is-invalid');
    }

    // Validate Description
    if (!desc.value.trim()) {
      desc.classList.add('is-invalid');
      isValid = false;
    } else {
      desc.classList.remove('is-invalid');
    }

    // If all validations pass, submit the form
    if (isValid) {
      event.target.submit();
    }
  }
