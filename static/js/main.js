document.addEventListener("DOMContentLoaded", function () {
    const checkboxes = document.querySelectorAll("input[name='categories']");
    
    checkboxes.forEach(checkbox => {
        checkbox.addEventListener("change", function () {
            const checkedBoxes = document.querySelectorAll("input[name='categories']:checked");
            
            if (checkedBoxes.length > 3) {
                this.checked = false; // Prevent selecting more than 3
                alert("You can select up to 3 categories only.");
            } else if (checkedBoxes.length === 0) {
                alert("You must select at least one category.");
            }
        });
    });
});

document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");
    const submitButton = document.querySelector("button[type='submit']");
    const requiredFields = form.querySelectorAll("[required]");
    const categoryCheckboxes = form.querySelectorAll("input[name='categories']");
    
    function validateForm() {
        let allFilled = true;
        // Check if required fields are filled
        requiredFields.forEach(field => {
            if (!field.value.trim()) {
                allFilled = false;
            }
        });
        // Check if at least one category is selected
        const checkedCategories = Array.from(categoryCheckboxes).some(checkbox => checkbox.checked);
        if (!checkedCategories) {
            allFilled = false;
        }
        // Enable/Disable submit button
        submitButton.disabled = !allFilled;
    }
    // Add event listeners to all required fields
    requiredFields.forEach(field => {
        field.addEventListener("input", validateForm);
    });
    // Add event listeners to category checkboxes
    categoryCheckboxes.forEach(checkbox => {
        checkbox.addEventListener("change", validateForm);
    });
    // Initial validation on page load
    validateForm();
});

