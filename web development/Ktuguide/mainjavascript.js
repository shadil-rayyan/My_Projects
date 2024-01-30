document.addEventListener('DOMContentLoaded', function () {
    const menuButton = document.querySelector('.menu-button');
    const mainNav = document.querySelector('.main-nav');
    const departmentItems = document.querySelectorAll('.has-dropdown');

    departmentItems.forEach(function (item) {
        item.addEventListener('click', function (event) {
            event.stopPropagation(); // Prevent the menu button from closing the department dropdown
            item.classList.toggle('active'); // Toggle the 'active' class for the clicked department
            // Close other department dropdowns
            departmentItems.forEach(function (otherItem) {
                if (otherItem !== item && otherItem.classList.contains('active')) {
                    otherItem.classList.remove('active');
                }
            });
        });
    });

    menuButton.addEventListener('click', function (event) {
        event.stopPropagation(); // Prevent the department dropdown from closing when clicking the menu button
        mainNav.classList.toggle('active');
    });

    document.addEventListener('click', function () {
        departmentItems.forEach(function (item) {
            item.classList.remove('active'); // Close all department dropdowns
        });
        mainNav.classList.remove('active'); // Close the main navigation
    });
});

